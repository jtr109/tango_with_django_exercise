from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context_dict = {'boldmessage': "I am bold font from the context"}

    return render(request, 'rango/index.html', context_dict)


def about(request):
    context_dict = {'about_message': "About page"}

    return render(request, 'rango/about.html', context_dict)
