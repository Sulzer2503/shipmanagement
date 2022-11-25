from django.urls import path
from . import views

urlpatterns = [
    path('spares/', views.spares_main),
    path('defects/', views.defects_main)
]