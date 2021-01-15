from django.shortcuts import render
import requests
from bs4 import BeautifulSoup


# Create your views here.
def home(request):
    return render(request, template_name='my_app/index.html')


def new_search(request):
    search = request.POST.get('search')
    stuff_for_frontend = {
        'search': search,
        'title': 'Xanderslist',
    }
    return render(request, 'my_app/new_search.html', stuff_for_frontend)



