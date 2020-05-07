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
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    comment = models.TextField(max_length=3000, null=True, blank=True)
    liked = models.ManyToManyField(User, blank=True, default=None, related_name='liked')
    categories = models.ManyToManyField(Category, blank=True, related_name='get_page')
    created = models.DateTimeField( auto_now_add=True)
    updated = models.DateTimeField( auto_now=True)
    
    class Meta:
        verbose_name = 'Page'
        verbose_name_plural = 'Pages'
        ordering =  ['-created']
    
    def __str__(self):
        return self.title

    @property
    def run_likes(self):
        return self.liked.all().count()


LIKE_CHOICES = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike'),
)


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, default='Like', max_length=10)
