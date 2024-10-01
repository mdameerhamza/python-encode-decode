from django.db import models

class EncodedPayload(models.Model):
    payload = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
