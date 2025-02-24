from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RegisterSerializer
from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

User = get_user_model()

class RegisterView(APIView):
    permission_classes = [AllowAny]  # No authentication required
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"message": "User registered successfully!", "email": user.email}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PublicView(APIView):
    """
    This view is accessible to everyone.
    """
    permission_classes = [AllowAny]  # No authentication required

    def get(self, request):
        return Response({"message": "This is an unprotected view. Anyone can access this!"})


class ProtectedView(APIView):
    """
    This view is only accessible to authenticated users.
    """
    authentication_classes = [JWTAuthentication]  # Requires JWT token
    permission_classes = [IsAuthenticated]  # Only authenticated users can access

    def get(self, request):
        return Response({"message": f"Hello {request.user.email}, you have accessed a protected view!"})