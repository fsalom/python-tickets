from django.db import models

from driven.db.user.models import UserDBO


class MailDBO(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    date_raw = models.CharField(max_length=25)
    email = models.ForeignKey(
        UserDBO, on_delete=models.CASCADE, related_name="mails"
    )
    subject = models.CharField(max_length=150, default="")
    content = models.TextField()

    class Meta:
        verbose_name = "Mail"
        verbose_name_plural = "Mails"