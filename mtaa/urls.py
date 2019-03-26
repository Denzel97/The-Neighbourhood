from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='mtaa-home'),
    path('business/', views.business, name='mtaa-business'),
]
