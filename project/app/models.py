from django.db import models

# Create your models here.


class Student_Data(models.Model):
    User_name = models.CharField(max_length=50,default="")
    Father_name = models.CharField(max_length=50,default="")
    Email = models.CharField(max_length=50,default="")
    Password = models.CharField(max_length=50,default="")
    About_user = models.TextField()
    Dath_Of_Birth = models.DateTimeField(max_length=50,default="")
    prof_pic = models.ImageField(upload_to="profile_pics",max_length=50,default="")
    def __str__(self):
        return self.User_name


