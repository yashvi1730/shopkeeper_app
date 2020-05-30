from django.urls import path
from main import views

urlpatterns = [
    path('slots',views.slots,name="slots"),
    path('pick_up',views.pick_up,name="pickup"),
    path('buyin',views.buy_in,name="buy_in")
]