from datetime import datetime
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','m_tv.settings')

import django
django.setup()

from forms.models import User, Booking, Slott
from faker import Faker



fake = Faker()

def populate(N=10):
    for entry in range(N):
        
        apartment = 45
        fake_email = fake.email()

        slot_number_1 = 1
        #slot_number_1_start = datetime.time(7,0,0)
        #slot_number_1_end = datetime.time(11,0,0)
        slott_date = datetime.now()
        
        
        
        user = User.objects.get_or_create(apartment_nr=apartment, user_email=fake_email)[0]
       # slot1 = Slott.objects.get_or_create(slott_nr=slot_number_1,slott_start_time=slot_number_1_start, slott_end_time=slot_number_1_end )
       # booking = Booking.objects.get_or_create(booking_date = slott_date, booking_slot=slot_number_1, booking_owner=apartment)

        
        
        #booking = Booking.objects.get_or_create(booking_date = slott_date, booking_slot=1, booking_owner=11)
       
 
       

        user.save()
        #booking.save()
        #booking.save()
        #slot1.save()
        
    return user
     

if __name__ == '__main__':
    print('Adding users')
    populate()
    print('Users added!')
    print