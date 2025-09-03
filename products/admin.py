from django.contrib import admin
from .models import Category, Product, Order


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    search_fields = ['name']
    list_filter = ['created_at']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'stock', 'is_in_stock', 'created_at']
    list_filter = ['category', 'created_at', 'stock']
    search_fields = ['name', 'description']
    list_editable = ['price', 'stock']
    list_per_page = 20
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'description', 'category')
        }),
        ('Pricing and Stock', {
            'fields': ('price', 'stock')
        }),
        ('Media', {
            'fields': ('image',)
        }),
    )


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer_name', 'customer_email', 'product', 'quantity', 'total_price', 'created_at']
    list_filter = ['created_at', 'product__category']
    search_fields = ['customer_name', 'customer_email', 'product__name']
    readonly_fields = ['total_price', 'created_at']
    list_per_page = 20
