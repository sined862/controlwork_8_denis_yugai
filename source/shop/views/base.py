from django.views.generic import ListView
from shop.models import Product, CategoryChoices


class IndexView(ListView):
    template_name = 'index.html'
    model = Product
    context_object_name = 'products'
    ordering = ('-id',)
    extra_context = {'choices': CategoryChoices.choices}

