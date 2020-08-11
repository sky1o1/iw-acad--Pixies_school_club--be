from django.db import models


class Club(models.Model):
    president_name = models.CharField(max_length=150, default='Megha')
    club_name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    logo = models.ImageField()

    def __str__(self):
        return self.club_name