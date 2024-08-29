from rest_framework import serializers
from token_bundler.models import WalletModel


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = WalletModel
        fields = '__all__'