from django.test import TestCase
from django.urls import reverse, resolve
from . import views


class TestUrls(TestCase):

    """
    The TestUrls class has twelve test methods.
    For each URL, we use reverse function to get the URL pattern
    for the named URL, and then use resolve to get the function
    that will handle the request for that URL pattern.
    We then use assertEqual to check if the function returned by resolve
    is the same as the view function defined in the views module.
    These tests will ensure that each URL in the urlpatterns list
    is correctly mapped to the corresponding view function.
    """

    def test_recipes_url_resolves(self):
        url = reverse('recipes')
        self.assertEqual(resolve(url).func, views.recipes)

    def test_recipe_unit_url_resolves(self):
        url = reverse('recipeunit', args=['1'])
        self.assertEqual(resolve(url).func, views.recipeUnit)

    def test_register_url_resolves(self):
        url = reverse('register')
        self.assertEqual(resolve(url).func, views.registerView)

    def test_login_url_resolves(self):
        url = reverse('login')
        self.assertEqual(resolve(url).func, views.loginView)

    def test_logout_url_resolves(self):
        url = reverse('logout')
        self.assertEqual(resolve(url).func, views.logoutView)

    def test_create_recipe_url_resolves(self):
        url = reverse('create-recipe')
        self.assertEqual(resolve(url).func, views.createRecipe)

    def test_update_recipe_url_resolves(self):
        url = reverse('update-recipe', args=['1'])
        self.assertEqual(resolve(url).func, views.updateRecipe)

    def test_delete_recipe_url_resolves(self):
        url = reverse('delete-recipe', args=['1'])
        self.assertEqual(resolve(url).func, views.deleteRecipe)

    def test_about_us_url_resolves(self):
        url = reverse('about-us')
        self.assertEqual(resolve(url).func, views.aboutUs)

    def test_gallery_url_resolves(self):
        url = reverse('gallery')
        self.assertEqual(resolve(url).func, views.gallery)

    def test_like_recipe_url_resolves(self):
        url = reverse('like-recipe', args=['1'])
        self.assertEqual(resolve(url).func, views.likeRecipe)

    def test_contact_url_resolves(self):
        url = reverse('contact')
        self.assertEqual(resolve(url).func, views.contact)
