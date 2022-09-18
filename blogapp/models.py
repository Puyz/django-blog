from datetime import datetime
from email.mime import image
from email.policy import default
from json import load
from typing_extensions import Required
from django.forms import ImageField
from django.urls import reverse
from turtle import title
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50, null=True)
    slug = models.SlugField(max_length=50, unique=True, null= True)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=50, null=True)
    slug = models.SlugField(max_length=50, unique=True, null= True)

    category = models.ForeignKey(
        Category, 
        on_delete= models.CASCADE,
        verbose_name="Kategori"
    )

    def __str__(self):
        return self.name


class BlogPost(models.Model):
    title = models.CharField(max_length=200, verbose_name="Post başlığı")
    author = models.ForeignKey(
        'auth.User', on_delete= models.CASCADE,
        verbose_name="Yazar"
    )
    body = models.TextField(verbose_name="İçeriği")
    code = models.TextField(verbose_name="Örnek kod", blank=True)
    views = models.IntegerField(default=0, verbose_name="Görüntülenme sayısı")
    imageurl = models.ImageField(upload_to="static/upload/%Y/%m/%d/", verbose_name="Fotoğraf seç", default="static/img/default.png")
    created_datetime = models.DateTimeField(auto_now_add=True, auto_now=False)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, verbose_name="Kategori")
    sub_category = models.ForeignKey(SubCategory, on_delete=models.DO_NOTHING, verbose_name="Alt kategori", null=True)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("home", kwargs={'pk' : self.pk})




class Message(models.Model):
    name = models.CharField(max_length=50, verbose_name="İsim")
    email = models.CharField(max_length=50, verbose_name="Email")
    message = models.TextField(verbose_name="Mesaj")

    def __str__(self):
        return self.name+" : "+self.message
