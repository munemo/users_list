import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','m_tv.settings')

import django
django.setup()

from forms.models import User
from faker import Faker

fake = Faker()

def populate(N=10):
    for entry in range(N):
        
        first = fake.first_name()
        last = fake.last_name()
        user_email = fake.email()
        
        user = User.objects.get_or_create(first_name=first, last_name=last, email=user_email)[0]
        
        print(user.first_name)
        print(user.last_name)
        print(user.email)
        user.save()
        
    return user.first_name
     

if __name__ == '__main__':
    print('Adding users')
    populate()
    print('Users added!')
    print