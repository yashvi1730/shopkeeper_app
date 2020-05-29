from django.contrib import admin
from main import models

# Register your models here.
admin.site.register([
    models.Booking,
    models.Slot,
    models.Buy_In,
    models.Pick_Up
])
