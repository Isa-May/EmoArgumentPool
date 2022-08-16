from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
# This is a request handler; it takes a request and returns a response

def say_hello(request):
    #return render(request, 'hello.html')
    return HttpResponse('Hello World')

#def sort_by(request):
 #   return HttpResponse('')