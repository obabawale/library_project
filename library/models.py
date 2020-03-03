from django.db import models

class Book(models.Model):
	name = models.CharField(max_length=32)
	isbn = models.CharField(max_length=12)
	author = models.CharField(max_length=32)
	# lender = models.ForeignKey('Borrower', on_delete=models.CASCADE)

	def __str__(self):
		return self.name


# class Borrower(models.Model):
	# user = models.OneToOneField('User', on_delete=models.CASCADE)