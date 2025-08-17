
from django.test import TestCase, Client
from django.urls import reverse
from .models import User, Post, Comment

class BlogPostViewTests(TestCase):
	def setUp(self):
		self.client = Client()
		self.user1 = User.objects.create_user(username='user1', password='pass1')
		self.user2 = User.objects.create_user(username='user2', password='pass2')
		self.post = Post.objects.create(title='Test Post', content='Test Content', author=self.user1)
		self.comment = Comment.objects.create(post=self.post, author=self.user1, content='Test Comment')

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


	def test_comment_creation_requires_login(self):
		response = self.client.post(reverse('post-detail', args=[self.post.pk]), {'content': 'New Comment'})
		self.assertNotEqual(response.status_code, 302)  # Should not redirect for anonymous
		self.client.login(username='user1', password='pass1')
		response = self.client.post(reverse('post-detail', args=[self.post.pk]), {'content': 'New Comment'})
		self.assertEqual(response.status_code, 302)  # Should redirect after comment
		self.assertTrue(Comment.objects.filter(content='New Comment').exists())

	def test_comment_edit_permission(self):
		self.client.login(username='user2', password='pass2')
		response = self.client.get(reverse('comment-update', args=[self.post.pk, self.comment.pk]))
		self.assertEqual(response.status_code, 403)
		self.client.login(username='user1', password='pass1')
		response = self.client.get(reverse('comment-update', args=[self.post.pk, self.comment.pk]))
		self.assertEqual(response.status_code, 200)

	def test_comment_delete_permission(self):
		self.client.login(username='user2', password='pass2')
		response = self.client.get(reverse('comment-delete', args=[self.post.pk, self.comment.pk]))
		self.assertEqual(response.status_code, 403)
		self.client.login(username='user1', password='pass1')
		response = self.client.get(reverse('comment-delete', args=[self.post.pk, self.comment.pk]))
		self.assertEqual(response.status_code, 200)

	def test_comment_displayed_on_post_detail(self):
		response = self.client.get(reverse('post-detail', args=[self.post.pk]))
		self.assertContains(response, 'Test Comment')
