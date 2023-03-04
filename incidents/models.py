from django.db import models
from incidents import constants
from login.models import User
import random
import datetime
# from django.contrib.auth import get_user_model
# User = get_user_model()

class Incident(models.Model):
    incident_id = models.CharField(max_length=100, blank=True,unique=True)
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=True, default='')
    body = models.TextField(blank=True, default='')
    status = models.CharField(
        max_length=20,
        choices=constants.STATUS_CHOICES,
        default=constants.OPEN
    )
    priority = models.CharField(
        max_length=20,
        choices=constants.PRIORITY_CHOICES,
        default=constants.LOW
    )
    # exclude=("incident_id")
    user = models.ForeignKey(User, related_name='incidents', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']

    def __str__(self):
            return self.incident_id

    def idd(self):
        today = datetime.date.today()
        year = today.year
        id= 'RMG' + str(random.randrange(11111,99999,5)) + str(year)
        return id

    def save(self):
        if not self.incident_id:
            self.incident_id = self.idd()
            while Incident.objects.filter(incident_id=self.incident_id).exists():
                self.incident_id=self.idd()
        super(Incident,self).save()

