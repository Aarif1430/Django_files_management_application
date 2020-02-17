import pytest
from django.contrib.auth.models import AnonymousUser, User
from django.test import RequestFactory
from django.urls import reverse
from mixer.backend.django import mixer

from mysite.core import views
from mysite.core.forms import BookForm
from mysite.core.models import Book

pytestmark = pytest.mark.django_db


class TestMyView:
    def test_anonymous(self):
        req = RequestFactory().get(reverse("myapp:myview"))
        resp = views.Home.as_view()(req)
        assert resp.status_code == 200


class TestMyCreateView:
    def test_authentication(self):
        req = RequestFactory().get(reverse("myapp:mycreateview"))
        # req.user = AnonymousUser()
        resp = views.Home.as_view()(req)
        assert resp.status_code == 200, "Everyone can create a MyModel"

    def test_post(self):
        assert False is Book.objects.all().exists()
        data = {
            "name": "Hans",
            "other_model": mixer.blend("myapp.MyOtherModel").pk
        }
        req = RequestFactory().post(reverse("myapp:mycreateview"), data=data)
        resp = views.Home.as_view()(req)
        assert resp.status_code == 302, "Should redirect to success url"
        assert resp.url == "/create_success/"
        assert Book.objects.all().exists()
        assert Book.objects.all()[0].name == "Hans"