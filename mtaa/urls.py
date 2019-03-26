from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='mtaa-home'),
    path('about/', views.about, name='mtaa-about'),
]
