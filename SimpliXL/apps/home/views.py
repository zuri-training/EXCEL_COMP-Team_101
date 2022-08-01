from django.contrib.auth.decorators import login_required

from django.shortcuts import render


# Create your views here.

def home_page(request):
    return render(request, "home/index.html")


def about(request):
    return render(request, 'home/about.html')


@login_required
def dashboard(request):
    return render(request, 'home/dashboard.html')


@login_required
def authenticate(request):
    return render(request, 'home/authenticate.html')
