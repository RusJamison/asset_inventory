from django.urls import path
from . import views

urlpatterns = [
    path("equipment_list/", views.equipment_list, name="equipment_list"),
    # path('about/',views.about,name='about'),
    # path('contact/',views.contact,name='contact'),  # new route added here.
    path("create/", views.create_equipment, name="create_equipment"),
    path("details/<str:asset_tag>/", views.equipment_details, name="equipment_details"),
    path("edit/<str:asset_tag>/", views.update_equipment, name="edit_equipment"),
    path("delete/<str:asset_tag>/", views.delete_equipment, name="delete_equipment"),
    path("search/", views.search_view, name="search_equipment"),
    path('reports/equipment/', views.generate_equipment_pdf, name='equipment_pdf'),
    # path('equipment_list/', views.equipment_list, name='equipment_list'),
]

# about => /about
# index => /
# contact => /contact
