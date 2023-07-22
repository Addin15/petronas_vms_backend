import uuid
from django.db import models
from users.models import User

# Create your models here.
class Meeting(models.Model):
    summary = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    purpose = models.CharField(max_length=50)
    venue = models.TextField()
    test = models.BooleanField(default=False)

class Invitation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE)
    host = models.ForeignKey(User, on_delete=models.CASCADE)
    visitor_name = models.CharField(max_length=255,null=True)
    visitor_email = models.EmailField()
    visitor_nric = models.CharField(max_length=20, null=True)
    visitor_phone = models.CharField(max_length=20,null=True)
    is_preregistered = models.BooleanField(default=False)
    in_time = models.TimeField(null=True)
    out_time = models.TimeField(null=True)