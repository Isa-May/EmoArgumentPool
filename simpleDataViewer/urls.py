from django.urls import path
from simpleDataViewer import views

# URLConfiguration
urlpatterns = [
    path('', views.say_hello, name="say_hello"),
]