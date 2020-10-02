from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.conf import settings
from taggit.managers import TaggableManager
from django.utils.text import slugify

from registration.models import Profile


class Page(models.Model):
    image = models.ImageField(upload_to='pages')
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, blank=True)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='get_pofiles')
    comment = models.TextField(max_length=3000, null=True, blank=True)
    likes = models.ManyToManyField(User, related_name="likes")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    tags = TaggableManager(blank=True)

    class Meta:
        verbose_name = 'Page'
        verbose_name_plural = 'Pages'
        ordering = ['-created']

    def __str__(self):
        return self.title

    @property
    def total_likes(self):
        return self.likes.count()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self, *args, **kwargs):
        return reverse('pages:page', kwargs={'slug': self.slug, 'pk': self.id})
