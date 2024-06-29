from django.db import models

class BlacklistedToken(models.Model):
    token = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.token

    class Meta:
        db_table = 'token_blacklist_blacklistedtoken'