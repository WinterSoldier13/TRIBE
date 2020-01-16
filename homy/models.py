from django.db import models

# Create your models here.
class product(models.Model):

    pname=models.CharField(max_length=100)
    img1=models.ImageField(upload_to='pics')
    img2=models.ImageField(upload_to='pics')
    dis=models.IntegerField(default=0)
    newprice=models.IntegerField(default=0)
    oldprice=models.IntegerField(default=0)
    pdesc=models.CharField(max_length=100)

    def __str__(self):
        return self.pname
