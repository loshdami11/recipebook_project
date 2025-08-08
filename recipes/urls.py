from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create-recipe/', views.create_recipe, name='create-recipe'),
    path('success', views.success, name='success'),
    path('recpes/<int:recipe_id>/', views.recipe_detail, name='recipe-detail'),
    path('recipes/update-recipe/<int:recipe_id>/', views.update_recipe, name='update-recipe'),
    path('recipes/delete-recipe/<int:recipe_id>/', views.delete_recipe, name='delete-recipe'),
]