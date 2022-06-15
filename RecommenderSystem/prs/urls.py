from django.urls import path
from .import views

urlpatterns = [
    path('', views.index,name='index'),
    path('home/', views.home, name='home'),
    path('recommender/', views.rs, name='AwesomeRecommender'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('show/', views.show, name='show'),
]
