from django.urls import path
from simpleDataViewer import views

# URLConfiguration
urlpatterns = [
    path('hello/', views.say_hello)
]