from django.urls import path
from . import views

urlpatterns = [
    path('scheduled_work_orders/', views.scheduled_work_orders, name='scheduled_work_orders'),
    path('create_scheduled_work_order/<str:asset_tag>/', views.create_scheduled_work_order, name='create_scheduled_work_order'),
    path('unscheduled_work_orders/', views.unscheduled_work_orders, name='unscheduled_work_orders'),
    path('create_unscheduled_work_order/<str:asset_tag>/', views.create_unscheduled_work_order, name='create_unscheduled_work_order'),  # new route added here.
]
