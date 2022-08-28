from django.urls import path
from simpleDataViewer import views

# URLConfiguration
urlpatterns = [
    path('', views.render_welcome_page, name="render_welcome_page"),

    path('render_arguments_by_topic_1/', views.render_arguments_by_topic_1, name="render_arguments_by_topic_1"),
    path('render_arguments_by_topic_2/', views.render_arguments_by_topic_2, name="render_arguments_by_topic_2"),
    path('render_arguments_by_topic_3/', views.render_arguments_by_topic_3, name="render_arguments_by_topic_3"),
    path('render_arguments_by_topic_4/', views.render_arguments_by_topic_4, name="render_arguments_by_topic_4"),
    path('render_arguments_by_topic_5/', views.render_arguments_by_topic_5, name="render_arguments_by_topic_5"),
    path('render_arguments_by_topic_6/', views.render_arguments_by_topic_6, name="render_arguments_by_topic_6"),

    path('render_arguments_by_topic_1_non_emo/', views.render_arguments_by_topic_1_non_emo, name="render_arguments_by_topic_1_non_emo"),
    path('render_arguments_by_topic_2_non_emo/', views.render_arguments_by_topic_2_non_emo, name="render_arguments_by_topic_2_non_emo"),
    path('render_arguments_by_topic_3_non_emo/', views.render_arguments_by_topic_3_non_emo, name="render_arguments_by_topic_3_non_emo"),
    path('render_arguments_by_topic_4_non_emo/', views.render_arguments_by_topic_4_non_emo, name="render_arguments_by_topic_4_non_emo"),
    path('render_arguments_by_topic_5_non_emo/', views.render_arguments_by_topic_5_non_emo, name="render_arguments_by_topic_5_non_emo"),
    path('render_arguments_by_topic_6_non_emo/', views.render_arguments_by_topic_6_non_emo, name="render_arguments_by_topic_6_non_emo"),



]