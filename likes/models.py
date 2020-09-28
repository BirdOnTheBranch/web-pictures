from django.db import models
from django.contrib.auth.models import User
from pages.models import Page, Profile


# Create your models here.
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    value = models.CharField(max_length=10)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Like'
        verbose_name_plural = 'Likes'
        ordering = ['-created']

    def __str__(self):
        return f'{self.user} ' + f"{self.value}'s " + 'your pic '+f'{self.page}'
