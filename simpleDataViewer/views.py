from django.http import HttpResponse
from .models import EmoArgument


# Create your views here.
# This is a request handler; it takes a request and returns a response
from django.template import loader
from django.shortcuts import render


def say_hello(request):
    my_args=EmoArgument.objects.all().values()
    template = loader.get_template('hello.html')
    context = {
        'my_args': my_args,
    }
 #   output = ""
  #  for x in my_args:
   #     output += x["argument"]
    return HttpResponse(template.render(context, request))
    #return render(request, 'hello.html')
    #  template = loader.get_template('hello.html')
    #  return HttpResponse(template.render())
    #return HttpResponse('Hello World')

#def sort_by(request):
 #   return HttpResponse('')
