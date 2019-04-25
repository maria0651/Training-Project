from django.urls import path
from firstapp import views



urlpatterns = [
    path('first',views.index,name='index'),
    path('',views.home, name='home'),
    path('about/',views.about, name='about'),
    path('gallery/',views.gallery, name='gallery'),
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),

]