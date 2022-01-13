# petshop
Pet Shop Boys

1. Seems like you have defined some `User` in `api` app, so add that app to the installed apps in `settings.py`:
```py
# settings.py
INSTALLED_APPS = [
    ...
    "api",
```

Also, it is not really possible or needed to reference the `User` in this way.

I imagine your `models.py` to be something like this:
```py
from api.models import CustomUser
from django.db import models


class Pet(models.Model):
    name = models.CharField(max_length=100)
    pet_sitter = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='pets', blank=True,null=True)

class Booking(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    start_date = models.DateTimeField()  
    end_date = models.DateTimeField()
```

check the source code here 