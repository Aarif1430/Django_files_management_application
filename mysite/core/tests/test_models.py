import pytest
from mixer.backend.django import mixer
from django.test import TestCase, Client
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, Client
from django.urls import reverse_lazy as reverse
from django.utils.six import BytesIO
from mysite.core.models import Book

pytestmark = pytest.mark.django_db


class UserTests(TestCase):
    def setUp(self):
        self.user = Book(username='me')

    # deleting the user will remove the user, the user_profile, AND the avatar image
    def tearDown(self):
        self.user.delete()

    def test_uploading_non_image_file_errors(self):
        # make sure we start out with no UserProfile (and thus no avatar)
        self.assertIsNone(Book.objects.filter(user_id=self.user.id).first())
        myClient = Client()
        myClient.login(username=self.user.username, password='password')

        # set up form data
        text_file = SimpleUploadedFile('front.png', b'this is some text - not an image')
        form_data = {'avatar': text_file}

        response = myClient.post(reverse('avatar_form'), form_data, follow=True)
        self.assertFormError(response, 'avatar_form', 'avatar',
                             'Upload a valid image. The file you uploaded was either not an image or a corrupted image.')