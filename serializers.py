from edx.app.edxapp.venvs.edxapp.lib.python2.7.site-packages.social_django.models import UserSocialAuth
from rest_framework import serializers

class UserSocialAuthSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserSocialAuth
        fields = '__all__'
        
