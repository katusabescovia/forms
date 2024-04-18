from django.urls import path
from .  import  views

urlpatterns = [
    path('', views.sitterform, name='sitterform'),
    path('add/', views.add, name='add'),
    
    path('edit/<int:id>/', views.edit, name='edit'),
    path('read/<int:id>/', views.read, name='read'),
    

]