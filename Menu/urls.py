
from django.urls import path
from Menu import views

urlpatterns = [
    path('', views.home, name='home'),
    path('Sistemas-de-Comunicacion/', views.page_sc, name='page_sc'),
]