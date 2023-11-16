from django.shortcuts import render

def aboutUs (request):
    return render(request, 'aboutUs/aboutUs.html')
