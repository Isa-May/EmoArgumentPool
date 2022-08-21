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


def render_arguments_by_topic(request):
    my_args = EmoArgument.objects.all().filter(topic='tv-is-better-than-books')
    template = loader.get_template('render_arguments.html')
    context = {
        'my_args': my_args,
    }
    return HttpResponse(template.render(context, request))

#render arguments on certain topics
### emotional or non-emotional
### pro or contra


    # if contains school-uniform in topic
    # tv-is-better-than-books
    # firefox-vs-internet-explorer
    # ban-plastic-water-bottles


