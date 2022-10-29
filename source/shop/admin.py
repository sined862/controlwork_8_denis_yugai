from django.contrib import admin
from shop.models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'image')
    list_filter = ('title', 'description', 'category')
    search_fields = ('title', 'description', 'category')
    fields = ('title', 'description', 'category', 'image')

admin.site.register(Product, ProductAdmin)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'product', 'rating')
    list_filter = ('author', 'product', 'rating')
    search_fields = ('author', 'product', 'rating')
    fields = ('author', 'product', 'text', 'rating')

admin.site.register(Review, ReviewAdmin)

