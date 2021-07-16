from django.contrib import admin
from .models import MyProjects, Profile, Rating,

# Register your models here.
admin.site.register(Profile)
admin.site.register(MyProjects)
admin.site.register(Rating)