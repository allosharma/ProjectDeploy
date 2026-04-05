from django.shortcuts import render

# Create your views here.

def homePage(request):
    return render(request, 'index.html')


def orderPage(request):
    return render(request, 'orders.html')