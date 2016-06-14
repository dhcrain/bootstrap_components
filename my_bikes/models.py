from django.db import models

# Create your models here.


class MyBike(models.Model):
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.IntegerField()
    type_choice = (('Mountain', "Mountain"), ('Road', "Road"), ('Cruiser', "Cruiser"))
    type = models.CharField(max_length=10, choices=type_choice)
    frame_choice = (('Full Suspension', "Full Suspension"), ('Hardtail', "Hardtail"))
    frame_type = models.CharField(max_length=15, choices=frame_choice)
    build = models.CharField(max_length=100)
    picture = models.URLField(max_length=200, default=False)

    def __str__(self):
        return self.model
