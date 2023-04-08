from django.db import models
from django.utils import timezone


class ParentFeeling(models.Model):
    id = models.CharField(max_length=36, primary_key=True)
    title = models.CharField(max_length=200)
    isVisible = models.BooleanField
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
