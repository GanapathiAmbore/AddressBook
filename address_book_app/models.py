from django.db import models

class Address(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    phone=models.CharField(max_length=100,null=True,blank=True)
    email=models.EmailField(null=True,blank=True)
    website=models.URLField(max_length=100,null=True,blank=True)
    address=models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table='address_book'
