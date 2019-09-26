from account.models import Profile, Account

from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError, ObjectDoesNotExist

from rest_framework.exceptions import PermissionDenied
from rest_framework.serializers import (ModelSerializer,EmailField,Serializer,CharField)



class AccountSerializer(ModelSerializer):
	password = CharField(min_length=6, max_length=60)
	current_account = None
	class Meta:
		model = Account
		fields = ['name', 'phone', 'email', 'gender', 'password']

	def set_current_account(self, account):
		self.current_account = account
	

	def _validate_phone(self, phone, exclude_self=False):
		if exclude_self:
			query = Account.objects.filter(phone=phone).exclude(
				id=self.current_account.id)
		else:
			query = Account.objects.filter(phone=phone)
		if query.exists():
			raise ValidationError("phone already exists")
		return phone

	
	def _validate_email(self, email, exclude_self=False):
		if exclude_self:
			query = Account.objects.filter(email__iexact=email).exclude(
				id=self.current_account.id)
		else:
			query = Account.objects.filter(email__iexact=email)
		if query.exists():
			raise ValidationError("email already exists")
		return email
	

	def validate(self, data):
		phone = data.get('phone')
		email = data.get('email')

		if self.current_account:
			self._validate_phone(phone, True)
			self._validate_email(email, True)
		else:
			self._validate_phone(phone)
			self._validate_email(email)
		return data


	def create(self, validated_data):
		account = Account(
			name = validated_data.get('name'),
			phone = validated_data.get('phone'),
			email = validated_data.get('email'),
			gender = validated_data.get('gender')
		)
		password = validated_data.get('password')
		account.set_password(password)
		account.save()
		return account


	def update(self, validated_data):
		self.current_account.name = validated_data.get('name')
		self.current_account.phone = validated_data.get('phone')
		self.current_account.email = validated_data.get('email')
		self.current_account.gender = validated_data.get('gender')
		self.current_account.save()
		return self.current_account




class LogSerializer(Serializer):
	password = CharField(min_length=6, max_length=60)
	email = EmailField()


	def validate_email(self, value):
		account = Account.objects.filter(email__iexact=value).first()
		if account:
			return value
		raise ValidationError("account with this email doesn't exists")


	def validate(self, data):
		email = data.get('email')
		password = data.get('password')

		user = authenticate(email=email, password=password)
		if user:
			self._user = user
			return data
		else:
			raise ValidationError("authentication failed")

	def get_user(self):
		if self._user:
			return self._user
		return None
	


class ProfileSerializer(ModelSerializer):
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

	
	def update(self, validated_data):
		profile = Profile.objects.get(account=self.current_user)
		profile.institute = validated_data.get('institute')
		profile.bar = validated_data.get('bar')
		profile.session = validated_data.get('session')
		profile.save()
		return profile
