from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import Book
from django.utils import timezone

class BookModelTest(TestCase):

    def setUp(self):
        # Crear un libro para las pruebas
        self.book = Book.objects.create(
            title='Django Testing',
            description='A book about Django testing'
        )

    def test_book_creation(self):
        """Prueba que un libro se crea correctamente."""
        self.assertEqual(self.book.title, 'Django Testing')
        self.assertEqual(self.book.description, 'A book about Django testing')
        self.assertIsNotNone(self.book.created_at)
        self.assertIsNotNone(self.book.updated_at)

    def test_book_str_method(self):
        """Prueba el método __str__ del modelo Book."""
        self.assertEqual(str(self.book), 'Django Testing')

    def test_book_update(self):
        """Prueba que la fecha de actualización se actualiza correctamente."""
        original_updated_at = self.book.updated_at
        # Simular una actualización después de un segundo
        self.book.save()
        self.assertGreater(self.book.updated_at, original_updated_at)

    def test_book_query(self):
        """Prueba la consulta del libro por título."""
        queried_book = Book.objects.get(title='Django Testing')
        self.assertEqual(queried_book, self.book)

    def test_book_query_nonexistent(self):
        """Prueba la consulta de un libro que no existe."""
        with self.assertRaises(Book.DoesNotExist):
            Book.objects.get(title='Nonexistent Book')
