from django.urls import path
from shop.views.base import IndexView
from shop.views.products import ProductView, ProductAddView, ProductUpdateView, ProductDelView, ProductDelConfirmView
from shop.views.reviews import ReviewUpdateView, ReviewDelView, ReviewDelConfirmView
from shop.views.accounts import register_user, LoginView, logout_view, ProfileView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('product/<int:pk>', ProductView.as_view(), name='product'),
    path('product_create/', ProductAddView.as_view(), name='product_add'),
    path('product_update/<int:pk>', ProductUpdateView.as_view(), name='product_update'),
    path('del/<int:pk>', ProductDelView.as_view(), name='product_del'),
    path('del_confirm/<int:pk>', ProductDelConfirmView.as_view(), name='product_del_confirm'),
    path('review_update/<int:pk>', ReviewUpdateView.as_view(), name='review_update'),
    path('del_r/<int:pk>', ReviewDelView.as_view(), name='review_del'),
    path('del_confirm_r/<int:pk>', ReviewDelConfirmView.as_view(), name='review_del_confirm'),
    path('register/', register_user, name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
]