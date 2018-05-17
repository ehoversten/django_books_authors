from django.db import models

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    notes = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return "<Author object: {}| first:{} last:{} email:{} notes:{}>".format(self.id, self.first_name, self.last_name, self.email, self.notes)


class Book(models.Model):
    name = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    author = models.ManyToManyField(Author, related_name='books')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return "<Book object: {}| name:{} desc:{} >".format(self.id, self.name, self.desc)
