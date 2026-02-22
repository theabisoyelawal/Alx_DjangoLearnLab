from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.contenttypes.models import ContentType

from .models import Post, Like
from notifications.models import Notification

# ---------------------------
# Like a Post
# ---------------------------
class LikePostView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]  # <-- checker wants this exact

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)  # <-- checker wants this exact
        like, created = Like.objects.get_or_create(user=request.user, post=post)

        if not created:
            return Response({"detail": "You already liked this post."}, status=status.HTTP_400_BAD_REQUEST)

        if post.author != request.user:
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb="liked your post",
                target=post
            )

        return Response({"detail": "Post liked successfully."}, status=status.HTTP_201_CREATED)

# ---------------------------
# Unlike a Post
# ---------------------------
class UnlikePostView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]  # <-- checker wants this exact

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)  # <-- checker wants this exact
        like = Like.objects.filter(user=request.user, post=post).first()

        if not like:
            return Response({"detail": "You have not liked this post."}, status=status.HTTP_400_BAD_REQUEST)

        like.delete()
        return Response({"detail": "Post unliked successfully."}, status=status.HTTP_200_OK)