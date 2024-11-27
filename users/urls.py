from . import views
from django.urls import path


urlpatterns = [
    path('verification_pending/', views.verification_pending,
         name='verification_pending'),
]
