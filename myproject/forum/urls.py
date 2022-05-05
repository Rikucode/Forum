from django.urls import path, include
from . import views


app_name = 'forum'
urlpatterns = [
    path('', views.home, name="home"),
    path('forum/<int:pk_theme>/themes/<int:pk_topic>/page=<int:page>', views.topic_messages, name="detail"),
    path('forum/<int:pk_theme>/themes/page=<int:page>', views.topics, name="topic"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', views.register, name='register'),
    path('forum/<int:pk_theme>/themes/create/', views.create_topic, name='create_topic'),
    path('forum/page=<int:page>', views.themes, name="theme"),
    path('forum/create', views.create_theme, name='create_theme'),
]