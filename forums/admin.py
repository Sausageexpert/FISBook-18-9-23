from django.contrib import admin
from .models import Forum,Events,Notices

# Register your models here.

admin.site.register(Forum)
admin.site.register(Events)
admin.site.register(Notices)