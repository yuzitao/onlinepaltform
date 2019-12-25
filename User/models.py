from django.db import models

# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    nickname = models.CharField(max_length=64, null=True)
    phone = models.CharField(max_length=11)
    password = models.CharField(max_length=256)
    emial = models.EmailField(null=True)
    universities = models.CharField(max_length=64, null=True)
    introduction = models.TextField(null=True)

    def __str__(self):
        return self.nickname

    class Meta:
        db_table = 'user'
