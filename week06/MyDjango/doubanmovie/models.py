from django.db import models

# Create your models here.
class Douban1917(models.Model):
    comment = models.TextField(blank=True, null=True)
    vote = models.CharField(max_length=255)
    star = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'douban1917'