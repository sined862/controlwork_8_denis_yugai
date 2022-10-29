from django import forms
from shop.models import Product, Review
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User



class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


class LoginForm(forms.Form):
    username = forms.CharField(
        required=True,
        label='Логин'
    )
    password = forms.CharField(
        required=True,
        label='Пароль',
        widget=forms.PasswordInput
    )


class ProductForm(forms.ModelForm):
     class Meta:
        model = Product
        fields = ('title', 'description', 'category', 'image')
        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'style': 'height:150px'}),
            'category': forms.RadioSelect
        }


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('text', 'rating',)
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control', 'style': 'height:150px'})
        }