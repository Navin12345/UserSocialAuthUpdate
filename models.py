from django.db import models

class UserSocialAuth(models.Model):
    id = models.AutoField(primary_key=True)
    provider = models.CharField(max_length=50)
    uid = models.CharField(max_length=255)
    extra_data = models.CharField(max_length=15)
    user_id = models.IntergerField()

    class Meta:
        db_table = 'social_auth_usersocialauth'
