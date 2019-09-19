from account.models import Profile

from rest_framework.exceptions import PermissionDenied
from rest_framework import serializers


class ProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model = Profile
		fields = ['account','institute', 'bar', 'session']


	def set_current_user(self, user):
		self.current_user = user


	def validate(self, data):
		account = data.get('account')
		if self.current_user != account:
			raise PermissionDenied("access denied")
		return data

	def create(self, validated_data):
		profile = Profile(
			account = validated_data.get('account'),
			institute = validated_data.get('institute'),
			bar = validated_data.get('bar'),
		)

		session = validated_data.get('session')
		if session:
			profile.session = session

		profile.save()
		return profile
