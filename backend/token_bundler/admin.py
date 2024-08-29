from django.contrib import admin

# Register your models here.
from token_bundler.models import WalletModel


admin.site.register(WalletModel)
