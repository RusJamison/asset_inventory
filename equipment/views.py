from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Equipment, HealthFacility, Department, EquipmentLocation
from .forms import (
    EquipmentCreationForm,
    EquipmentUpdateForm,
)
import logging
from django.contrib.auth.decorators import login_required
from .utils import search_all_models_full_text
from django.core.paginator import Paginator

from django.http import HttpResponse
from reportlab.lib.pagesizes import A4
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from io import BytesIO

# import requests


logger = logging.getLogger(__name__)


@login_required()
def generate_equipment_pdf(request):
    # Create a BytesIO buffer to receive PDF data
    buffer = BytesIO()

    # Create the PDF object, using the buffer as its "file."
    doc = SimpleDocTemplate(buffer, pagesize=A4)

    # Container for the 'Flowable' objects
    elements = []

    # Get sample styles
    styles = getSampleStyleSheet()
    title_style = styles["Title"]
    header_style = styles["Heading2"]
    normal_style = styles["BodyText"]

    # Add Title
    title = Paragraph("Equipment List", title_style)
    elements.append(title)
    elements.append(Spacer(1, 12))

    # Add a description or any introductory text
    intro_text = "This document contains a list of all\
         equipment in the inventory."
    intro_paragraph = Paragraph(intro_text, normal_style)
    elements.append(intro_paragraph)
    elements.append(Spacer(1, 12))

    # Query all Equipment objects
    user = request.user
    if user.is_superuser:
        equipments = Equipment.objects.all()
    else:
        equipments = (
            Equipment.objects.filter(
                location__health_facility=user.health_facility)
            .all()
            .order_by("-created_at")
        )

    # Define table data with headers
    table_data = [
        [
            "Asset Tag",
            "Name",
            "Model",
            "Serial No",
            "Price",
            "Status",
            "Location"]
    ]

    # Populate table data
    for equipment in equipments:
        table_data.append([
          equipment.asset_tag,
          equipment.name,
          equipment.model,
          equipment.serial_no,
          f"${equipment.price}",
          equipment.status,
          equipment.location.health_facility if equipment.location else "N/A",
        ]
        )

    # Create the table
    table = Table(
        table_data,
        repeatRows=1,
    )

    # Style the table
    table_style = TableStyle(
        [
            ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#d3d3d3")),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.green),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("BOTTOMPADDING", (0, 0), (-1, 0), 12),
            ("GRID", (0, 0), (-1, -1), 0.5, colors.green),
        ]
    )
    table.setStyle(table_style)

    # Alternate row colors
    for i in range(1, len(table_data)):
        if i % 2 == 0:
            bg_color = colors.whitesmoke
        else:
            bg_color = colors.lightgrey
        table_style.add("BACKGROUND", (0, i), (-1, i), bg_color)

    elements.append(table)
    elements.append(Spacer(1, 24))

    # Build the PDF
    doc.build(elements)

    # Get the value of the BytesIO buffer and write it to the response.
    pdf = buffer.getvalue()
    buffer.close()
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = 'attachment; \
        filename="equipment_list.pdf"'
    response.write(pdf)
    return response


@login_required()
def equipment_list(request):
    user = request.user
    if user.is_superuser:
        equipment_list = Equipment.objects.all()
    else:
        equipment_list = Equipment.objects.filter(
            location__health_facility=user.health_facility
        ).all()
    print(equipment_list)
    paginator = Paginator(equipment_list, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {"title": "Home Page", "page_obj": page_obj}
    return render(request, "equipment/index.html", context=context)


@login_required()
def create_equipment(request):
    form = EquipmentCreationForm()
    facility = request.user.health_facility
    departments = Department.objects.filter(health_facility=facility).all()

    if request.method == "POST":
        form = EquipmentCreationForm(request.POST, request.FILES)
        post_data = request.POST
        print(post_data)
        facility = HealthFacility.objects.get(id=post_data.get("facilities"))
        department = Department.objects.get(id=post_data.get("department"))

        location_record = EquipmentLocation.objects.create(
            health_facility=facility,
            department=department,
        )

        if form.is_valid():
            equipment = form.save(commit=False)
            equipment.location = location_record
            equipment.save()

            if "save_and_add" in request.POST:
                return redirect(reverse("create_equipment"))

            elif "save_and_duplicate" in request.POST:
                form = EquipmentCreationForm(
                    instance=Equipment(
                        manufacturer=equipment.manufacturer,
                        model=equipment.model,
                        name=equipment.name,
                        description=equipment.description,
                        status=equipment.status,
                        location=location_record,
                        warranty_start_date=equipment.warranty_start_date,
                        warranty_end_date=equipment.warranty_end_date,
                        in_use_as_of_date=equipment.in_use_as_of_date,
                        service_provider=equipment.service_provider,
                        category=equipment.category,
                    )
                )

                context = {
                    "title": "Create Equipment",
                    "form": form,
                    "departments": departments,
                    "facility": facility,
                }
                return render(
                    request,
                    "equipment/create.html",
                    context=context
                )

            else:

                return redirect(reverse("equipment_list"))

        print(form.errors)

    context = {
        "title": "Create Equipment",
        "form": form,
        "departments": departments,
        "facility": facility,
    }
    return render(request, "equipment/create.html", context=context)


@login_required()
def equipment_details(request, asset_tag):
    equipment = Equipment.objects.get(asset_tag=asset_tag)
    location = equipment.location
    context = {
        "title": f"Equipment Details - {equipment.name}",
        "equipment": equipment,
        "location": location,
    }
    return render(request, "equipment/equipment_details.html", context=context)


@login_required()
def update_equipment(request, asset_tag):
    equipment = Equipment.objects.get(asset_tag=asset_tag)
    facility = request.user.health_facility
    facilities = HealthFacility.objects.all()

    departments_in_facility = Department.objects.filter(
        health_facility=facility
    ).all()
    all_departments = Department.objects.all()

    form = EquipmentUpdateForm(instance=equipment)

    if request.method == "POST":
        department_id = request.POST.get("department")
        facility_id = request.POST.get("facilities")
        print(f"Facility_id>>>{request.POST}")

        department = Department.objects.get(id=department_id)

        print(f"Department >>>{department}")
        facility = HealthFacility.objects.get(id=facility_id)

        form = EquipmentUpdateForm(
            request.POST,
            request.FILES,
            instance=equipment
        )

        if form.is_valid():
            equipment = form.save(commit=False)
            equipment.location.health_facility = facility
            equipment.location.department = department
            equipment.location.save()
            equipment.save()
            return redirect(reverse("equipment_list"))

    context = {
        "title": f"Update Equipment {equipment.name}",
        "form": form,
        "departments": all_departments,
        "facility_depts": departments_in_facility,
        "facility": facility,
        "facilities": facilities,
    }
    return render(request, "equipment/update.html", context=context)


@login_required()
def delete_equipment(request, asset_tag):
    equipment = Equipment.objects.get(asset_tag=asset_tag)

    if request.method == "POST":
        equipment.delete()
        return redirect(reverse("equipment_list"))

    return render(request, "equipment/delete.html", {"equipment": equipment})


@login_required()
def search_view(request):
    query = request.GET.get("search", "")

    if query:
        results = search_all_models_full_text(query)
        all_items = [
            {"entity": entity_name, "item": item}
            for entity_name, queryset in results.items()
            for item in queryset
        ]
        print(all_items)
        results = all_items
    else:
        # return empty queryset if no search term
        results = Equipment.objects.none()

    return render(
        request, "equipment/search_results.html",
        {"query": query, "results": results}
    )
