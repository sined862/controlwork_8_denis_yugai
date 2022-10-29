from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, View
from shop.models import Product, CategoryChoices, Review
from shop.forms import ProductForm, ReviewForm
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect, render, get_object_or_404


class ReviewUpdateView(UpdateView):
    template_name = 'review_update.html'
    model = Review
    form_class = ReviewForm


class ReviewDelView(DeleteView):
    template_name = 'confirm_delete_review.html'
    model = Review

    def get_success_url(self):
        return reverse('product_del', kwargs={'pk': self.object.pk})


class ReviewDelConfirmView(DeleteView):
    template_name = 'confirm_delete_review.html'
    model = Review
    success_url = reverse_lazy('index')