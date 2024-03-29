from django.db import models
import uuid
import random
from datetime import datetime

# Create your models here.
class Book(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,help_text="generated unique id for book")
    name=models.CharField(max_length=100, help_text='Book Name',null=True)
    
    purchase_date=models.DateField(null=True,blank=True)
    
    genre=models.ManyToManyField('Genre',help_text='genre of the book')#class name of genre should be mentioned
    book_author=models.ForeignKey('Author',on_delete=models.SET_NULL,help_text='Book Author',null=True)
    timestamp=models.DateTimeField(auto_now=True)
    # class Meta:
    #     db_table='my_books'
    def __str__(self):
        return self.name
    
class Author(models.Model):
    #id=models.AutoField(primary_key=True)
    
    author_name=models.CharField(max_length=100, help_text='Book Name',null=True)
    
    numChoice=(
        ('1','One'),
        ('2','Two'),
        ('3','Three'),
        ('4','Four'),
        ('5','Five')
    )
    place=models.CharField(max_length=100,help_text='place',null=True)
    total_book_written=models.CharField(max_length=1,choices=numChoice,null=True)
    
    date_of_birth=models.DateField('Birth',null=True,blank=True)
    date_of_death=models.DateField('Death',null=True,blank=True)
    def __str__(self):
        return self.author_name

class Genre(models.Model):
    genre_name=models.CharField(max_length=100,help_text='genre',null=True)
    def __str__(self):
        return self.genre_name

class Student(models.Model):
    student_name=models.CharField(max_length=100,help_text='student name',null=True)
    book_took=models.ForeignKey('Book',on_delete=models.SET_NULL,help_text='Book Took',null=True)
    issue_date=models.DateField('Issue',null=True,blank=True)
    senddate = models.DateField('Send after',
		default=datetime.now(),
		blank=True,
		editable=True)
    toaddress = models.EmailField(verbose_name="To (Additional address or addresses)",
		default=None,
		unique=False,
		blank=True,
		null=True,
		max_length=255)
    timestamp=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.student_name