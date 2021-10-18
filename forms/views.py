from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, permissions
from forms.serializers import SlottSerializer, UserSerializer, BookingSerializer
from forms.models import User, Booking, Slott

 

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    
class BookingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows bookings to be viewed or edited.
    """
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

  
class SlottViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows bookings to be viewed or edited.
    """
    queryset = Slott.objects.all()
    serializer_class = SlottSerializer
    permission_classes = [permissions.IsAuthenticated]

