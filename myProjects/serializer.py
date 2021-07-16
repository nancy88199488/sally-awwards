from rest_framework import serializers
from .models import Profile,myProjects

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('Bio', 'image', 'user')


class myProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = myProjects
        fields = ('title', 'description', 'image','myprojecturl','user') 
        
         