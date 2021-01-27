from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class CVInfo(models.Model):
    template1 = models.BooleanField(default=True)
    template2 = models.BooleanField(default=False)
    cvColor = models.CharField(default="rgb(29, 202, 130)", max_length=255)
    fullName = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zip_code = models.IntegerField()
    cvEmail = models.EmailField()
    phoneNum = models.IntegerField()
    objective = models.TextField(default="I am seeking employment with a company where I can grow professionally and personally.I seek challenging opportunities where I can fully use my skills for the success of the organization.With the sill sets that I have I am very confident that I am perfect for this job.")
    hobbyandinterest = models.CharField(max_length=255)
    reference = models.CharField(max_length=255, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)



class PersonalAccomplishment(models.Model):
    paccomplishment1 = models.CharField(max_length=500, blank=True, null=True)
    paccomplishment2 = models.CharField(max_length=500, blank=True, null=True)
    paccomplishment3 = models.CharField(max_length=500, blank=True, null=True)
    paccomplishment4 = models.CharField(max_length=500, blank=True, null=True)
    paccomplishment5 = models.CharField(max_length=500, blank=True, null=True)
    cvinfo = models.ForeignKey(CVInfo, on_delete=models.CASCADE)


class ProfessionalAccomplishment(models.Model):
    praccomplishment1 = models.CharField(max_length=500, blank=True, null=True)
    praccomplishment2 = models.CharField(max_length=500, blank=True, null=True)
    praccomplishment3 = models.CharField(max_length=500, blank=True, null=True)
    praccomplishment4 = models.CharField(max_length=500, blank=True, null=True)
    praccomplishment5 = models.CharField(max_length=500, blank=True, null=True)
    cvinfo = models.ForeignKey(CVInfo, on_delete=models.CASCADE)


class Education(models.Model):
    schoolandcollege = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    grade = models.CharField(max_length=255)
    date = models.CharField(max_length=255)
    cvinfo = models.ForeignKey(CVInfo, on_delete=models.CASCADE)


class Education1(models.Model):
    schoolandcollege = models.CharField(max_length=255, blank=True, null=True)
    subject = models.CharField(max_length=255, blank=True, null=True)
    grade = models.CharField(max_length=255, blank=True, null=True)
    date = models.CharField(max_length=255, blank=True, null=True)
    cvinfo = models.ForeignKey(CVInfo, on_delete=models.CASCADE)


class Education2(models.Model):
    schoolandcollege = models.CharField(max_length=255, blank=True, null=True)
    subject = models.CharField(max_length=255, blank=True, null=True)
    grade = models.CharField(max_length=255, blank=True, null=True)
    date = models.CharField(max_length=255, blank=True, null=True)
    cvinfo = models.ForeignKey(CVInfo, on_delete=models.CASCADE)


class WorkHistory(models.Model):
    jobTitle = models.CharField(max_length=255, blank=True, null=True)
    companyName = models.CharField(max_length=255, blank=True, null=True)
    employmentDateStart = models.CharField(
        max_length=50, blank=True, null=True)
    employmentDateEnd = models.CharField(max_length=50, blank=True, null=True)
    cvinfo = models.ForeignKey(CVInfo, on_delete=models.CASCADE)


class CVImg(models.Model):
    img = models.FileField(upload_to="media", blank=True, null=True,  default='/media/media/avatar.png')
    cvinfo = models.ForeignKey("CVInfo", on_delete=models.CASCADE)
