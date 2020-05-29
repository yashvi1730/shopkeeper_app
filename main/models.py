from django.db import models
import requests

# Create your models here.

class Slot(models.Model):
    start_time=models.TimeField()
    stop_time=models.TimeField()
   
    

class Buy_In(models.Model):
    name=models.CharField(max_length=100)
    no_of_buyin=models.AutoField(primary_key=True)
    

class Pick_Up(models.Model):
    name=models.CharField(max_length=100)
    notification=models.BooleanField()
    message=models.TextField()
    no_of_pickup=models.AutoField(primary_key=True)


class Booking(models.Model):
    types=(
    ('b','buy_in'),
    ('p','pick_up')
    )
    slot=models.ForeignKey('Slot',on_delete=models.CASCADE)
    order_type=models.CharField(max_length=1,choices=types,default='b')
    pick_up=models.ForeignKey('Pick_Up',blank=True, default = None,null=True,on_delete=models.CASCADE)
    buy_in=models.ForeignKey('Buy_In',blank=True, default = None,null=True,on_delete=models.CASCADE)

    @property
    def polymorphic(self):
        return self.pickup if self.order_type=='p' else self.buy_in