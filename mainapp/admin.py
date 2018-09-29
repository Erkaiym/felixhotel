from django.contrib import admin
from mainapp.models import Product, Partner


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    fields = ['name', 'logo']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = ['name', 'image']
