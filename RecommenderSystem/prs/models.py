from django.db import models

# Create your models here.
class Movie_list(models.Model):
    Movie_id = models.IntegerField()
    Movie_name = models.CharField(max_length=300,null=True,blank=True)
    Sug_1 = models.CharField(max_length=300,null=True,blank=True)
    Sug_2 = models.CharField(max_length=300,null=True,blank=True)
    Sug_3 = models.CharField(max_length=300,null=True,blank=True)
    Sug_4 = models.CharField(max_length=300,null=True,blank=True)
    Sug_5 = models.CharField(max_length=300,null=True,blank=True)
    Sug_6 = models.CharField(max_length=300,null=True,blank=True)
    Sug_7 = models.CharField(max_length=300,null=True,blank=True)
    Sug_8 = models.CharField(max_length=300,null=True,blank=True)
    Sug_9 = models.CharField(max_length=300,null=True,blank=True)
    Sug_10 = models.CharField(max_length=300,null=True,blank=True)
    class Meta:
        db_table='Movie_list'


class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    email = models.CharField(max_length=100)
    content = models.TextField()
