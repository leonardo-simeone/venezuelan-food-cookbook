from django.urls import path
from . import views

urlpatterns = [
    path('', views.recipes, name='recipes'),
    path('recipe/<int:pk>/', views.recipeUnit, name='recipeunit'),
]
