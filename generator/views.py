from django.shortcuts import render
from django.http import HttpResponse
import random

def home(request):
    return render(request, 'generator/home.html')

def creator(request):
    return render(request, 'generator/creator.html')

def password(request):
    the_password = ''

    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    uppercase_alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    special_symbols = list('!@#$^%&*?<>+-=~`')
    numbers = list('0123456789')

    if request.GET.get('Uppercase'):
        alphabet.extend(uppercase_alphabet)

    if request.GET.get('Special symbols'):
        alphabet.extend(special_symbols)
        
    if request.GET.get('Numbers'):
        alphabet.extend(numbers)

    length = int(request.GET.get('Length', 10))

    for i in range(length):
        the_password += random.choice(alphabet)

    return render(request, 'generator/password.html', {'password': the_password})
