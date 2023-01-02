from django.db import models

# Create your models here.

class Movie(models.Model):
    name = models.CharField(max_length=250)
    desc = models.TextField(max_length=220)
    year = models.IntegerField()
    image = models.ImageField(upload_to='galary')


    # def __str__(self):
    #     return self.name

    def __str__(self):
        return "%s" % self.name