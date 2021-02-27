from django.contrib import admin
from django.urls import path
from .views import mainfunction, testfunction, test1function

urlpatterns = [
    path('admin/', admin.site.urls),
    path('top/', mainfunction),
    path('test/', testfunction),
    path('test1/', test1function)
]
