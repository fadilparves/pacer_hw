from django.db import models

# Create your models here.
class Score(models.Model):
    score = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    user_id = models.IntegerField()
    def __str__(self):
        return str(self.score)