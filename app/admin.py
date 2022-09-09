from django.contrib import admin

# Register your models here.
from .models import happy
from .models import sad
from .models import Complaints
from .models import admlogin
from .models import dash


admin.site.register(happy)
admin.site.register(sad)
admin.site.register(dash)
admin.site.register(Complaints)
admin.site.register(admlogin)
