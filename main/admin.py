from django.contrib import admin
from main import models, shopkeeper

# Register your models here.
admin.site.register([
    models.Slot,
    models.PickUpBooking,
    models.BuyInBooking,
    shopkeeper.Shop
    ])
