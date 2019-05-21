from django.conf import settings
from django.db import models
from django.utils.timezone import now


class CommonInfo(models.Model):
    created_at = models.DateTimeField("Creado el", default=now, blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, "Creado por", blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = now()

        super(CommonInfo, self).save(*args, **kwargs)

    class Meta:
        abstract = True