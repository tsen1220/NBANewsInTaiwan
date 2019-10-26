from django.db import models


class NBAnews(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    posttime = models.CharField(max_length=100)

    def __str__(self):
        return self.title
