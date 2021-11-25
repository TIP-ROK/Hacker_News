from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=200)
    link = models.URLField()
    created = models.DateTimeField(auto_now_add=True)
    upvotes = models.ManyToManyField(User, related_name='upvotes')
    upvotes_count = models.PositiveIntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='posts')

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name='comments')
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    score = models.IntegerField(null=True, default=None)

    def __str__(self):
        return f'comment on {self.post.title}'
