from django.db import models

# Create your models here.
class FeedbackData(models.Model):
    name=models.CharField(max_length=100)
    rating=models.IntegerField()
    date=models.DateTimeField(max_length=100)
    Feedback=models.CharField(max_length=100)