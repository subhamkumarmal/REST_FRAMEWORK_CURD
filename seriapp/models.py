from django.db import models

# Create your models here.

class Students(models.Model):
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    email=models.EmailField()

    def __str__(self):
        return self.name

    class Meta:
        db_table='student'
