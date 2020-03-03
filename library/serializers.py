from rest_framework import serializers
from .models import Book
# , Borrower

class BookSerializer(serializers.ModelSerializer):
	class Meta:
		model = Book
		fields = ('id', 'name', 'isbn', 'author')


# class BorrowerSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = Borrower
# 		fields = ('username', 'first_name', 'last_name')