from django.urls import path 
from . import views


urlpatterns = [
    path('main/', views.home, name ="home"), 

    path('about/', views.about, name = "about"),

    path('menu/', views.menu, name = "menu"), 

    path('menu/<int:pk>/', views.item, name= "item"), 
    
    path('book/', views.book, name = "book"),
]
