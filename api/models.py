from django.db import models


class User(models.Model):
    class Meta:
        db_table = 'users'
        managed = True

    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=200)
    user_type = models.CharField(max_length=100 , default="Email")

    def __unicode__(self):
        return self.email