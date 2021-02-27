from django.shortcuts import render

def mainfunction(request):
    return render(request, 'base.html')

def testfunction(request):
    return render(request, 'profile.html')