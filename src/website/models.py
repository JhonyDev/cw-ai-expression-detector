from django.db import models

from src.accounts.models import User


class Session(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True, blank=True)

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name_plural = 'Sessions'
        ordering = ['-id']


class ScanImage(models.Model):
    image_url = models.ImageField(upload_to='images/', null=False, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    stress_level = models.FloatField(default=None, null=True, blank=True)
    status = models.CharField(default=None, null=True, blank=True, max_length=50)
    session = models.ForeignKey(Session, on_delete=models.CASCADE, default=None, null=True, blank=True)

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name_plural = 'Scan Images'
        ordering = ['-id']
