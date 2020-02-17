from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    description = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='books/pdfs/')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.description

    def delete(self, *args, **kwargs):
        self.pdf.delete()
        super().delete(*args, **kwargs)

