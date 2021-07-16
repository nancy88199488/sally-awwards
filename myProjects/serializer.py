from rest_framework import serializers
from .models import MyProjects, Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('bio', 'image', 'user')


class myProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyProjects
        fields = ('title', 'description', 'image','myprojecturl','user') 
        
         