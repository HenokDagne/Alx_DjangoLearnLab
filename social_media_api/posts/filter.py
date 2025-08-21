import django_filters
from posts.models import Post, Comment
class PostFilter(django_filters.FilterSet):
    class Meta:
        model = Post
        fields = {
            'title': ['icontains'],
            'content': ['icontains'],
            'created_at': ['gte', 'lte'],
        }
class CommentFilter(django_filters.FilterSet):
    class Meta:
        model = Comment
        fields = {
            'post': ['exact'],
            'author': ['exact'],
            'content': ['icontains'],
            'created_at': ['gte', 'lte'],
        }
