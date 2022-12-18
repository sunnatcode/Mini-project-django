from django.urls import path
from .views import about_us, main, shopView, bookView
app_name = 'cofe'

urlpatterns = [
    path('', main, name='main'),
    path('about_us/',  about_us, name='about_us'),
    path('shop/',  shopView, name='shop'),
    path('book/',  bookView, name='book'),
]