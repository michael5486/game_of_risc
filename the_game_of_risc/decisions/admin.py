from django.contrib import admin

# Register your models here.

from .models import Decision
from .models import Adjudication


#fix user and userprofiles here

admin.site.register(Decision)
admin.site.register(Adjudication)
