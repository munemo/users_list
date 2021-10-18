from django.contrib import admin
from forms.models import Slott, User, Booking

admin.site.register(User)
admin.site.register(Booking)
admin.site.register(Slott)