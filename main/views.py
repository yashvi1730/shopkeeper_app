from rest_framework.response import Response
from main import models
# from main import models,serializers
# from rest_framework.generics import(
#     ListAPIView,
#     RetrieveAPIView,
#     UpdateAPIView,
#     RetrieveUpdateAPIView,
#     ListCreateAPIView,
#     DestroyAPIView
# )
# # Create your views here.
#
# class BookingListView(ListCreateAPIView):
#     queryset=models.Booking.objects.all()
#     serializer_class=serializers.BookingSerializer
#
def slots(request):
    slot=models.Slot.objects.all()
    context={
        "start_time":slot.start_time,
        "stop_time":slot.stop_time,
        "buy_in":slot.num_buyins,
        "pick_up":slot.num_pickups,
        "view":slot.to_dict()
    }

    return render(request,'slots.html',context)

def pick_up(request):
    pickup=models.PickUpBooking.objects.all()
    context={
        "message":pickup.message,
        "name":pickup.user_name,
        "is_fulfilled":pickup.is_fulfilled

    }

    return render(request,'pick_up.html',context)

def buy_in(request):
    buyin=models.BuyInBooking.objects.all()
    context={
         "name":buyin.user_name,
        "is_fulfilled":buyin.is_fulfilled
    }

    return render(request,'buy_in.html',context)


