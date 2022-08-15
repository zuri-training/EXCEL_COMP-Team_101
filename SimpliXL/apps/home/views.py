from django.contrib.auth.decorators import login_required

from django.shortcuts import render


# Create your views here.

def home_page(request):
    return render(request, "home/index.html")


def about(request):
    return render(request, 'home/about.html')


def feature(request):
    return render(request, 'home/feature.html')


def how_to(request):
    return render(request, 'home/how_to.html')

def request_tool(request):
    return render(request, 'home/request.html')

def terms(request):
    return render(request, 'home/terms.html')

def contact_us(request):
    return render(request, 'home/contactus.html')

def help(request):
    return render(request, 'home/help.html')



@login_required
def dashboard(request):
    return render(request, 'home/dashboard.html')


@login_required
def authenticate(request):
    return render(request, 'home/authenticate.html')
