from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import RegistrationForm as reg_form
from .models import *


# Контроллер головної сторінки
def main_page(request):
    context = {'title': 'YorsGate'}
    return render(request, 'users/index.html', context=context)


# Контроллер для ідентифікації і реєстрації користувачів
def register(request):
    # Якщо форма не була заповнена відмальовуємо її інакше проводимо валідацію
    if request.method != 'POST':
        form = reg_form()
    else:
        form = reg_form(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect('game:shop')

    context = {'title': 'YorsGate', 'form': form}
    return render(request, 'registration/register.html', context=context)
