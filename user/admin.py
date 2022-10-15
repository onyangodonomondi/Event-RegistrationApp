from django.contrib import admin
from .models import Experience
from .models import Education
from .models import skills


# Register your models here.
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(skills)