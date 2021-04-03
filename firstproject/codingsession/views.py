from django.shortcuts import render,HttpResponse

# Create your views here.

def codingsessionspage(request):
    return HttpResponse('<h1>Hello World</h1>')
