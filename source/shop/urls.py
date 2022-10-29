from django.urls import path
from shop.views.base import index_view

urlpatterns = [
    path('', index_view, name='index')
]