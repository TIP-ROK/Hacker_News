from rest_framework import serializers
from .models import Post, Comment


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    post = serializers.StringRelatedField(read_only=True, many=False)

    class Meta:
        model = Comment
        fields = ('id', 'content', 'author', 'post', 'created')


class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    upvotes_count = serializers.ReadOnlyField()
    comments_count = serializers.ReadOnlyField()

    class Meta:
        model = Post
        fields = ('id', 'title', 'link', 'created', 'author', 'upvotes_count', 'comments_count')


class PostDetailSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(read_only=True, many=True)
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'link', 'created', 'author', 'comments',)
