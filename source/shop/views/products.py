from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, View
from shop.models import Product, CategoryChoices, Review
from shop.forms import ProductForm, ReviewForm
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect, render, get_object_or_404
from django.db.models import Avg
from django.contrib.auth.mixins import LoginRequiredMixin


class ProductView(LoginRequiredMixin, DetailView):
    template_name = 'product.html'
    model = Product
    extra_context = {'choices': CategoryChoices.choices}
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form_review = ReviewForm
        print(self.object.id)
        avg_rating = Review.objects.filter(product=self.object.id).aggregate(avg=Avg('rating'))
        context['avg_rating'] = avg_rating
        context['form_review'] = form_review
        return context

    def post(self, request, *args, **kwargs):
        product = get_object_or_404(Product, pk=kwargs.get('pk'))
        form = ReviewForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data.get('text')
            rating = form.cleaned_data.get('rating')
            author = self.request.user
            Review.objects.create(author=author, product=product, text=text, rating=rating)
            return redirect('product', pk=product.id)
        return reverse('product', kwargs={'pk': product.id})

class ProductAddView(LoginRequiredMixin, CreateView):
    template_name = 'product_create.html'
    model = Product
    form_class = ProductForm
    extra_context = {'choices': CategoryChoices.choices}

    def get_success_url(self):
        return reverse('product', kwargs={'pk': self.object.pk})


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'product_update.html'
    model = Product
    form_class = ProductForm
    extra_context = {'choices': CategoryChoices.choices}

    def get_success_url(self):
        return reverse('product', kwargs={'pk': self.object.pk})


class ProductDelView(LoginRequiredMixin, DeleteView):
    template_name = 'confirm_delete.html'
    model = Product

    def get_success_url(self):
        return reverse('product_del', kwargs={'pk': self.object.pk})


class ProductDelConfirmView(LoginRequiredMixin, DeleteView):
    template_name = 'confirm_delete.html'
    model = Product
    success_url = reverse_lazy('index')