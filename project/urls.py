from django.contrib import admin
from django.urls import path
from .views import mainfunction, my_page, user_list, show_user, testfunction

urlpatterns = [
    path('admin/', admin.site.urls),
    path('top/', user_list),
    path('mypage/', my_page),
    path('users/', user_list),
    path('aaa/', show_user),
    path('test/', testfunction)
]
