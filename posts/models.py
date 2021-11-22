from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=200)
    link = models.URLField()
    created = models.DateTimeField(auto_now_add=True)
    upvotes = models.ManyToManyField(User, related_name='upvotes')
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='posts')

    def __str__(self):
        return self.title
