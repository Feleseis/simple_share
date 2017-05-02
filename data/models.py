from django.db import models

# Create your models here.

class Stock(models.Model):
    stock_id = models.IntegerField()
    stock_name = models.CharField(max_length=50)
    def __str__(self):
        return self.stock_id
