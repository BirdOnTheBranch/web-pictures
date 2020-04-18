from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categorys'
        ordering =  ['-created']
        
    def __str__(self):
        return self.name



class Page(models.Model):
    image = models.ImageField(upload_to='pages')
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(max_length=300, null=True, blank=True)
    categories = models.ManyToManyField(Category)
    created = models.DateTimeField( auto_now_add=True)
    updated = models.DateTimeField( auto_now=True)
    
    class Meta:
        verbose_name = 'Page'
        verbose_name_plural = 'Pages'
        ordering =  ['-created']
    
    def __str__(self):
        return self.title 
