from django.urls import path
from . import views

urlpatterns = [
    path('', views.recipes, name='recipes'),
    path('recipe/<int:pk>/', views.recipeUnit, name='recipeunit'),
    path('register/', views.registerView, name='register'),
    path('login/', views.loginView, name='login'),
    path('logout/', views.logoutView, name='logout'),
]
