from django.test import TestCase
from .models import Category, Image
from datetime import date
from django.core.files.uploadedfile import SimpleUploadedFile

class CategoryModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Test Category')

    def test_category_creation(self):
        self.assertIsInstance(self.category, Category)
        self.assertEqual(self.category.name, 'Test Category')

    def test_category_str_method(self):
        self.assertEqual(str(self.category), 'Test Category')

class ImageModelTest(TestCase):
    def setUp(self):
        self.category1 = Category.objects.create(name='Category 1')
        self.category2 = Category.objects.create(name='Category 2')
        self.image = SimpleUploadedFile(name='test_image.png', content=b'', content_type='image/png')
        self.image_instance = Image.objects.create(
            title='Test Image',
            image=self.image,
            created_date=date.today(),
            age_limit=18
        )
        self.image_instance.categories.set([self.category1, self.category2])

    def test_image_str_method(self):
        self.assertEqual(str(self.image_instance), 'Test Image')

    def test_image_categories(self):
        categories = self.image_instance.categories.all()
        self.assertEqual(categories.count(), 2)
        self.assertIn(self.category1, categories)
        self.assertIn(self.category2, categories)