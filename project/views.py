from django.shortcuts import render

def mainfunction(request):
    return render(request, 'base.html')

def testfunction(request):
    return render(request, 'profile.html')

def test1function(request):
    return render(request, 'test.html')