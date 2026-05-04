from django.test import TestCase
from catalog.models import Category


class ModelTest(TestCase):

    def test_category(self):
        c = Category.objects.create(name="Test")
        self.assertEqual(str(c), "Test")