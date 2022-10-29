from django.views.generic import ListView
from shop.models import Product, CategoryChoices
from django.contrib.auth.mixins import LoginRequiredMixin


class IndexView(LoginRequiredMixin, ListView):
    template_name = 'index.html'
    model = Product
    context_object_name = 'products'
    ordering = ('-id',)
    extra_context = {'choices': CategoryChoices.choices}

