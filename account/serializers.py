from account.models import Profile, Account

from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError, ObjectDoesNotExist

from rest_framework.exceptions import PermissionDenied
from rest_framework.serializers import (ModelSerializer,EmailField,Serializer,CharField
	,IntegerField, BooleanField)



class AccountSerializer(ModelSerializer):
	password = CharField(min_length=6, max_length=60)
	social = BooleanField(default=False)
	class Meta:
		model = Account
		fields = ['name', 'phone', 'email', 'gender', 'password', 'social']



	def _validate_phone(self, phone, exclude_self=False):
		if exclude_self:
			query = Account.objects.filter(phone=phone).exclude(
				id=self.account.id)
		else:
			query = Account.objects.filter(phone=phone)
		if query.exists():
			raise ValidationError("phone already exists")
		return phone

	
	def _validate_email(self, email, exclude_self=False):
		if exclude_self:
			query = Account.objects.filter(email__iexact=email).exclude(
				id=self.account.id)
		else:
			query = Account.objects.filter(email__iexact=email)
		if query.exists():
			raise ValidationError("email already exists")
		return email
	

	def validate(self, data):
		phone = data.get('phone')
		email = data.get('email')

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
		if not validated_data.get('social'):
			account.is_active = False
		account.save()
		return account



class AccountUpdateSerializer(Serializer):
	phone = CharField(max_length=12)
	name = CharField(max_length=80)
	email = EmailField(max_length=120)
	gender = CharField(max_length=1)

	def __init__(self, *args, **kwargs):
		account = kwargs.pop('account')
		super(AccountUpdateSerializer, self).__init__(*args, **kwargs)
		self.account = account


	def _validate_phone(self, phone):
		query = Account.objects.filter(phone=phone).exclude(
				id=self.account.id)
		if query.exists():
			raise ValidationError("phone already exists")
		return phone

	
	def _validate_email(self, email):
		query = Account.objects.filter(email__iexact=email).exclude(
				id=self.account.id)
		if query.exists():
			raise ValidationError("email already exists")
		return email


	def _validate_gender(self, gender):
		if not gender in ['*', 'O', 'M', 'F']:
			raise ValidationError("not a specified gender")
		return gender


	def validate(self, data):
		phone = data.get('phone')
		email = data.get('email')
		gender = data.get('gender')

		self._validate_phone(phone)
		self._validate_email(email)
		self._validate_gender(gender)

		return data


	def save(self, validated_data ,commit=False):
		self.account.name = validated_data.get('name')
		self.account.phone = validated_data.get('phone')
		self.account.email = validated_data.get('email')
		self.account.gender = validated_data.get('gender')
		if commit:
			self.account.save()
		return self.account



class LogSerializer(Serializer):
	email = EmailField()
	password = CharField(min_length=6, max_length=60)

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
			raise ValidationError({"password":["invalid password"]})

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



class ProfileUpdateSerializer(Serializer):
	account = IntegerField()
	institute = CharField(max_length=250)
	bar =CharField(max_length=250)
	session = IntegerField(default=0)


	def __init__(self,*args, **kwargs):
		profile = kwargs.pop('profile')
		account = kwargs.pop('account')
		super(ProfileUpdateSerializer, self).__init__(*args, **kwargs)
		self.profile = profile
		self.account = account


	def validate(self, data):
		if self.account != self.profile.account:
			raise ValidationError("invalid account")
		if data.get('account') != self.profile.account_id:
			raise ValidationError("invalid account")
		if data.get('account') != self.account.id:
			raise ValidationError("invalid account")
		return data


	def update(self, validated_data):
		self.profile.institute = validated_data.get('institute')
		self.profile.bar = validated_data.get('bar')
		self.profile.session = validated_data.get('session')
		self.profile.save()
		return self.profile



class PasswordChangeSerializer(Serializer):
	password = CharField(min_length=6)
	new_password = CharField(min_length=6)
	confirm_password = CharField(min_length=6)

	def __init__(self, *args, **kwargs):
		account = kwargs.pop('account')
		super(PasswordChangeSerializer, self).__init__(*args, **kwargs)
		self.account = account

	def _validate_password(self, password):
		valid = self.account.check_password(password)
		if not valid:
			raise ValidationError("incorrect password")
		return password


	def validate(self, data):
		self._validate_password(data.get('password'))
		if data.get('new_password') != data.get('confirm_password'):
			raise ValidationError("new passwords didn't matched")
		return data

	def save(self, validated_data):
		self.account.set_password(validated_data.get('confirm_password'))
		self.account.save()
		return self.account