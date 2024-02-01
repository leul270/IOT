from django.shortcuts import render, redirect
from django.urls import path
from .forms import UserForm, CustomerResgistrationForm
from .models import user_form

# Create your views here.


def customer_registration(request):
    template_name = "user/registration.html"

    if request.method == "POST":
        form = CustomerResgistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect(
                "home"
            )  # Replace 'home' with the actual URL you want to redirect to after registration
    else:
        form = CustomerResgistrationForm()

    return render(request, template_name, {"form": form})


def home(request):
    context = {}
    return render(request, "home.html", context)


def user_home(request, id):
    USERFORM = user_form.objects.get(id=id)
    context = {"USERFORM": USERFORM}
    return render(request, "user/user_home.html", context)


def technician_home(request, id):
    context = {}
    return render(request, "technician/technician_home.html", context)


def administrator_home(request, id):
    USERFORM = user_form.objects.select_related("customer").all()
    USERFORM = user_form.objects.filter(customer__isnull=False)
    # USERFORM=user_form.objects.all()
    context = {"USERFORM": USERFORM}
    return render(request, "administrator/administrator_home.html", context)


def create_form(request):
    form = UserForm()
    if form.is_valid():
        form = form.save()
        return redirect("user_home")
    context = {"form": form}
    return render(request, "form.html", context)


# def device_create(request):
#     if request.method == 'POST':
#         form = UserForm(request.POST)
#         if form.is_valid():
#             device = form.save()
#             # Process the form data and redirect
#     else:
#         form = UserForm()
#         hardware_form = HardwareForm()
#         software_form = SoftwareForm()

#     return render(request, 'device_create.html', {
#         'form': form,
#         'hardwareForm': hardware_form,
#         'softwareForm': software_form
#     })
