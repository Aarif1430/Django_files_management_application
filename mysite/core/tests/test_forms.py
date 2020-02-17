import pytest
from mixer.backend.django import mixer
from mysite.core.forms import BookForm
import snakeviz
pytestmark = pytest.mark.django_db


class TestMyModelForm:
    def test_mymodelform(self):
        form = BookForm()
        assert False is form.is_valid()

        data = {"name": "Hans"}
        form = BookForm(data=data)
        assert False is form.is_valid()
        assert form.errors
        assert "other_model" in form.errors, "other_model cant be null"

        form = BookForm(data=data)
        assert True is form.is_valid()
        assert not form.errors, "Should be no errors, when form is valid"


