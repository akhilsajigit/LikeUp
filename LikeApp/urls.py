from django.urls import path
from LikeApp import views

urlpatterns = [
    path('',views.home_page, name="Home")
]