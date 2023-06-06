from django.db import models

# Create your models here.
class Score(models.Model):
    score = models.IntegerField()
    user_id = models.IntegerField()
    username = models.CharField(max_length=200, default='')
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.score)