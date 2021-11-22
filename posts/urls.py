from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListCreateView.as_view()),
    path('<int:pk>/', views.PostDetailView.as_view()),
    path('<int:pk>/comment/', views.CommentCreateView.as_view()),
    path('<int:pk>/comment_detail/', views.CommentDetailView.as_view()),
    path('<int:pk>/upvote/', views.upvote),
]
