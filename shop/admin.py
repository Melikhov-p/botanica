from django.contrib import admin
from .models import Category, Product

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'amount', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'amount', 'available']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name', 'category__name']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
