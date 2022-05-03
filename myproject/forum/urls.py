from django.urls import path, include
from . import views


app_name = 'forum'
urlpatterns = [
    path('', views.home, name="home"),
    path('questions/<int:pk>/', views.TopicDetailView.as_view(), name="detail"),
    path('questions/', views.IndexView.as_view(), name="index"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', views.register, name='register'),
    path('questions/create/', views.create_q, name='create_q'),
    # path('questions/<int:pk>/write', views.create_a, name='create_a'),
]