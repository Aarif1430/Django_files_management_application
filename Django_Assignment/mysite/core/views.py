from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView
from django.urls import reverse_lazy
from django.views import generic
from .models import User

from .forms import BookForm
from .models import Book
from rest_framework.views import APIView
from rest_framework.response import Response
from .document_serializer import DocumentSerializer


class Home(TemplateView):
    template_name = 'home.html'


def book_list(request):
    books = Book.objects.all()
    books = Book.objects.filter(user=request.user)
    return render(request, 'book_list.html', {
        'books': books
    })


def upload_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = User.objects.get(username=request.user)
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'upload_book.html', {
        'form': form
    })


def delete_book(request, pk):
    if request.method == 'POST':
        book = Book.objects.get(pk=pk)
        book.delete()
    return redirect('book_list')

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class BookListView(ListView):
    model = Book
    template_name = 'class_book_list.html'
    context_object_name = 'books'


class UploadBookView(CreateView):
    model = Book
    form_class = BookForm
    success_url = reverse_lazy('class_book_list')
    template_name = 'upload_book.html'


class DocumentList(APIView):
    def get(self, request):
        documents = Book.objects.all()
        serializer = DocumentSerializer(documents, many=True)
        return Response({'documents': serializer.data})

    def post(self, request):
        serializer = DocumentSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            document_saved = serializer.save()
        return Response({"success": "Document '{}' created successfully".format(document_saved)})
