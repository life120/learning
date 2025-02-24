from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
import logging
logger = logging.getLogger('test')

User = get_user_model()

class UserAuthTests(TestCase):

    def setUp(self):
        """
        Create a test user before running tests.
        """
        self.test_user = User.objects.create_user(
            email="testuser@example.com",
            password="StrongPass123",
            first_name="John",
            last_name="Doe"
        )
        self.register_url = reverse("accounts:register")
        self.login_url = reverse("accounts:token_obtain_pair")
        self.sample_protected_url = reverse('accounts:protected-view')

    def test_register_successful(self):
        """
        Ensure a new user can register successfully.
        """
        data = {
            "email": "newuser@example.com",
            "first_name": "Alice",
            "last_name": "Smith",
            "password": "SecurePass456"
        }
        response = self.client.post(self.register_url, data)
        print(response.status_code)
        print(response.json())
        self.assertEqual(response.status_code, 201)
        self.assertIn("message", response.json())
        self.assertEqual(response.json()["message"], "User registered successfully!")

        # Verify that the user was created in the database
        self.assertTrue(User.objects.filter(email="newuser@example.com").exists())

    def test_register_existing_email(self):
        """
        Ensure registration fails if the email is already in use.
        """
        data = {
            "email": "testuser@example.com",  # This email is already used
            "first_name": "Duplicate",
            "last_name": "User",
            "password": "AnotherPass123"
        }
        response = self.client.post(self.register_url, data)

        self.assertEqual(response.status_code, 400)
        self.assertIn("email", response.json())  # Ensure error response includes email field

    def test_register_invalid_email(self):
        """
        Ensure registration fails if the email format is invalid.
        """
        data = {
            "email": "invalidemail",  # Invalid email format
            "first_name": "Invalid",
            "last_name": "Email",
            "password": "Pass1234"
        }
        response = self.client.post(self.register_url, data)

        self.assertEqual(response.status_code, 400)
        self.assertIn("email", response.json())

    def test_register_weak_password(self):
        """
        Ensure registration fails if the password is too short.
        """
        data = {
            "email": "weakpass@example.com",
            "first_name": "Weak",
            "last_name": "Password",
            "password": "123"  # Too short
        }
        response = self.client.post(self.register_url, data)

        self.assertEqual(response.status_code, 400)
        self.assertIn("password", response.json())

    def test_login_successful(self):
        """
        Ensure a user can log in successfully and receive JWT tokens.
        """
        data = {
            "email": "testuser@example.com",
            "password": "StrongPass123"
        }
        response = self.client.post(self.login_url, data)

        self.assertEqual(response.status_code, 200)
        self.assertIn("access", response.json())
        self.assertIn("refresh", response.json())

    def test_login_wrong_password(self):
        """
        Ensure login fails with incorrect password.
        """
        data = {
            "email": "testuser@example.com",
            "password": "WrongPassword123"
        }
        response = self.client.post(self.login_url, data)

        self.assertEqual(response.status_code, 401)
        self.assertIn("detail", response.json())

    def test_login_non_existent_user(self):
        """
        Ensure login fails for a non-existent user.
        """
        data = {
            "email": "nouser@example.com",
            "password": "DoesNotExist123"
        }
        response = self.client.post(self.login_url, data)

        self.assertEqual(response.status_code, 401)
        self.assertIn("detail", response.json())

    def test_access_protected_view_with_token(self):
        """
        Ensure authenticated users can access protected views.
        """
        # Generate the access token for the test user
        refresh = RefreshToken.for_user(self.test_user)
        access_token = str(refresh.access_token)

        response = self.client.get(
            self.sample_protected_url, 
            HTTP_AUTHORIZATION=f"Bearer {access_token}"
        )
        
        self.assertEqual(response.status_code, 200)
        self.assertIn("message", response.json())

    def test_access_protected_view_without_token(self):
        """
        Ensure unauthorized users cannot access protected views.
        """
        response = self.client.get(self.sample_protected_url)
        
        self.assertEqual(response.status_code, 401)
        self.assertIn("detail", response.json())
