from django.db import models
from django.utils import timezone

from multiselectfield import MultiSelectField

from app_users.models import CustomUser
from app_hazid.utils import ACTIVITY_OBSERVED, I_OBSERVED, POSSIBLE_CONSEQUENCES, CONDITIONS_RELATED


class Survey(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="surveys")
    created_at = models.DateTimeField(default=timezone.now)

    title = models.CharField(max_length=50)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=35)
    company_observed = models.CharField(max_length=20)
    activity_observed = models.CharField(max_length=27, choices=ACTIVITY_OBSERVED, default=None)
    i_observed = models.CharField(max_length=21, choices=I_OBSERVED, default="None")
    possible_consequences = MultiSelectField(max_length=255, choices=POSSIBLE_CONSEQUENCES)
    conditions_related = MultiSelectField(max_length=500, choices=CONDITIONS_RELATED)
    description = models.CharField(max_length=300)
    swa_applied = models.BooleanField(default=False)
    corrective_measures = models.BooleanField(default=False)
    further_action = models.BooleanField(default=False)
    corrective_action = models.CharField(max_length=150)
    reported = models.BooleanField(default=False)
    if_reported = models.CharField(max_length=100, blank=True)

    class Meta:
        verbose_name = "Hazid"
        verbose_name_plural = "Hazids"
    
    def __str__(self):
        return self.title