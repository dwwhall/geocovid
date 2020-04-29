from django.contrib import admin

# Register your models here.

from .models import (Sequence, Publications)
admin.site.register(Sequence)
admin.site.register(Publications)