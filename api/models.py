from django.db import models

class Task (models.Model):
    name=models.CharField( max_length=500)
    caption=models.CharField( max_length=500)
    url=models.CharField( max_length=500)

    def __str__(self):
        return self.name