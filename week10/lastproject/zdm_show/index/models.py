from django.db import models

# Create your models here.
class CommentItem(models.Model):
    comment_id = models.IntegerField(primary_key=True)
    comment_rank = models.IntegerField()
    comment_href = models.CharField(max_length=200)
    comment_title = models.CharField(max_length=100)
    comment_cotents = models.TextField()
    comment_sen = models.FloatField()
    create_time = models.TimeField(auto_now=False, auto_now_add=False)

    class Meta:
        managed = False
        db_table = 'zdm_phone'