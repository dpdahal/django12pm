from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'frontend/pages/index/index.html')


def contact(request):
    return render(request, 'frontend/pages/contact/contact.html')
