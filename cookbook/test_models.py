from django.test import TestCase
from django.contrib.auth.models import User
from .models import *
from django.utils import timezone


class TestRecipeModel(TestCase):

    """
    The setUp method is used to create a User object and a Recipe object.
    The TestRecipeModel class has three test methods: test_recipe_creation,
    test_recipe_tags, and test_recipe_likes.
    - In test_recipe_creation, we check if a Recipe object
    is created correctly and if all its fields are correctly saved.
    - In test_recipe_tags, we test if we can set and retrieve
    the tags for a Recipe.
    - In test_recipe_likes, we test if we can add likes to a Recipe,
    retrieve the number of likes, and check if a user is in the likes queryset.
    """

    # Creates the necessary user and recipe objects to run tests.
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass'
        )
        self.recipe = Recipe.objects.create(
            creator=self.user,
            title='Test Recipe',
            short_description='This is a test recipe',
            ingredients='Test ingredient 1, Test ingredient 2',
            instructions='<p>Test instruction</p>'
        )

    # Checks if a Recipe object is created correctly and if all its fields
    # are correctly saved.
    def test_recipe_creation(self):
        self.assertEqual(str(self.recipe), 'Test Recipe by testuser')
        self.assertEqual(self.recipe.creator, self.user)
        self.assertEqual(
            self.recipe.short_description, 'This is a test recipe'
            )
        self.assertEqual(
            self.recipe.ingredients, 'Test ingredient 1, Test ingredient 2'
            )
        self.assertEqual(self.recipe.instructions, '<p>Test instruction</p>')
        self.assertEqual(self.recipe.tags, None)
        self.assertEqual(self.recipe.total_likes(), 0)

    # Tests if we can set and retrieve the tags for a Recipe.
    def test_recipe_tags(self):
        self.recipe.tags = ['Breakfast', 'Lunch']
        self.recipe.save()
        self.assertEqual(self.recipe.tags, ['Breakfast', 'Lunch'])

    # Tests if we can add likes to a Recipe, retrieve the number of likes,
    # and checks if a user is in the likes queryset.
    def test_recipe_likes(self):
        user1 = User.objects.create_user(
            username='testuser1',
            password='testpass1'
        )
        user2 = User.objects.create_user(
            username='testuser2',
            password='testpass2'
        )
        self.recipe.likes.add(user1)
        self.recipe.likes.add(user2)
        self.assertEqual(self.recipe.total_likes(), 2)
        self.assertTrue(user1 in self.recipe.likes.all())
        self.assertTrue(user2 in self.recipe.likes.all())


class TestCommentModel(TestCase):

    """
    The TestCommentModel class has two test methods: test_comment_name
    and test_comment_ordering.
    The setUpTestData class method is used to set up the test data.
    In this case, we create a User object and a Recipe object,
    and then create a Comment object that is associated with the Recipe object.
    - test_comment_name tests that the __str__ method
    of the Comment model returns the expected string.
    - test_comment_ordering tests that the Meta.ordering attribute
    of the Comment model is working correctly by creating a second
    Comment object and checking that the two objects are ordered correctly
    when retrieved from the database.
    """

    @classmethod
    # Set up non-modified objects used by all test methods
    def setUpTestData(cls):
        user = User.objects.create_user(username='testuser', password='12345')
        recipe = Recipe.objects.create(title='Test Recipe', creator=user)

        Comment.objects.create(
            recipe=recipe,
            name='testuser',
            body='Test body',
            created=timezone.now(),
            updated=timezone.now(),
        )

    # Tests that the __str__ method of the Comment model
    # returns the expected string.
    def test_comment_name(self):
        comment = Comment.objects.get(id=1)
        expected_name = (
            f'Comment made by {comment.name} on {comment.recipe.title}'
            )
        self.assertEqual(expected_name, str(comment))

    # Tests that the Meta.ordering attribute of the Comment model
    # is working correctly by creating a second Comment object
    # and checking that the two objects are ordered correctly
    # when retrieved from the database.
    def test_comment_ordering(self):
        comment1 = Comment.objects.get(id=1)
        comment2 = Comment.objects.create(
            recipe=comment1.recipe,
            name='Test Name 2',
            body='Test body 2',
            created=timezone.now(),
            updated=timezone.now(),
        )
        comments = Comment.objects.all()
        self.assertEqual(comments.count(), 2)
        self.assertEqual(comments[0], comment1)
        self.assertEqual(comments[1], comment2)
