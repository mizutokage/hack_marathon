from django.contrib import admin
from django.urls import path
from .views import mainfunction, testfunction

urlpatterns = [
    path('admin/', admin.site.urls),
    path('top/', mainfunction),
    path('test/', testfunction)
]
