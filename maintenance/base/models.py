from django.db import models

# from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    is_staff = models.BooleanField(default=False)
    is_technician = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=True)

    def __str__(self):
        return self.username


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    department = models.CharField(max_length=100)
    campus = models.CharField(max_length=50)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class Administrator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    department = models.CharField(max_length=100)
    campus = models.CharField(max_length=50)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class Technician(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    department = models.CharField(max_length=100)
    campus = models.CharField(max_length=50)
    work_experiance = models.IntegerField()
    SKILL_LEVEL_CHOICES = (
        (1, "Beginner"),
        (2, "Intermediate"),
        (3, "Advanced"),
    )
    skill_level = models.IntegerField(choices=SKILL_LEVEL_CHOICES)
    short_description = models.TextField(null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    administrator = models.ForeignKey(
        Administrator, on_delete=models.CASCADE, default=1
    )

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class user_form(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    administrator = models.ForeignKey(
        Administrator, on_delete=models.CASCADE, default=1
    )
    technician = models.ForeignKey(Technician, on_delete=models.CASCADE, null=True)

    DEVICE_PROBLEM_CHOICES = [
        ("hardware", "Hardware"),
        ("software", "Software"),
    ]

    device_problem = models.CharField(max_length=20, choices=DEVICE_PROBLEM_CHOICES)
    can_the_pc_start = models.BooleanField(default=False)
    short_description = models.TextField(null=True)
    form_name = models.CharField(
        max_length=50,
    )

    def __str__(self):
        return self.short_description


class hardware_form(models.Model):
    short_description = models.TextField(null=True)

    def __str__(self):
        return self.short_description


class software_form(models.Model):
    short_description = models.TextField(null=True)

    def __str__(self):
        return self.short_description
