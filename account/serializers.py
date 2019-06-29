from account.models import Account

from rest_framework.serializers import ModelSerializer



class ProfileSerializer(ModelSerializer):
	class Meta:
		model = Account
		fields = ('name', 'phone', 'email', 'gender')
