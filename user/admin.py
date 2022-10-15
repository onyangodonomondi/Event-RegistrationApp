from django.contrib import admin
from .models import Experience
from .models import Education


# Register your models here.
admin.site.register(Experience)
admin.site.register(Education)