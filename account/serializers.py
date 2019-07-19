from account.models import Account

from rest_framework import serializers


class ProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model = Account
		fields = ('name', 'phone', 'email', 'gender')
