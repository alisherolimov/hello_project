from django.db import models

class Banner(models.Model):
    img = models.ImageField(upload_to='banner/')
    title = models.CharField(max_length=255)
    text = models.TextField()

    def __str__(self):
        return self.title


class About(models.Model):
    img = models.ImageField(upload_to='about/')
    title = models.CharField(max_length=255)
    text = models.TextField()

    def __str__(self):
        return self.title


class Blog(models.Model):
    img = models.ImageField(upload_to='blog/')


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.name