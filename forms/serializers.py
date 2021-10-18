from forms.models import User, Booking, Slott
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['apartment_nr', 'user_email']

   
class BookingSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Booking
        fields = ['booking_slot', 'booking_owner', 'booking_date']
    
 
  
class SlottSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Slott
        fields = ['slott_nr', 'slott_start_time', 'slott_end_time']
    