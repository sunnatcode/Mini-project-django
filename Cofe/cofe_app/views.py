from django.shortcuts import render
from django.views import View
from .models import MainPage, MainAboutProduct
# Create your views here.



def main(request):
    mainpage = MainPage.objects.all()
    aboutProduct = MainAboutProduct.objects.all()
    return render(request, 'block_main.html', {'main':mainpage, 'aboutProduct': aboutProduct})


def about_us(request):
    return render(request, 'about_us.html',{})


def shopView(request):
    return render(request, 'shop.html',{})

def bookView(request):
    return render(request, 'book.html',{})    