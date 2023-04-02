
from django.contrib import admin
from .models import Product, ProductBrand, ProductCategory, ProductColor, ProductDiscount
from .models import ProductTag


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Product._meta.fields]


@admin.register(ProductBrand)
class ProductBrandAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductBrand._meta.fields]


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductCategory._meta.fields]


@admin.register(ProductColor)
class ProductColorAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductColor._meta.fields]


@admin.register(ProductDiscount)
class ProductDiscountAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductDiscount._meta.fields]


@admin.register(ProductTag)
class ProductTagAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductTag._meta.fields]
