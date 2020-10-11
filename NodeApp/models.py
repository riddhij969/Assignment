from django.db import models

class Products(models.Model):
    Model_No = models.CharField(max_length=20, unique=True)
    Name = models.CharField(max_length=20)
    Description = models.CharField(max_length=200)
    RAM = models.IntegerField()
    Processor = models.CharField(max_length=20)
    Type = models.CharField(max_length=20)

    def __str__(self):
        return self.Model_No

