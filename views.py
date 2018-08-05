from django.shortcuts import render
from student.models import UserProfile
from edx.app.edxapp.venvs.edxapp.lib.python2.7.site-packages.social_django.models import UserSocialAuth
from rest_framework.response import Response
from rest_framework.views import APIView

class socialauth(APIView):
    def post(self, request):
        data_username = request.data
        user_profile=UserProfile.objects.get(username=data_username['username'])
        userid=user_profile.user_id
        data['provider'] = 'google-oauth2'
        data['uid'] = userid
        
        user_serializer = UserSocialAuthSerializer(data = data)
        if UserSocialAuthSerializer.is_valid():

            current = user_serializer.objects.filter(student_id = student_id, course_id = course_id)
            UserSocialAuthSerializer.save()
            return Response(UserSocialAuthSerializer.data, status=status.HTTP_201_CREATED)

        return Response(UserSocialAuthSerializer.data, status=status.HTTP_400_BAD_REQUEST)
