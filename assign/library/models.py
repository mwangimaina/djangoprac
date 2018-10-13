from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.db.models import Manager


class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()

    def __str__(self):
        return '%s %s' %(self.first_name, self.last_name)


class Book(models.Model):
    title = models.CharField(max_length=100)
    authors: Manager = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher,  on_delete=models.CASCADE)
    publication_date = models.DateField()
    user = models.OneToOneField(User, blank=True, null=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

# TODO :  Update, delete Author, Books
# Do A Student Model  - CRUD

