from django.urls import path
from simpleDataViewer import views

urlpatterns = [
    path('', views.render_welcome_page, name="render_welcome_page"),

    path('render_arguments_by_topic_1/', views.render_arguments_by_topic_1_emo, name="render_arguments_by_topic_1_emo"),
    path('render_arguments_by_topic_2/', views.render_arguments_by_topic_2_emo, name="render_arguments_by_topic_2_emo"),
    path('render_arguments_by_topic_3/', views.render_arguments_by_topic_3_emo, name="render_arguments_by_topic_3_emo"),
    path('render_arguments_by_topic_4/', views.render_arguments_by_topic_4_emo, name="render_arguments_by_topic_4_emo"),
    path('render_arguments_by_topic_5/', views.render_arguments_by_topic_5_emo, name="render_arguments_by_topic_5_emo"),
    path('render_arguments_by_topic_6/', views.render_arguments_by_topic_6_emo, name="render_arguments_by_topic_6_emo"),

    path('render_arguments_by_topic_1_non_emo/', views.render_arguments_by_topic_1_non_emo, name="render_arguments_by_topic_1_non_emo"),
    path('render_arguments_by_topic_2_non_emo/', views.render_arguments_by_topic_2_non_emo, name="render_arguments_by_topic_2_non_emo"),
    path('render_arguments_by_topic_3_non_emo/', views.render_arguments_by_topic_3_non_emo, name="render_arguments_by_topic_3_non_emo"),
    path('render_arguments_by_topic_4_non_emo/', views.render_arguments_by_topic_4_non_emo, name="render_arguments_by_topic_4_non_emo"),
    path('render_arguments_by_topic_5_non_emo/', views.render_arguments_by_topic_5_non_emo, name="render_arguments_by_topic_5_non_emo"),
    path('render_arguments_by_topic_6_non_emo/', views.render_arguments_by_topic_6_non_emo, name="render_arguments_by_topic_6_non_emo"),



]