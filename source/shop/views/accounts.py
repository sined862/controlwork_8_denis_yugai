from django.shortcuts import redirect, render, get_object_or_404
from shop.forms import UserRegisterForm, UserLoginForm
from django.contrib.auth import login, logout


def register_user(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})



def login_user(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
        print('Ошибка')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})