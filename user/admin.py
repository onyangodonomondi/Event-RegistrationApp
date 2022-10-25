from django.contrib import admin
from .models import Experience
from .models import Education
from .models import skill
from .models import Blog
from .models import Message
from .models import Category
from .models import Image

# Register your models here.
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(skill)
admin.site.register(Blog)
admin.site.register(Message)

admin.site.register(Image)
admin.site.register(Category)


