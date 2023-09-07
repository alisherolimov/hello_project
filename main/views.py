from django.shortcuts import render, redirect
from .models import *

def index_view(request):
    context = {
        'banner': Banner.objects.last(),
        'about': About.objects.all(),
        'blog': Blog.objects.all(),
    }
    return render(request, 'index.html', context)


def create_reservation_view(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        Contact.objects.create(
            name=name,
            email=email,
            message=message,
        )
        return redirect('index_url')
    return render(request, 'index.html')