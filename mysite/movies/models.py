from django.db import models

# Create your models here.

class Moviedata(models.Model):

    def _str_(self):
        return self.name
     
    name=models.CharField(max_length=200)
    duration=models.FloatField()
    rating=models.FloatField()
    typ=models.CharField(max_length=200, default='Action')
    image=models.ImageField(upload_to='Images/',default="Images/None/Noimg.jpg")
    