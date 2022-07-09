from django.db import models


class Engine(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    problems = models.TextField()
    tuning = models.TextField()
    image = models.ImageField(upload_to='engine/images/')


    def __str__(self):
        return self.title
