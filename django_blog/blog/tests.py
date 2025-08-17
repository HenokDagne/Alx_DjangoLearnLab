
from django.test import TestCase, Client
from django.urls import reverse
from .models import User, Post

class BlogPostViewTests(TestCase):
	def setUp(self):
		self.client = Client()
		self.user1 = User.objects.create_user(username='user1', password='pass1')
		self.user2 = User.objects.create_user(username='user2', password='pass2')
		self.post = Post.objects.create(title='Test Post', content='Test Content', author=self.user1)

	def test_post_list_view(self):
		response = self.client.get(reverse('post-list'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Test Post')

	def test_post_detail_view(self):
		response = self.client.get(reverse('post-detail', args=[self.post.pk]))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Test Content')

	def test_create_post_requires_login(self):
		response = self.client.get(reverse('post-create'))
		self.assertNotEqual(response.status_code, 200)
		self.client.login(username='user1', password='pass1')
		response = self.client.get(reverse('post-create'))
		self.assertEqual(response.status_code, 200)

	def test_edit_post_permission(self):
		self.client.login(username='user2', password='pass2')
		response = self.client.get(reverse('post-update', args=[self.post.pk]))
		self.assertEqual(response.status_code, 403)
		self.client.login(username='user1', password='pass1')
		response = self.client.get(reverse('post-update', args=[self.post.pk]))
		self.assertEqual(response.status_code, 200)

	def test_delete_post_permission(self):
		self.client.login(username='user2', password='pass2')
		response = self.client.get(reverse('post-delete', args=[self.post.pk]))
		self.assertEqual(response.status_code, 403)
		self.client.login(username='user1', password='pass1')
		response = self.client.get(reverse('post-delete', args=[self.post.pk]))
		self.assertEqual(response.status_code, 200)

	def test_navigation_links(self):
		response = self.client.get(reverse('post-list'))
		self.assertContains(response, reverse('post-create'))
		self.assertContains(response, reverse('post-detail', args=[self.post.pk]))
