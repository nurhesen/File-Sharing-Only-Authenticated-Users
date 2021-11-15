from django.contrib.auth.models import User

try:
    usr=User.objects.create_superuser('testuser', 'testuser@testuser.com', 'testuser')

except:
    pass