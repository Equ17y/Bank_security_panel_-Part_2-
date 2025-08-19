from django.db import models
from django.utils.timezone import localtime, now
from datetime import timedelta


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    SECONDS_IN_MINUTE = 60
    SECONDS_IN_HOUR = 3600
    SUSPICIOUS_VISIT_DURATION_MINUTES = 60

    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard, on_delete=models.CASCADE)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved=(
                f'leaved at {self.leaved_at}'
                if self.leaved_at else 'not leaved'
            )
        )

    def get_duration(self):
        if self.leaved_at:
            return localtime(self.leaved_at) - localtime(self.entered_at)
        return localtime(now()) - localtime(self.entered_at)

    def is_visit_long(self, minutes=SUSPICIOUS_VISIT_DURATION_MINUTES):
        duration = self.get_duration()
        return duration.total_seconds() > minutes * self.SECONDS_IN_MINUTE

    def format_duration(self):
        duration = self.get_duration()
        total_seconds = int(duration.total_seconds())
        hours = total_seconds // self.SECONDS_IN_HOUR
        minutes = (total_seconds % self.SECONDS_IN_HOUR) // self.SECONDS_IN_MINUTE
        seconds = total_seconds % self.SECONDS_IN_MINUTE
        return f"{hours}:{minutes:02d}:{seconds:02d}"