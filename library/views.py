from django.shortcuts import render
from rest_framework import viewsets, filters
from .models import Book
from .serializers import BookSerializer

class BookView(viewsets.ModelViewSet):
	search_fields = ['name']
	filter_backends = (filters.SearchFilter,)
	queryset = Book.objects.all()
	serializer_class = BookSerializer

# class BookBorrowView(viewsets.ModelViewSet):
# 	queryset = Book.objects.all()
# 	serializer_class = BookSerializer
