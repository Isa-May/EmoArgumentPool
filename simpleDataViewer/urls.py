from django.urls import path
from simpleDataViewer import views

# URLConfiguration
urlpatterns = [
    path('', views.render_welcome_page, name="render_welcome_page"),
    path('render_arguments/', views.render_arguments, name="render_arguments"),
    path('render_arguments_by_topic_1/', views.render_arguments_by_topic_1, name="render_arguments_by_topic_1"),
    path('render_arguments_by_topic_2/', views.render_arguments_by_topic_2, name="render_arguments_by_topic_2"),
    path('render_arguments_by_topic_3/', views.render_arguments_by_topic_3, name="render_arguments_by_topic_3"),
]