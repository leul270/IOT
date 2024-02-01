from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path(
        "customer_registration",
        views.customer_registration,
        name="customer_registration",
    ),
    path("user_home/<str:id>/", views.user_home, name="user_home"),
    path("technician_home/<str:id>/", views.technician_home, name="technician_home"),
    path(
        "administrator_home/<str:id>/",
        views.administrator_home,
        name="administrator_home",
    ),
    path("create_form/", views.create_form, name="create_form"),
]
