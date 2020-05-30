from django.db import models
from .shopkeeper import Shop
# Create your models here.

class Slot(models.Model):
    shop            = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='slots')
    slot_id         = models.CharField(max_length=16, unique=True, primary_key=True)
    start_time      = models.DateTimeField()
    stop_time       = models.DateTimeField()
    num_pickups     = models.IntegerField(default=0)
    num_buyins      = models.IntegerField(default=0)

    def to_dict(self):
        return {
            "shop_name" : self.shop.name,
            "shop_id"   : self.shop.id,
            "slot_id"   : self.user_id,
            "user_id"   : self.user_name,
            "start_time": self.start_time,
            "stop_time" : self.stop_time
        }

class BuyInBooking(models.Model):
    id              = models.CharField(max_length=16, unique=True, primary_key=True)
    slot            = models.ForeignKey(Slot, on_delete=models.CASCADE, related_name='buyin')
    user_id = models.CharField(max_length=16, unique=True, null=True)
    user_name = models.CharField(max_length=100)
    is_fulfilled    = models.BooleanField(default=False)




class PickUpBooking(models.Model):
    id              = models.CharField(max_length=16, unique=True, primary_key=True)
    slot            = models.ForeignKey(Slot, on_delete=models.CASCADE, related_name='pickup')
    is_fulfilled    = models.BooleanField(default=False)
    user_id = models.CharField(max_length=16, unique=True, null=True)
    user_name = models.CharField(max_length=100)
    message         = models.CharField(max_length=256)