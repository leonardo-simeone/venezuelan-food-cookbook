from django.urls import path
from . import views

urlpatterns = [
    path('', views.recipes, name='recipes'),
    path('recipe/<str:pk>/', views.recipeUnit, name='recipeunit'),
    path('register/', views.registerView, name='register'),
    path('login/', views.loginView, name='login'),
    path('logout/', views.logoutView, name='logout'),
    path('create-recipe/', views.createRecipe, name='create-recipe'),
    path('update-recipe/<str:pk>/', views.updateRecipe, name='update-recipe'),
    path('delete-recipe/<str:pk>/', views.deleteRecipe, name='delete-recipe'),
    path('about-us/', views.aboutUs, name='about-us'),
    path('gallery/', views.gallery, name='gallery'),
    path('like-recipe/<str:pk>/', views.likeRecipe, name='like-recipe'),
    path('contact/', views.contact, name='contact'),
]
