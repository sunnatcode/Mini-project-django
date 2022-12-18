from django.contrib import admin

# Register your models here.
from .models import MainPage, MainAboutProduct


admin.site.register(MainAboutProduct)
admin.site.register(MainPage)