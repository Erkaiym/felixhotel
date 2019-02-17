from django.contrib import admin
from mainapp.models import Product, Partner, Review, Recommendation, Certificate, AboutCompany


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    fields = ['name', 'logo']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = ['name', 'image']


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    fields = ['name', 'company', 'comment', 'image', 'published']


@admin.register(Recommendation)
class RecommendationAdmin(admin.ModelAdmin):
    fields = ['company_name', 'image']


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    fields = ['title', 'image']


@admin.register(AboutCompany)
class AboutCompanyAdmin(admin.ModelAdmin):
    fields = ['title', 'text']
