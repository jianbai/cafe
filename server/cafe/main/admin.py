from django.contrib import admin

# Register your models here.

from .models import User
from .models import Location
from .models import Match

admin.site.register(User)
admin.site.register(Location)
admin.site.register(Match)