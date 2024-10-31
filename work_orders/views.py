from django.shortcuts import render, redirect
from .models import ScheduledWorkOrder, UnscheduledWorkOrder
from .forms import ScheduledWorkOrderForm, UnScheduleWorkOrderForm
from django.urls import reverse
from equipment.models import Equipment
from equipment.forms import EquipmentCreationForm
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required()
def scheduled_work_orders(request):
    work_orders = ScheduledWorkOrder.objects.all()
    context = {"title": "Scheduled Work Orders","work_orders":work_orders}
    return render(request, "work_orders/scheduled_work_orders.html", context=context)

@login_required()
def create_scheduled_work_order(request, asset_tag):
    equipment = Equipment.objects.get(asset_tag=asset_tag)
    equipment_form = EquipmentCreationForm(instance=equipment)
    form = ScheduledWorkOrderForm()

    if request.method == "POST":
        form = ScheduledWorkOrderForm(request.POST)


        if form.is_valid():
            work_order = form.save(commit=False)
            work_order.equipment = equipment
            work_order.save()

            return redirect(reverse("scheduled_work_orders"))

        print(form.errors)

    context = {
        "work_order_form": form,
        "equipment_form": equipment_form
    }
    return render(request, "work_orders/create_scheduled_work_order.html", context)

@login_required()
def unscheduled_work_orders(request):
    work_orders = UnscheduledWorkOrder.objects.all()
    context = {"title": "Unscheduled Work Orders","work_orders":work_orders}
    return render(request, "work_orders/unscheduled_work_orders.html", context=context)

@login_required()
def create_unscheduled_work_order(request, asset_tag):
    form = UnScheduleWorkOrderForm()
    
    equipment = Equipment.objects.get(asset_tag=asset_tag)
    equipment_form = EquipmentCreationForm(instance=equipment)
    

    if request.method == "POST":
        form = UnScheduleWorkOrderForm(request.POST, request.FILES)


        if form.is_valid():
            work_order = form.save(commit=False)
            work_order.equipment = equipment
            work_order.save()

            return redirect(reverse("unscheduled_work_orders"))

        print(form.errors)

    context = {
        "work_order_form": form,
        "equipment_form": equipment_form
    }

    return render(request, "work_orders/create_unscheduled_work_order.html", context)

def scheduled_work_order_detail(request, work_order_num):
    work_order = ScheduledWorkOrder.objects.get(
        work_order_num = work_order_num
    )
    return render(request,"work_orders/scheduled_detail.html",{
        'work_order':work_order
    })

def unscheduled_work_order_detail(request, work_order_num):
    work_order = UnscheduledWorkOrder.objects.get(
        work_order_num = work_order_num
    )
    return render(request,"work_orders/unscheduled_detail.html",{
        'work_order':work_order
    })


