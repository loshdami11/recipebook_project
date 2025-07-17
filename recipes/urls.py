from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('create-recipe/', views.create_recipe,name='create-recipe'),
    path('success',views.success,name='success'),
]