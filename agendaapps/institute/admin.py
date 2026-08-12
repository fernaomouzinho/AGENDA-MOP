from django.contrib import admin
from .models import Institution, Attendence, unitADN, DepartmentADN

# Register your models here.

admin.site.register(Institution)
admin.site.register(unitADN)
admin.site.register(DepartmentADN)
