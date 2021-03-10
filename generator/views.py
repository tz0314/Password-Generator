from django.shortcuts import render
from django.http import HttpResponse
import string
import random


# Create your views here.

def home(request):
    return render(request, 'generator/home.html')


def password(request):
    password_characters = list(string.ascii_lowercase)
    upper_case_letters = list(string.ascii_uppercase)
    numbers = list('1234567890')
    special_characters = list('!@#$%^&*()<>?')

    if request.GET.get('uppercase'):
        password_characters.extend(upper_case_letters)
    if request.GET.get('numbers'):
        password_characters.extend(numbers)
    if request.GET.get('special'):
        password_characters.extend(special_characters)

    length = int(request.GET.get('length', 12))

    the_password = ''
    for char in range(length):
        the_password += random.choice(password_characters)

    return render(request, 'generator/password.html', {'password': the_password})

def about(request):
    return render(request, 'generator/about.html')
