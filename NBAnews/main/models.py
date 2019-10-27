from django.db import models

# Create your models here.


class news(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    time = models.CharField(max_length=30)

    def __str__(self):
        return self.title
