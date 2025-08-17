
from django.test import TestCase, Client
from django.urls import reverse
from .models import User, Post, Comment

from .models import Tag

class BlogPostViewTests(TestCase):
	def setUp(self):
		self.client = Client()
		self.user1 = User.objects.create_user(username='user1', password='pass1')
		self.user2 = User.objects.create_user(username='user2', password='pass2')
		self.tag1 = Tag.objects.create(name='django')
		self.tag2 = Tag.objects.create(name='blog')
		self.post = Post.objects.create(title='Test Post', content='Test Content', author=self.user1)
		self.post.tags.add(self.tag1, self.tag2)
		self.comment = Comment.objects.create(post=self.post, author=self.user1, content='Test Comment')
	def test_post_tags_displayed(self):
		response = self.client.get(reverse('post-detail', args=[self.post.pk]))
		self.assertContains(response, 'django')
		self.assertContains(response, 'blog')

	def test_create_post_with_tags(self):
		self.client.login(username='user1', password='pass1')
		response = self.client.post(reverse('post-create'), {
			'title': 'Tagged Post',
			'content': 'Content with tags',
			'tags': 'python, web'
		})
		self.assertEqual(response.status_code, 302)
		post = Post.objects.get(title='Tagged Post')
		self.assertTrue(post.tags.filter(name='python').exists())
		self.assertTrue(post.tags.filter(name='web').exists())

	def test_edit_post_tags(self):
		self.client.login(username='user1', password='pass1')
		response = self.client.post(reverse('post-update', args=[self.post.pk]), {
			'title': self.post.title,
			'content': self.post.content,
			'tags': 'django, updated'
		})
		self.assertEqual(response.status_code, 302)
		self.post.refresh_from_db()
		self.assertTrue(self.post.tags.filter(name='updated').exists())

	def test_search_by_title(self):
		response = self.client.get(reverse('post-search') + '?q=Test')
		self.assertContains(response, 'Test Post')

	def test_search_by_content(self):
		response = self.client.get(reverse('post-search') + '?q=Content')
		self.assertContains(response, 'Test Post')

	def test_search_by_tag(self):
		response = self.client.get(reverse('post-search') + '?q=django')
		self.assertContains(response, 'Test Post')

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
