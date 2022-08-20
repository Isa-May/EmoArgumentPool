from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
# This is a request handler; it takes a request and returns a response
from django.template import loader
from .models import EmoArgument

def say_hello(request):
    my_args=EmoArgument.objects.all().values()
    output = ""
    for x in my_args:
        output += x["argument"]
    return HttpResponse(output)
    #return render(request, 'hello.html')
    #  template = loader.get_template('hello.html')
    #  return HttpResponse(template.render())
    #return HttpResponse('Hello World')

#def sort_by(request):
 #   return HttpResponse('')
