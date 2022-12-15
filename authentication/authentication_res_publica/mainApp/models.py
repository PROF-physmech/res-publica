from django.db import models


class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_role = models.IntegerField()
    user_name = models.CharField(max_length=200)
    user_login = models.CharField(max_length=200, blank=True, null=True)
    user_pass = models.CharField(max_length=200)
    user_photo_id = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
