from main.shopkeeper import Shop
from main.models import Slot, PickUpBooking, BuyInBooking
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import datetime

# View to create a new slot

@APIView(["POST"])
def create_slot(request):
    try:
        slot_id=request.data['slot_id']
    except:
        return Response({
            "status": False,
            "details": "Please send slot id."
        }, status=status.HTTP_400_BAD_REQUEST)
    try:
        shop_id=request.data['shop_id']
    except:
        return Response({
            "status": False,
            "details": "Please send slot id."
        }, status=status.HTTP_400_BAD_REQUEST)
    try:
        start_time=request.data['start_time']
    except:
        return Response({
            "status": False,
            "details": "Please send start time."
        }, status=status.HTTP_400_BAD_REQUEST)
    try:
        stop_time=request.data['stop_time']
    except:
        return Response({
            "status": False,
            "details": "Please send stop time."
        }, status=status.HTTP_400_BAD_REQUEST)

    shop=Shop.objects.get(id=shop_id)
    if not shop==None:
        slot=Slot()
        slot.slot_id    = slot_id
        slot.start_time = start_time
        slot.stop_time  = stop_time
        slot.save()
        return Response({
            "status": True,
            "slot": slot.to_dict()
        }, status=status.HTTP_201_CREATED)
    else:
        return Response({
            "Status": False,
            "details": "Shop does not exist."
        }, status=status.HTTP_403_FORBIDDEN)



@APIView(["POST"])
def create_buy_in(request):
    try:
        slot_id =   request.data['slot_id']
    except:
        return Response({
            "status": False,
            "details": "Please send slot id."
        }, status=status.HTTP_400_BAD_REQUEST)
    try:
        buyin_id =   request.data['buyin_id']
    except:
        return Response({
            "status": False,
            "details": "Please send buy-in id."
        }, status=status.HTTP_400_BAD_REQUEST)
    try:
        user_id =   request.data['user_id']
    except:
        return Response({
            "status": False,
            "details": "Please send user id."
        }, status=status.HTTP_400_BAD_REQUEST)
    try:
        user_name =   request.data['user_name']
    except:
        return Response({
            "status": False,
            "details": "Please send user's name."
        }, status=status.HTTP_400_BAD_REQUEST)
    slot = Slot.objects.get(slot_id=slot_id)
    if slot==None:
        return Response({
            "status": False,
            "details": "Slot doesn't exist."
        }, status=status.HTTP_403_FORBIDDEN)
    else:
        create_buy_in = BuyInBooking(id= buyin_id)
        create_buy_in.slot = slot
        create_buy_in.user_id = user_id
        create_buy_in.user_name = user_name
        create_buy_in.save()
        return Response({
            "status": True,
            "details": "Buy-In Booking Created."
        }, status=status.HTTP_201_CREATED)


