from rest_framework import serializers
from .models import Post, Comment
from django.db.models import Avg


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    post = serializers.StringRelatedField(read_only=True, many=False)

    class Meta:
        model = Comment
        fields = ('id', 'content', 'author', 'post', 'created')


class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    upvotes_count = serializers.ReadOnlyField()
    comments_count = serializers.IntegerField(read_only=True)
    likes = serializers.IntegerField(read_only=True)
    average_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'link', 'created', 'author', 'upvotes_count', 'comments_count', 'likes',
                  'average_count')

    def to_representation(self, instance):
        response = super().to_representation(instance)
        post = Post.objects.get(id=instance.id)
        response['comments_count'] = post.comments.count()
        response['likes'] = post.upvotes.count()
        average = post.comments.all().aggregate(Avg('score'))
        response['average_count'] = average['score__avg']
        return response


class PostDetailSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(read_only=True, many=True)
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'link', 'created', 'author', 'comments',)
