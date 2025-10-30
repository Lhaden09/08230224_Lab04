from django.contrib import admin

# Register your models here.
from .models import LearningJourney, AboutMe

admin.site.register(LearningJourney)
admin.site.register(AboutMe)