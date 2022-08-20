from django.http import HttpResponse
from .models import EmoArgument
from django.template import loader

def render_arguments(request):
    my_args=EmoArgument.objects.all().values()
    template = loader.get_template('render_arguments.html')
    context = {
        'my_args': my_args,
    }
    return HttpResponse(template.render(context, request))
