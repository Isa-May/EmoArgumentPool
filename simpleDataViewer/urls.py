from django.urls import path
from simpleDataViewer import views

# URLConfiguration
urlpatterns = [

    path('render_arguments/', views.render_arguments, name="render_arguments"),
    path('render_arguments_by_topic/', views.render_arguments_by_topic, name="render_arguments_by_topic"),

]