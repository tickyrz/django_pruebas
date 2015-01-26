from django.db import models

# Create your models here.
class Publisher(models.Model):
	name = models.CharField(max_length=30)
	address = models.CharField(max_length=50)
	city = models.CharField(max_length=60)
	state_province = models.CharField(max_length=30)
	country = models.CharField(max_length=50)
	website = models.URLField(max_length=50)

	def __str__(self): #Representacion de texto para name
		return self.name

	class Meta:
		ordering = ["name"] #Ordenamiento por name

	#class Admin:
	#	pass

class Author(models.Model):
	salutation = models.CharField(max_length=10)
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=40)
	email = models.EmailField(max_length=50)
	#headshot = models.FileField(upload_to='/tmp') c

	def __str__(self):
		return '%s %s' % (self.first_name, self.last_name)

	#class Admin:
	#	pass

class Book(models.Model):
	title = models.CharField(max_length=100)
	authors = models.ManyToManyField(Author)
	publisher = models.ForeignKey(Publisher)
	publication_date = models.DateField()

	def __str__(self):
		return self.title

	#class Admin:
	#	fields = ('title', 'publisher', 'publication_date')
    #    list_filter = ('publisher', 'publication_date')
    #    ordening = ('-publication_date',)
    #    search_fields = ('title',)
