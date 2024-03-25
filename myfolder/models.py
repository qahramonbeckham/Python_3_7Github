from django.db import models


# Create your models here.
class Type(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Portfolio(models.Model):
    name = models.CharField(max_length=30)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    client = models.CharField(max_length=50)
    date = models.DateField()
    url = models.CharField(max_length=100000)
    text = models.TextField()
    picture1 = models.ImageField(upload_to='media')
    picture2 = models.ImageField(upload_to='media', null=True, blank=True)
    picture3 = models.ImageField(upload_to='media', null=True, blank=True)
    picture4 = models.ImageField(upload_to='media', null=True, blank=True)
    picture5 = models.ImageField(upload_to='media', null=True, blank=True)
    picture6 = models.ImageField(upload_to='media', null=True, blank=True)
    picture7 = models.ImageField(upload_to='media', null=True, blank=True)
    picture8 = models.ImageField(upload_to='media', null=True, blank=True)
    picture9 = models.ImageField(upload_to='media', null=True, blank=True)
    picture10 = models.ImageField(upload_to='media', null=True, blank=True)


class Type2(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Services(models.Model):
    name = models.CharField(max_length=30)
    type2 = models.ForeignKey(Type2, on_delete=models.CASCADE)
    text = models.TextField()
    picture1 = models.ImageField(upload_to='media')


class Job(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=30)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    text = models.TextField()
    picture1 = models.ImageField(upload_to='media')


class Contact(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=60)
    subject = models.CharField(max_length=200)
    message = models.TextField()


class Subcribe(models.Model):
    gmail=models.CharField(max_length=100)