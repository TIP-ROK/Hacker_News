from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Post, Comment
from .permissions import IsOwnerOrReadOnly
from .serializer import PostSerializer, CommentSerializer, PostDetailSerializer


class PostListCreateView(generics.ListCreateAPIView):
    """
        This API endpoint allows to get list of post and create post
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class CommentCreateView(generics.CreateAPIView):
    """
        This API endpoint allows to get list of comment and create comment
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        post = Post.objects.get(pk=self.kwargs['pk'])
        serializer.save(author=self.request.user, post=post)


class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


@csrf_exempt
@api_view(['POST'])
def upvote(request, pk):
    post = Post.objects.get(pk=pk)
    if request.user in post.upvotes.all():
        post.upvotes.remove(request.user)
        post.upvotes_count -= 1
        return Response(data={'message': f'{request.user.username}'}, status=status.HTTP_201_CREATED)
    else:
        post.upvotes.add(request.user)
        post.upvotes_count += 1
        return Response(data={'message': ''}, status=status.HTTP_202_ACCEPTED)
