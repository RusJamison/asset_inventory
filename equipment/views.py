from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Equipment, HealthFacility, Department
from .forms import (
    EquipmentCreationForm,
    EquipmentUpdateForm,
)
import logging

# Create your views here.

# 1. function to render the page (view)
# 2. map function to A URL

logger = logging.getLogger(__name__)


def equipment_list(request):
    equipment_list = Equipment.objects.all()
    print(equipment_list)

    context = {"title": "Home Page", "equipments": equipment_list}
    return render(request, "equipment/index.html", context=context)


def create_equipment(request):
    form = EquipmentCreationForm()
    departments = Department.objects.all()
    facilities = HealthFacility.objects.all()

    print(facilities)

    if request.method == "POST":
        form = EquipmentCreationForm(request.POST, request.FILES)
        post_data = request.POST

        facility = HealthFacility.objects.get(id=post_data.get("facilities"))
        department = Department.objects.get(id=post_data.get("department"))
        print(f"post data:{post_data}")
        if form.is_valid():
            equipment = form.save(commit=False)
            equipment.health_facility = facility
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
                        health_facility=facility,
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
                    "facilities": facilities,
                }
                return render(request, "equipment/create.html", context=context)

            else:

                return redirect(reverse("equipment_list"))

        print(form.errors)

    context = {
        "title": "Create Equipment",
        "form": form,
        "departments": departments,
        "facilities": facilities,
    }
    return render(request, "equipment/create.html", context=context)


def equipment_details(request, asset_tag):
    equipment = Equipment.objects.get(asset_tag=asset_tag)
    facility = equipment.health_facility
    context = {
        "title": f"Equipment Details - {equipment.name}",
        "equipment": equipment,
        "facility": facility,
    }
    return render(request, "equipment/equipment_details.html", context=context)


def update_equipment(request, asset_tag):
    equipment = Equipment.objects.get(asset_tag=asset_tag)
    facility = equipment.health_facility
    print(equipment)

    form = EquipmentUpdateForm(instance=equipment)

    if request.method == "POST":
        form = EquipmentUpdateForm(request.POST, request.FILES, instance=equipment)

        if form.is_valid():
            form.save()
            return redirect(reverse("equipment_list"))

    context = {
        "title": f"Update Equipment {equipment.name}",
        "form": form,
        "facility": facility,
    }
    return render(request, "equipment/update.html", context=context)


def delete_equipment(request, asset_tag):
    equipment = Equipment.objects.get(asset_tag=asset_tag)

    if request.method == "POST":
        equipment.delete()
        return redirect(reverse("index"))

    return render(request, "equipment/delete.html", {"equipment": equipment})


#def about(request):
#    context = {"title": "About"}
#    return render(request, "equipment/about.html", context=context)


#def contact(request):
#    context = {"title": "Contact"}
    # return render(request, "equipment/contact.html", context=context)


#def equipment_list(request):
    # context = {}
    # return render(request, "equipment/list.html", context=context)


# !. Model (Database)
# 2. Views (Functions request into responses)
# 3. Temaplates (HTML templates)

