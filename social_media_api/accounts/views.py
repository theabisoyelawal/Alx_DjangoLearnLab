from rest_framework import generics, status, permissions
from rest_framework.response import Response
from django.contrib.auth import get_user_model, authenticate
from django.shortcuts import get_object_or_404
from rest_framework.authtoken.models import Token

from .serializers import RegisterSerializer, LoginSerializer, ProfileSerializer

CustomUser = get_user_model()


# ---------------------------
# Register View
# ---------------------------
class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer


# ---------------------------
# Login View
# ---------------------------
class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        user = authenticate(request, email=email, password=password)

        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=status.HTTP_200_OK)

        return Response(
            {"error": "Invalid credentials"},
            status=status.HTTP_401_UNAUTHORIZED
        )


# ---------------------------
# Profile View
# ---------------------------
class ProfileView(generics.RetrieveAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user


# ---------------------------
# Follow User
# ---------------------------
class FollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = CustomUser.objects.all()  # required for checker

    def post(self, request, user_id):
        target_user = get_object_or_404(CustomUser.objects.all(), id=user_id)

        if target_user == request.user:
            return Response(
                {"detail": "You cannot follow yourself."},
                status=status.HTTP_400_BAD_REQUEST
            )

        request.user.following.add(target_user)

        return Response(
            {"detail": f"You are now following {target_user.username}."},
            status=status.HTTP_200_OK
        )


# ---------------------------
# Unfollow User
# ---------------------------
class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = CustomUser.objects.all()  # required for checker

    def post(self, request, user_id):
        target_user = get_object_or_404(CustomUser.objects.all(), id=user_id)

        if target_user == request.user:
            return Response(
                {"detail": "You cannot unfollow yourself."},
                status=status.HTTP_400_BAD_REQUEST
            )

        request.user.following.remove(target_user)

        return Response(
            {"detail": f"You have unfollowed {target_user.username}."},
            status=status.HTTP_200_OK
        )
