from http import client
from itertools import product
from django.contrib import admin
from core.erp.models import  *

from import_export.admin import ImportExportModelAdmin

# Register your models here.
""" admin.site.register(Category)
admin.site.register(Client)
admin.site.register(Product) """
@admin.register(Category, Client ,Product)
class ViewAdmin(ImportExportModelAdmin):
    pass