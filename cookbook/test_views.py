from django.test import TestCase, Client
from django.urls import reverse
from unittest.mock import patch
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator
from django.core.files.uploadedfile import SimpleUploadedFile
from .forms import *
from .models import *
from .views import *


class TestRegisterView(TestCase):

    """
    The TestRegisterView class has three test methods: test_register_view, test_register_view_post
    and test_register_view_invalid_post. The setUp method is used to set up the test data.
    In this case, we create a Client object, set up the URLs for the register and login views,
    and create some test data to use in our tests.
    - test_register_view tests that the register view returns a 200 status code and uses the correct template.
    - test_register_view_post tests that the register view correctly creates a new user and logs them in when valid data is submitted via POST request.
    - test_register_view_invalid_post tests that the register view correctly handles invalid data submitted via POST request.
    """

    # Creates the necessary user data to run tests.
    def setUp(self):
        self.client = Client()
        self.register_url = reverse('register')
        self.login_url = reverse('login')
        self.user_data = {
            'username': 'testuser',
            'password1': 'testpassword123',
            'password2': 'testpassword123',
        }
        self.invalid_user_data = {
            'username': 'testuser',
            'password1': 'testpassword123',
            'password2': 'wrongpassword',
        }
        self.form = NewUserForm(data=self.user_data)
        self.invalid_form = NewUserForm(data=self.invalid_user_data)

    # Tests that the register view returns a 200 status code
    # and uses the correct template.
    def test_register_view(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/register.html')

    # Tests that the register view correctly creates a new user
    # and logs them in when valid data is submitted via POST request.
    def test_register_view_post(self):
        response = self.client.post(self.register_url, data=self.user_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('recipes'))
        self.assertEqual(User.objects.count(), 1)
        self.assertTrue(User.objects.filter(username=self.user_data['username']).exists())

    # Tests that the register view correctly handles invalid data
    # submitted via POST request.
    def test_register_view_invalid_post(self):
        response = self.client.post(self.register_url, data=self.invalid_user_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/register.html')
        self.assertFormError(response, 'form', 'password2', 'The two password fields didn’t match.')


class TestLoginView(TestCase):

    """
    The setUp method is used to create a test client, define URLs to test, and create a user for testing.
    The TestLoginView class has three test methods:
    - test_login_successful tests that a user can log in successfully by sending a POST request to the loginView with correct credentials.
    It asserts that the response status code is 302 (redirect), the response redirects to the recipes page, and the _auth_user_id key is in the session.
    - test_login_failure tests that the login fails when incorrect credentials are sent. It asserts that the response status code is 200 (OK),
    the response contains the error message, and the _auth_user_id key is not in the session.
    - test_login_view_uses_correct_template tests that the login view is rendered with the correct template.
    It asserts that the response status code is 200 (OK) and the correct template is used.
    """

    # Creates the necessary user data to run tests.
    def setUp(self):
        self.client = Client()
        self.login_url = reverse('login')
        self.user = User.objects.create_user(username='testuser', password='testpass')

    # Tests that a user can log in successfully by sending a POST request
    # to the loginView with correct credentials.
    def test_login_successful(self):
        response = self.client.post(self.login_url, {'username': 'testuser', 'password': 'testpass'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('recipes'))
        self.assertIn('_auth_user_id', self.client.session)

    # Tests that the login fails when incorrect credentials are sent.
    # It asserts that the response status code is 200 (OK), the response
    # contains the error message, and the _auth_user_id key
    # is not in the session.
    def test_login_failure(self):
        response = self.client.post(self.login_url, {'username': 'testuser', 'password': 'wrongpass'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Username OR password is incorrect')
        self.assertNotIn('_auth_user_id', self.client.session)

    # It asserts that the response status code is 200 (OK) and the
    # the login view is rendered with the correct template.
    def test_login_view_uses_correct_template(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/login.html')


class TestLogoutView(TestCase):

    """
    The setUp method is used to create the data required by the tests. In this case, the test client is created,
    the logout URL is defined, and a test user is created and logged in.
    The TestLogoutView class has one test method:
    - test_logout_successful tests whether the logout view returns a 302 (temporary redirect) status code,
    redirects to the homepage (recipes) and that the _auth_user_id key is not in the session.
    """

    # Creates the necessary user data to run tests.
    def setUp(self):
        self.client = Client()
        self.logout_url = reverse('logout')
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')

    # Tests whether the logout view returns a 302 status code,
    # redirects to the homepage (recipes) and that the _auth_user_id
    # key is not in the session.
    def test_logout_successful(self):
        response = self.client.get(self.logout_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('recipes'))
        self.assertNotIn('_auth_user_id', self.client.session)


class TestRecipesView(TestCase):

    """
    We create three test recipes in the setUp method.
    The TestRecipesView class has two test methods:
    - test_recipes_view_uses_correct_template, tests whether the view is rendering the correct template.
    - test_recipes_view_pagination, tests whether the pagination is working correctly.
    We first test the initial page without any pagination, and then we add more recipes to the database
    to test the pagination functionality.
    """

    # Creates the necessary user and recipe objects to run tests.
    def setUp(self):
        self.client = Client()
        self.login_url = reverse('login')
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.recipe1 = Recipe.objects.create(creator=self.user, title='Recipe 1', short_description='Description 1', ingredients='Ingredients 1', instructions='Instructions 1')
        self.recipe2 = Recipe.objects.create(creator=self.user, title='Recipe 2', short_description='Description 2', ingredients='Ingredients 2', instructions='Instructions 2')
        self.recipe3 = Recipe.objects.create(creator=self.user, title='Recipe 3', short_description='Description 3', ingredients='Ingredients 3', instructions='Instructions 3')
        self.url = reverse('recipes')

    # Tests whether the view is rendering the correct template.
    def test_recipes_view_uses_correct_template(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'index.html')

    # Tests whether the pagination is working correctly.
    def test_recipes_view_pagination(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['recipes_list']), 3)
        self.assertTrue(isinstance(response.context['recipes_list'][0], Recipe))
        self.assertTrue(isinstance(response.context['recipes_list'][1], Recipe))
        self.assertTrue(isinstance(response.context['recipes_list'][2], Recipe))
        self.assertTrue(response.context['recipes_list'].has_previous() is False)
        self.assertTrue(response.context['recipes_list'].has_next() is False)

        # add more recipes
        for i in range(4, 10):
            Recipe.objects.create(title='Recipe %d' % i, short_description='Description %d' % i)

        response = self.client.get(self.url + '?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['recipes_list']), 3)
        self.assertTrue(isinstance(response.context['recipes_list'][0], Recipe))
        self.assertTrue(isinstance(response.context['recipes_list'][1], Recipe))
        self.assertTrue(isinstance(response.context['recipes_list'][2], Recipe))
        self.assertTrue(response.context['recipes_list'].has_previous())
        self.assertTrue(response.context['recipes_list'].has_next())
        self.assertEqual(response.context['recipes_list'].previous_page_number(), 1)
        self.assertEqual(response.context['recipes_list'].next_page_number(), 3)


class TestRecipeUnitView(TestCase):

    """
    We defined the setUp method to create a test user, a test recipe and a test comment in the database before each test is run.
    The TestRecipeUnitView class has two test methods:
    - The test_recipe_unit_view method tests that the recipeUnit view returns a status code of 200,
    it uses the recipe.html template and that the recipe contains all its attributes such as creator, title, etc.
    - The test_add_comment method tests that a comment can be added to the recipe using the CommentForm
    and that the comment is saved in the database.
    """

    # Creates the necessary user, recipe and comment objects to run tests.
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpass'
        )

        self.recipe = Recipe.objects.create(
            creator=self.user,
            title='Test Recipe',
            short_description='This is a test recipe',
            ingredients='Test Ingredients',
            instructions='Test Instructions',
        )

        self.comment = Comment.objects.create(
            recipe=self.recipe,
            name='testuser',
            body='This is a test comment'
        )

        self.client = Client()

    # Tests that the recipe page is displayed correctly, that it uses the
    # correct template and that the recipe contains all the expected
    # attributes.
    def test_recipe_unit_view(self):

        url = reverse('recipeunit', args=[self.recipe.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipe.html')
        self.assertContains(response, self.recipe.creator.username)
        self.assertContains(response, self.recipe.title)
        self.assertContains(response, self.recipe.short_description)
        self.assertContains(response, self.recipe.ingredients)
        self.assertContains(response, self.recipe.instructions)
        self.assertContains(response, self.comment.name)
        self.assertContains(response, self.comment.body)

    # Tests that a comment can be added to the recipe page using the
    # CommentForm and that the comment is saved in the database.
    def test_add_comment(self):

        url = reverse('recipeunit', args=[self.recipe.id])
        self.client.login(username='testuser', password='testpass')

        data = {
            'name': 'Test User',
            'body': 'This is a test comment'
        }

        with patch('django.contrib.messages.success') as mock_message:
            response = self.client.post(url, data=data)

        comment_count = Comment.objects.filter(recipe=self.recipe).count()

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('recipeunit', args=[self.recipe.id]))
        self.assertEqual(comment_count, 2)
        self.assertTrue(mock_message.called)


class TestCreateRecipe(TestCase):

    """
    The setUp method is used to create the data required by the test. In this case,
    the test client and the recipe are created.
    The TestCreateRecipe class has one test method:
    - test_create_recipe_authenticated, tests that a recipe can be created successfully when
    the user is authenticated, it tests that the user is redirected to recipes page after recipe created,
    it tests that the recipe exists, it tests that the recipe creator is set to the authenticated user,
    it tests that the __str__ method of the Recipe model returns the recipe title correctly
    and the tearDown method cleans up the test data after each test.
    """

    # Creates the necessary user and recipe objects to run tests.
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass'
        )
        self.recipe_data = {
            'title': 'Test Recipe',
            'short_description': 'This is a test recipe',
            'image': SimpleUploadedFile("test.jpg", b"file_content", content_type="image/jpeg"),
            'ingredients': 'Test Ingredient 1\nTest Ingredient 2\nTest Ingredient 3',
            'instructions': 'Test Instructions 1\nTest Instructions 2\nTest Instructions 3',
        }

    # Tests that a recipe can be created successfully when the user is authenticated,
    # that the user is redirected to recipes page after recipe created,
    # that the recipe exists, that the recipe creator is set to the authenticated user,
    # and that the __str__ method of the Recipe model returns the recipe title correctly.
    def test_create_recipe_authenticated(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('create-recipe'), data=self.recipe_data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Recipe.objects.filter(title='Test Recipe').exists())
        recipe = Recipe.objects.get(title='Test Recipe')
        self.assertEqual(recipe.creator, self.user)
        self.assertEqual(str(recipe), self.recipe_data.get('title') + ' by ' + self.user.username)

    # Cleans up the test data after each test.
    def tearDown(self):
        self.user.delete()
        Recipe.objects.filter(title='Test Recipe').delete()


class TestUpdateRecipe(TestCase):

    """
    We define a setUp method to create a test user and a test recipe that we can use in our tests.
    The TestUpdateRecipe class has five test methods:
    - test_update_recipe_form_valid tests that the form is valid when given valid data.
    - test_update_recipe_form_invalid tests that the form is invalid when given invalid data.
    - test_update_recipe_view tests that it returns a 200 status code when accessed via GET.
    - test_update_recipe_view_post tests that it redirects to the recipeUnit view with the correct arguments
    when given valid data via POST.
    - test_update_recipe_view_post_invalid tests that it returns a 200 status code when given invalid data via POST.
    """

    # Creates the necessary user and recipe objects to run tests.
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpassword'
        )
        self.recipe = Recipe.objects.create(
            title='Test Recipe',
            short_description='Test Recipe Description',
            creator=self.user,
        )

    # Tests that the form is valid when given valid data.
    def test_update_recipe_form_valid(self):
        self.client.login(username='testuser', password='testpassword')
        data = {
            'title': 'Updated Test Recipe',
            'short_description': 'Updated Test Recipe Description',
            'creator': self.user.id,
            'ingredients': 'Updated Test Recipe Ingredients',
            'instructions': 'Updated Test Recipe Instructions',
        }
        form = RecipeForm(data, instance=self.recipe)
        self.assertTrue(form.is_valid())

    # Tests that the form is invalid when given invalid data.
    def test_update_recipe_form_invalid(self):
        self.client.login(username='testuser', password='testpassword')
        data = {
            'title': '',
            'short_description': '',
            'creator': '',
            'ingredients': '',
            'instructions': '',
        }
        form = RecipeForm(data, instance=self.recipe)
        self.assertFalse(form.is_valid())

    # Tests that it returns a 200 status code when accessed via GET.
    def test_update_recipe_view(self):
        self.client.login(username='testuser', password='testpassword')
        url = reverse('update-recipe', args=[self.recipe.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    # Tests that it redirects to the recipeUnit view with the correct arguments
    # when given valid data via POST.
    def test_update_recipe_view_post(self):
        self.client.login(username='testuser', password='testpassword')
        url = reverse('update-recipe', args=[self.recipe.id])
        data = {
            'title': 'Updated Test Recipe',
            'short_description': 'Updated Test Recipe Description',
            'creator': self.user.id,
            'ingredients': 'Updated Test Recipe Ingredients',
            'instructions': 'Updated Test Recipe Instructions',
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('recipeunit', args=[self.recipe.id]))

    # Tests that it returns a 200 status code when given invalid data via POST.
    def test_update_recipe_view_post_invalid(self):
        self.client.login(username='testuser', password='testpassword')
        url = reverse('update-recipe', args=[self.recipe.id])
        data = {
            'title': '',
            'short_description': '',
            'creator': '',
            'ingredients': '',
            'instructions': '',
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)


class TestDeleteRecipe(TestCase):

    """
    We define a setUp method to create a test user and a test recipe that we can use in our tests.
    The TestDeleteRecipe class has two test methods:
    - test_delete_recipe_view tests that the view can be accessed by a logged-in user with the
    appropriate permissions, that it returns a 200 status code when accessed via GET and
    that the correct template is used for the view.
    - test_delete_recipe_view_post tests whether the delete-recipe view can actually delete the recipe
    when a POST request is made to it, it tests that the response status code is 302, which indicates a successful redirect,
    that goes to the recipes URL, indicating that the recipe was successfully deleted.
    """

    # Creates the necessary user and recipe objects to run tests.
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpassword'
        )
        self.recipe = Recipe.objects.create(
            creator=self.user,
            title='Test Recipe',
            short_description='Updated Test Recipe Description',
            ingredients='Updated Test Recipe Ingredients',
            instructions='Updated Test Recipe Instructions',
        )

    # Tests that the view can be accessed by a logged-in user with the
    # appropriate permissions, that it returns a 200 status code when accessed
    # via GET and that the correct template is used for the view.
    def test_delete_recipe_view(self):
        self.client.login(username='testuser', password='testpassword')
        url = reverse('delete-recipe', args=[self.recipe.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'delete.html')

    # Tests whether the delete-recipe view can actually delete the recipe
    # when a POST request is made to it, it tests that the response
    # status code is 302, which indicates a successful redirect that goes
    # to the recipes URL, indicating that the recipe was successfully deleted.
    def test_delete_recipe_view_post(self):
        self.client.login(username='testuser', password='testpassword')
        url = reverse('delete-recipe', args=[self.recipe.id])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('recipes'))


class TestAboutUs(TestCase):

    """
    The TestAboutUs class has one test method:
    - test_about_us_view tests that it returns a 200 status code when accessed via GET.
    """

    # Tests that it returns a 200 status code when accessed via GET.
    def test_about_us_view(self):
        url = reverse('about-us')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


class TestGallery(TestCase):

    """
    We define a setUp method to create a test user and a test recipe that we can use in our test.
    The TestGallery class has one test method:
    - test_gallery_view tests that it returns a 200 status code when accessed via GET
    and that the view contains the recipe title and default food image.
    """

    # Creates the necessary user and recipe objects to run tests.
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpassword'
        )
        self.recipe = Recipe.objects.create(
            creator=self.user,
            title='Test Recipe',
            short_description='Test Recipe Description',
            ingredients='Test Recipe Ingredients',
            instructions='Test Recipe Instructions',
            food_image='default-image',
        )

    # Tests that it returns a 200 status code when accessed via GET
    # and that the view contains the recipe title and default food image.
    def test_gallery_view(self):
        url = reverse('gallery')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Recipe')
        self.assertContains(response, 'default-image')


class TestLikeRecipe(TestCase):

    """
    We define a setUp method to create a test user and a test recipe that we can use in our test.
    The TestLikeRecipe class has one test method:
    - test_like_recipe tests a POST request to the like-recipe URL with the ID of the test recipe as a parameter.
    We expect the response status code to be 302 (redirect), and the response URL to be the URL of the recipe detail
    page for the test recipe. We also refresh the recipe object from the database and assert that the user's like
    has been added to the recipe. We make sure that it correctly removes a like from the recipe when accessed via POST
    and that it redirects to the recipe detail page. We also refresh the recipe object from the database and assert
    that the user's like has been removed from the recipe.
    """

    # Creates the necessary user and recipe objects to run tests.
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.recipe = Recipe.objects.create(creator=self.user, title='Test Recipe', short_description='Test Description', ingredients='Test Ingredients', instructions='Test Instructions')

    # Tests that a recipe can be liked when a POST request is made to it
    # and that it redirects successfully to recipeunit URL.
    def test_like_recipe(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('like-recipe', args=[self.recipe.id]), {'recipe_id': self.recipe.id})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('recipeunit', args=[self.recipe.id]))

        # Tests that the recipe was liked
        self.recipe.refresh_from_db()
        self.assertTrue(self.recipe.likes.filter(id=self.user.id).exists())

        # Tries to like the recipe again
        response = self.client.post(reverse('like-recipe', args=[self.recipe.id]), {'recipe_id': self.recipe.id})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('recipeunit', args=[self.recipe.id]))

        # Tests that the recipe was unliked
        self.recipe.refresh_from_db()
        self.assertFalse(self.recipe.likes.filter(id=self.user.id).exists())
