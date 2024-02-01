from django.contrib import admin

# Register your models here.
from .models import Customer, Technician, Administrator, user_form, User

admin.site.register(User)
admin.site.register(Customer)
admin.site.register(Technician)
admin.site.register(Administrator)
admin.site.register(user_form)
