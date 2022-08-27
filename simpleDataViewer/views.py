from django.http import HttpResponse
from .models import EmoArgument
from django.template import loader

def render_arguments(request):
    my_args=EmoArgument.objects.all().values()
    template = loader.get_template('render_arguments_emo.html')
    context = {
        'my_args': my_args,
    }
    return HttpResponse(template.render(context, request))


def render_arguments_by_topic_1(request):
    my_args = EmoArgument.objects.all().filter(topic='tv-is-better-than-books', label=1)
    template = loader.get_template('render_arguments_emo.html')
    context = {
        'my_args': my_args,
    }
    return HttpResponse(template.render(context, request))

def render_arguments_by_topic_2(request):
    my_args = EmoArgument.objects.all().filter(topic='firefox-vs-internet-explorer', label=1)
    template = loader.get_template('render_arguments_emo.html')
    context = {
        'my_args': my_args,
    }
    return HttpResponse(template.render(context, request))

def render_arguments_by_topic_3(request):
    my_args = EmoArgument.objects.all().filter(topic='ban-plastic-water-bottles', label=1)
    template = loader.get_template('render_arguments_emo.html')
    context = {
        'my_args': my_args,
    }
    return HttpResponse(template.render(context, request))

def render_arguments_by_topic_4(request):
    my_args = EmoArgument.objects.all().filter(topic='if-your-spouse-committed-murder-and-he-or-she-confided-in-you-would-you-turn-them-in-', label=1)
    template = loader.get_template('render_arguments_emo.html')
    context = {
        'my_args': my_args,
    }
    return HttpResponse(template.render(context, request))

def render_arguments_by_topic_5(request):
    my_args = EmoArgument.objects.all().filter(topic='pro-choice-vs-pro-life', label=1)
    template = loader.get_template('render_arguments_emo.html')
    context = {
        'my_args': my_args,
    }
    return HttpResponse(template.render(context, request))


def render_arguments_by_topic_6(request):
    my_args = EmoArgument.objects.all().filter(topic='evolution-vs-creation', label=1)
    template = loader.get_template('render_arguments_emo.html')
    context = {
        'my_args': my_args,
    }
    return HttpResponse(template.render(context, request))


def render_welcome_page(request):
    template = loader.get_template('welcome.html')
    return HttpResponse(template.render({}, request))
