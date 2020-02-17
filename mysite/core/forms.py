from django import forms

from .models import Book


class BookForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(BookForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Book
        fields = ('description', 'pdf', 'user')
        exclude = ["user"]



