from django.urls import path
from main import views

urlpatterns = [
    path('bookings/',views.BookingListView.as_view()),
    path('slots/',views.SlotListView.as_view())
]