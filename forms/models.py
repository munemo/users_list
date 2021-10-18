from django.db import models
import datetime


class User(models.Model):
    
    apartment_nr = models.IntegerField(default=1)
    user_email = models.EmailField()
    
class Booking(models.Model):
    booking_date = datetime.date.today()
    booking_slot = models.IntegerField(default=1)
    booking_owner = models.IntegerField(default=1)
    
   
class Slott(models.Model):
  
    slott_nr = models.IntegerField(default=1)
    slott_start_time = datetime.time()
    slott_end_time = datetime.time()
    

    
    
          

