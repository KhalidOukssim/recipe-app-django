from django.contrib.auth import get_user_model
from django.test import TestCase


class ModelTests(TestCase):

    def test_create_user_with_eamil(self):
        """Test creating a new user with email is successful"""
        email = 'test@gmail.com'
        password = '1234567890'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        email = 'test@Gmail.com'
        user = get_user_model().objects.create_user(email, 'khalid123')

        self.assertEqual(user.email,email.lower())
