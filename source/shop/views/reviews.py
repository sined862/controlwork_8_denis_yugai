from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, View
from shop.models import Product, CategoryChoices, Review
from shop.forms import ProductForm, ReviewForm
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect, render, get_object_or_404


class ReviewUpdateView(UpdateView):
    template_name = 'review_update.html'
    model = Review
    form_class = ReviewForm

    # def post(self, request, *args, **kwargs):
        
    #     review = get_object_or_404(Product, pk=kwargs.get('pk'))
    #     print(f"Это --- {review.product_reviews} ")
    #     form = ReviewForm(request.POST)
    #     if form.is_valid():
    #         review.text = form.cleaned_data.get('text')
    #         review.rating = form.cleaned_data.get('rating')
    #         review.author = self.request.user
    #         review.save()
    #         # return redirect('product', pk=review.product)
    #     return reverse('review_update', kwargs={'pk': review.product})

    # def get_success_url(self):
    #     return reverse('product', kwargs={'pk': self.object.pk})

class ReviewDelView(DeleteView):
    template_name = 'confirm_delete_review.html'
    model = Review

    def get_success_url(self):
        return reverse('product_del', kwargs={'pk': self.object.pk})


class ReviewDelConfirmView(DeleteView):
    template_name = 'confirm_delete_review.html'
    model = Review
    success_url = reverse_lazy('index')