from django.db import models
class employee(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=200)
    address=models.TextField(max_length=200)
    job=models.CharField(max_length=50)
    salary=models.IntegerField()


    def __str__(self):
        return self.name
