from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import (
    user_form,
    hardware_form,
    software_form,
    Customer,
    User,
    Administrator,
)


class CustomerResgistrationForm(UserCreationForm):
    department = forms.CharField(max_length=50)
    campus = forms.CharField(max_length=50)

    class Meta(UserCreationForm.Meta):
        model = User
        # fields = "__all__"
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
            "department",
            "campus",
        ]

    def save(self, commit=True):
        user = super().save()
        department = self.cleaned_data["department"]
        campus = self.cleaned_data["campus"]
        customer = Customer.objects.create(
            user=user, department=department, campus=campus
        )
        return user


class TechnicianResgistrationForm(UserCreationForm):
    department = forms.CharField(max_length=50)
    campus = forms.CharField(max_length=50)

    work_experiance = forms.IntegerField()
    SKILL_LEVEL_CHOICES = (
        (1, "Beginner"),
        (2, "Intermediate"),
        (3, "Advanced"),
    )
    skill_level = forms.ChoiceField(choices=SKILL_LEVEL_CHOICES)
    short_description = forms.CharField(widget=forms.Textarea)

    administrator = forms.ModelChoiceField(
        queryset=Administrator.objects.all(), required=False
    )

    class Meta(UserCreationForm.Meta):
        model = User
        # fields = "__all__"
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
            "department",
            "campus",
        ]

    def save(self, commit=True):
        user = super().save()
        department = self.cleaned_data["department"]
        work_experiance = self.cleaned_data["work_experiance"]
        campus = self.cleaned_data["campus"]
        skill_level = self.cleaned_data["skilllevel"]
        administrator = self.cleaned_data["administrator"]
        technician = Technician.objects.create(
            user=user,
            department=department,
            campus=campus,
            work_experiance=work_experiance,
            skill_level=skill_level,
            administrator=administrator,
        )
        return user


class UserForm(ModelForm):
    class Meta:
        model = user_form
        fields = "__all__"


class HardwareForm(ModelForm):
    class Meta:
        model = hardware_form
        fields = "__all__"


class SoftwareForm(ModelForm):
    class Meta:
        model = software_form
        fields = "__all__"
