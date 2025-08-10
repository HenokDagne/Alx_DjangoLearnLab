

# ---------------------------------------------
# Testing Strategy for Book API Endpoints
# ---------------------------------------------
#
# This test suite uses Django's built-in test framework (unittest-based)
# and Django REST Framework's APITestCase to simulate API requests.
#
# Key areas tested:
# - CRUD operations for Book endpoints (create, update, delete, list)
# - Filtering, searching, and ordering (add tests as needed)
# - Permissions and authentication enforcement
#
# How to run tests:
# 1. Open a terminal in your project directory.
# 2. Run: python manage.py test
# 3. Django will use a separate test database and show results for each test case.
#
# Interpreting results:
# - Each test method checks status codes and response data for correctness.
# - Failures will show the expected vs. actual result for easy debugging.
# - All tests should pass for a healthy API implementation.
# ---------------------------------------------

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from .models import Book, Author

class BookAPITestCase(APITestCase):
	"""
	Test CRUD operations, filtering, searching, ordering, and permissions for Book API endpoints.
	Uses Django's test database, so production data is not affected.
	"""
	def setUp(self):
		# Create test user and author
		self.user = get_user_model().objects.create_user(username='testuser', password='testpass')
		self.author = Author.objects.create(name='Author One')
		self.book1 = Book.objects.create(title='Book One', publication_year=2020, author=self.author)
		self.book2 = Book.objects.create(title='Book Two', publication_year=2021, author=self.author)

	def test_create_book(self):
		self.client.login(username='testuser', password='testpass')
		url = reverse('book-create')
		data = {
			'title': 'Book Three',
			'publication_year': 2022,
			'author': self.author.id
		}
		response = self.client.post(url, data)
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		self.assertEqual(response.data['title'], 'Book Three')
		self.assertEqual(response.data['publication_year'], 2022)

	def test_update_book(self):
		self.client.login(username='testuser', password='testpass')
		url = reverse('book-update', args=[self.book1.id])
		data = {
			'title': 'Book One Updated',
			'publication_year': 2020,
			'author': self.author.id
		}
		response = self.client.put(url, data)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.book1.refresh_from_db()
		self.assertEqual(self.book1.title, 'Book One Updated')

	def test_delete_book(self):
		self.client.login(username='testuser', password='testpass')
		url = reverse('book-delete', args=[self.book2.id])
		response = self.client.delete(url)
		self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
		self.assertFalse(Book.objects.filter(id=self.book2.id).exists())

	def test_permission_required_for_create(self):
		url = reverse('book-create')
		data = {
			'title': 'Book Four',
			'publication_year': 2023,
			'author': self.author.id
		}
		response = self.client.post(url, data)
		self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

	# Example test: List books
	def test_list_books(self):
		url = reverse('book-list')
		response = self.client.get(url)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(len(response.data), 2)

	# More tests for CRUD, filtering, searching, ordering, and permissions will be added here
