from django.test import TestCase
from tinymce.widgets import TinyMCE
from django.forms.fields import MultipleChoiceField
from django.forms.widgets import CheckboxSelectMultiple
from django.contrib.auth.models import User
from .models import Recipe, Comment
from .forms import RecipeForm, NewUserForm, CommentForm


class TestRecipeForm(TestCase):

    """
    The TestRecipeForm class has two test methods: test_tags_field and test_meta_model.
    - The test_tags_field method tests that the tags field is an instance of MultipleChoiceField,
    has required attribute set to False, has the expected choices and widget.
    - The test_meta_model method tests that the Meta attributes are set as expected.
    """
    # Tests if the tags field is an instance of MultipleChoiceField, the required attribute set to False,
    # and that the tags field has the correct choices and widget.
    def test_tags_field(self):
        form = RecipeForm()
        self.assertIsInstance(form.fields['tags'], MultipleChoiceField)
        self.assertEqual(form.fields['tags'].required, False)
        self.assertEqual(form.fields['tags'].choices, [('Breakfast', 'Breakfast'), ('Lunch', 'Lunch'), ('Dinner', 'Dinner'), ('Supper', 'Supper'), ('Dessert', 'Dessert'), ('Drink', 'Drink')])
        self.assertIsInstance(form.fields['tags'].widget, CheckboxSelectMultiple)

    # Tests that the meta model has the attributes set as expected.
    def test_meta_model(self):
        form = RecipeForm()
        self.assertEqual(form.Meta.model, Recipe)
        self.assertEqual(form.Meta.fields, ['title', 'short_description', 'ingredients', 'instructions', 'tags', 'food_image'])


class TestNewUserForm(TestCase):

    """
    The TestNewUserForm class has only one test method,
    which tests that the Meta attributes are set as expected.
    """

    # Tests that the meta model has the attributes set as expected.
    def test_meta_model(self):
        form = NewUserForm()
        self.assertEqual(form.Meta.model, User)
        self.assertEqual(form.Meta.fields, ['username', 'email', 'password1', 'password2'])


class TestCommentForm(TestCase):

    """
    The TestCommentForm class has only one test method,
    which tests that the Meta attributes are set as expected.
    """

    # Tests that the meta model has the attributes set as expected.
    def test_meta_model(self):
        form = CommentForm()
        self.assertEqual(form.Meta.model, Comment)
        self.assertEqual(form.Meta.fields, ['body'])


if __name__ == '__main__':
    unittest.main()
