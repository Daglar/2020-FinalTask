from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ('title',)
    list_display = ('title', )
    list_filter = ('created_at',)
    search_fields = ('title',)


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    fields = ('title','parent_id',)
    list_display = ('title','parent_id',)
    list_filter = ('created_at',)
    search_fields = ('title',)



@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    fields = ('title',)
    list_display = ('title', )
    list_filter = ('created_at',)
    search_fields = ('title',)

@admin.register(ProductProperty)
class ProductPropertyAdmin(admin.ModelAdmin):
    fields = ('title', 'productproperty_id', )
    list_display = ('title', 'productproperty_id',)
    search_fields = ('title',)

# @admin.register(CategoryProperty)
# class CategoryPropertyAdmin(admin.ModelAdmin):
#     fields = ('title', 'category',)
#     list_display = ('title', 'category',)
#     search_fields = ('title',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = ('title', 'image', 'price', 'category', 'brand', )
    list_display = ('title', 'image', 'price', 'category', 'brand', )
    search_fields = ('title', 'price', 'category', 'brand',)