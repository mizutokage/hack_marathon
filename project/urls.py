from django.contrib import admin
from django.urls import path
from .views import mainfunction, my_page, user_list, show_user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('/', mainfunction),
    path('mypage/', my_page),
    path('users/', user_list),
    path('<str:pk>', show_user)
]
