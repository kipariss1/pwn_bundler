from django.db import models


# Create your models here.
class WalletModel(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=42, min_length=42, null=False, blank=False, unique=True)

    # TODO: set name to shortened address on save of the model
