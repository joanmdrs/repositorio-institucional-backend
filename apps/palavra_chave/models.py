from django.db import models

class PalavraChave(models.Model):
    termo = models.CharField(max_length=100, unique=True)

    def save(self, *args, **kwargs):
        self.termo = self.termo.strip().lower()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.termo
