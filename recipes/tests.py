from django.test import TestCase
from .models import Recipe

# Create your tests here.
class RecipeTest(TestCase):
    def setup(cls):
        recipe = Recipe.objects.create(
            id=1 ,   
            title='Test Title',
            author='Nadia', 
            context='This is just a test.'
            )

    def tests_views_index(self):
        recipe = Recipe.objects.get(id=1)
        self.assertEqual(recipe.title, 'Test Title')
        self.assertEqual(recipe.author, 'Nadia')
