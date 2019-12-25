from django.db import models

# Create your models here.

class Works(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    content = models.TextField(null=False)
    img = models.URLField(null=True)
    classification = models.CharField(max_length=64, null=True)
    label = models.CharField(max_length=64, null=True)
    user = models.ForeignKey('User.User', on_delete=models.CASCADE)

    class Meta:
        db_table = 'work'

class Comment(models.Model):
    id = models.AutoField(primary_key=True, unique=True) #unique唯一， 默认为False
    content = models.TextField()
    user = models.ForeignKey('User.User', on_delete=models.CASCADE)
    work = models.ForeignKey('Works', on_delete=models.CASCADE)


    class Meta:
        db_table = 'comment'
