from django.contrib import admin
from .models import *

admin.site.register(Post)
admin.site.register(Location)
admin.site.register(Neighbourhood)
admin.site.register(Business)