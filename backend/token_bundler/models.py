from django.db import models


# Create your models here.
class WalletModel(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=42, null=False, blank=False, unique=True)

    def save(self, *args, **kwargs):
        
        if len(self.name) == 0:
            self.name = f"{self.address[0:5]}...{self.address[-6:0]}"

        super().save(args, kwargs)
