from django.contrib import admin

# Register your models here.

from .models import User
from .models import Location
from .models import Match



#these configure the admin site
class UserDetailAdmin(admin.ModelAdmin):
    list_display = ('firstName', 'lastName', 'age')



admin.site.register(User, UserDetailAdmin)
admin.site.register(Location)
admin.site.register(Match)