from django.urls import path
from simpleDataViewer import views

# URLConfiguration
urlpatterns = [
    path('', views.render_arguments, name="render_arguments"),
]