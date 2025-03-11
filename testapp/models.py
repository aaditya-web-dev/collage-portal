from django.db import models

# Create your models here.
class student(models.Model):
    eno=models.IntegerField()
    name=models.CharField(max_length=64)
    specialization=models.CharField(max_length=64)
    image=models.ImageField(upload_to="bciit/image")
    def __str__(self):
        return self.name
    
    
class teacher(models.Model):
    id1=models.IntegerField(unique=True,null=False)
    name=models.CharField(max_length=35)
    Designation=models.CharField(max_length=35)
    subject=models.CharField(max_length=35)
    education=models.CharField(max_length=35)
    exp=models.CharField(max_length=35)
    image=models.ImageField(upload_to="bciit/image")
    
    def __str__(self):
        return self.name