from django.db.models.signals import m2m_changed, post_save
from django.dispatch import receiver

from .models import Post, Comment


@receiver(m2m_changed, sender=Post.upvotes.through)
def post_upvotes_changed(sender, instance, **kwargs):
    instance.upvotes_count = instance.upvotes.count()
    instance.save()
