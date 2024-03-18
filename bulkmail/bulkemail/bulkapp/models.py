from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class CustomUser(AbstractUser):
    userType=models.CharField(max_length=30,null=True)
class Cu_User(models.Model):
    Name=models.CharField(max_length=50,null=True)
    Phone=models.CharField(max_length=10,null=True)
    Address=models.CharField(max_length=1000,null=True)
    Email=models.EmailField(null=True)
    Uname=models.CharField(max_length=50,null=True)
    password=models.CharField(max_length=50,null=True)
    Department=models.CharField(max_length=30,null=True)
    regDte=models.DateField(auto_now_add=True,null=True)
    modDte=models.DateField(auto_now=True,null=True)
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True)
class EmailHistory(models.Model):
    sender = models.EmailField()
    recipients = models.TextField()  # Store recipients as a comma-separated string
    subject = models.CharField(max_length=255)
    message = models.TextField()
    sent_at = models.DateTimeField(default=timezone.now)
class CFOhistory(models.Model):
    sender = models.EmailField()
    recipients = models.TextField()  # Store recipients as a comma-separated string
    subject = models.CharField(max_length=255)
    message = models.TextField()
    sent_at = models.DateTimeField(default=timezone.now)
class CTOhistory(models.Model):
    sender = models.EmailField()
    recipients = models.TextField()  # Store recipients as a comma-separated string
    subject = models.CharField(max_length=255)
    message = models.TextField()
    sent_at = models.DateTimeField(default=timezone.now)
class CPOhistory(models.Model):
    sender = models.EmailField()
    recipients = models.TextField()  # Store recipients as a comma-separated string
    subject = models.CharField(max_length=255)
    message = models.TextField()
    sent_at = models.DateTimeField(default=timezone.now)
class CROhistory(models.Model):
    sender = models.EmailField()
    recipients = models.TextField()  # Store recipients as a comma-separated string
    subject = models.CharField(max_length=255)
    message = models.TextField()
    sent_at = models.DateTimeField(default=timezone.now)
class BDEhistory(models.Model):
    sender = models.EmailField()
    recipients = models.TextField()  # Store recipients as a comma-separated string
    subject = models.CharField(max_length=255)
    message = models.TextField()
    sent_at = models.DateTimeField(default=timezone.now)
class GMhistory(models.Model):
    sender = models.EmailField()
    recipients = models.TextField()  # Store recipients as a comma-separated string
    subject = models.CharField(max_length=255)
    message = models.TextField()
    sent_at = models.DateTimeField(default=timezone.now)
class GMhistory1(models.Model):
    sender = models.EmailField()
    recipients = models.TextField()  # Store recipients as a comma-separated string
    subject = models.CharField(max_length=255)
    message = models.TextField()
    sent_at = models.DateTimeField(default=timezone.now)
class Placehistory(models.Model):
    sender = models.EmailField()
    recipients = models.TextField()  # Store recipients as a comma-separated string
    subject = models.CharField(max_length=255)
    message = models.TextField()
    sent_at = models.DateTimeField(default=timezone.now)
class Academichistory(models.Model):
    sender = models.EmailField()
    recipients = models.TextField()  # Store recipients as a comma-separated string
    subject = models.CharField(max_length=255)
    message = models.TextField()
    sent_at = models.DateTimeField(default=timezone.now)
class Projecthistory(models.Model):
    sender = models.EmailField()
    recipients = models.TextField()  # Store recipients as a comma-separated string
    subject = models.CharField(max_length=255)
    message = models.TextField()
    sent_at = models.DateTimeField(default=timezone.now)
class HRhistory(models.Model):
    sender = models.EmailField()
    recipients = models.TextField()  # Store recipients as a comma-separated string
    subject = models.CharField(max_length=255)
    message = models.TextField()
    sent_at = models.DateTimeField(default=timezone.now)
class SHhistory(models.Model):
    sender = models.EmailField()
    recipients = models.TextField()  # Store recipients as a comma-separated string
    subject = models.CharField(max_length=255)
    message = models.TextField()
    sent_at = models.DateTimeField(default=timezone.now)
class Students(models.Model):
    Name=models.CharField(max_length=50,null=True)
    Mob=models.CharField(max_length=10,null=True)
    Address=models.CharField(max_length=1000,null=True)
    Email=models.EmailField(null=True)
    Course=models.CharField(max_length=50)
    Duration=models.CharField(max_length=50)
    regDte=models.DateField(auto_now_add=True,null=True)
class Tutorhistory(models.Model):
    tutortype=models.CharField(max_length=50,null=True)
    sender = models.EmailField()
    recipients = models.TextField()  # Store recipients as a comma-separated string
    subject = models.CharField(max_length=255)
    message = models.TextField()
    sent_at = models.DateTimeField(default=timezone.now)  
class Studenthistory(models.Model):
    Studentcourse=models.CharField(max_length=50,null=True)
    sender = models.EmailField()
    recipients = models.TextField()  # Store recipients as a comma-separated string
    subject = models.CharField(max_length=255)
    message = models.TextField()
    sent_at = models.DateTimeField(default=timezone.now)
class Accountshistory(models.Model):
    sender = models.EmailField()
    recipients = models.TextField()  # Store recipients as a comma-separated string
    subject = models.CharField(max_length=255)
    message = models.TextField()
    sent_at = models.DateTimeField(default=timezone.now)  
class Techhistory(models.Model):
    sender = models.EmailField()
    recipients = models.TextField()  # Store recipients as a comma-separated string
    subject = models.CharField(max_length=255)
    message = models.TextField()
    sent_at = models.DateTimeField(default=timezone.now)
class CPOhistory1(models.Model):
    Designation=models.CharField(max_length=50,null=True)
    sender = models.EmailField()
    recipients = models.TextField()  # Store recipients as a comma-separated string
    subject = models.CharField(max_length=255)
    message = models.TextField()
    sent_at = models.DateTimeField(default=timezone.now)  
class Placeteamhistory(models.Model):
    sender = models.EmailField()
    recipients = models.TextField()  # Store recipients as a comma-separated string
    subject = models.CharField(max_length=255)
    message = models.TextField()
    sent_at = models.DateTimeField(default=timezone.now)
class Projectcohistory(models.Model):
    sender = models.EmailField()
    recipients = models.TextField()  # Store recipients as a comma-separated string
    subject = models.CharField(max_length=255)
    message = models.TextField()
    sent_at = models.DateTimeField(default=timezone.now)
class HREhistory(models.Model):
    sender = models.EmailField()
    recipients = models.TextField()  # Store recipients as a comma-separated string
    subject = models.CharField(max_length=255)
    message = models.TextField()
    sent_at = models.DateTimeField(default=timezone.now)
class Inboundhistory(models.Model):
    sender = models.EmailField()
    recipients = models.TextField()  # Store recipients as a comma-separated string
    subject = models.CharField(max_length=255)
    message = models.TextField()
    sent_at = models.DateTimeField(default=timezone.now)