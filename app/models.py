from django.db import models

# Create your models here.


class DouBanBook(models.Model):
    name = models.CharField(max_length=256)
    pub = models.CharField(max_length=256)
    desc = models.TextField()
    star = models.FloatField()
    category = models.CharField(max_length=256)

    class Meta:
        indexes = [
            models.Index(fields=['name']),
        ]
        ordering = ['-id']