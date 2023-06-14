from django.urls import path, include
from rest_framework.routers import DefaultRouter
from user_app.api import views



urlpatterns = [
    path('movie/', views.movie_list, name= "movie_list"),
    path('movie/<int:pk>', views.movie_details, name= "movie_details"),
    

]