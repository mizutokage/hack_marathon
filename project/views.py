from django.shortcuts import render

def mainfunction(request):
    return render(request, 'base.html')

def my_page(reqeust):
    return render(reqeust, '.html')

def user_list(request):
    return render(request, 'users.html')

def show_user(request):
    return render(request, '.html')