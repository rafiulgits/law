from django.contrib.auth.models import (
	AbstractBaseUser, BaseUserManager,PermissionsMixin, 
	_user_has_module_perms, _user_has_perm, _user_get_all_permissions)

from django.contrib.auth import get_backends
from django.contrib.postgres.fields import JSONField
from django.db import models

from uuid import uuid4


_GENDER = (
	('F', 'Female'),
	('M', 'Male'),
	('O', 'Other'),
	('*', 'Not to say')
)

class UserManager(BaseUserManager):

	def create_user(self,phone,password=None,name=None,email=None,
		is_staff=False,is_superuser=False):
		if not password:
			raise ValueError('password needed')
		if not name:
			raise ValueError('name needed')
		if not email:
			raise ValueError('email needed')

		user = self.model(phone=phone)
		user.name = name
		user.email = email
		user.is_superuser = is_superuser
		user.is_staff = is_staff
		user.set_password(password)
		user.save(self._db)
		return user

	def create_staffuser(self, phone, password, name, email):
		if not phone or password:
			raise ValueError('must have the phone and password')
		if not name:
			raise ValueError('name needed')
		if not email:
			raise ValueError('email needed')


		user = self.create_user(phone, password, name, email, True,False)
		return user

	def create_superuser(self, phone, password, name, email):
		"""
		to create an admin
		"""
		if not phone or not password:
			raise ValueError('must have phone and password')
		if not name:
			raise ValueError('name needed')
		if not email:
			raise ValueError('email needed')


		user = self.create_user(phone, password, name, email, True, True)
		return user


class Account(AbstractBaseUser,PermissionsMixin):
	
	is_active = models.BooleanField(default=True)

	is_superuser = models.BooleanField(default=False)
	is_staff = models.BooleanField(default=False)
	

	phone = models.CharField(max_length=12, unique=True)
	name = models.CharField(max_length=80)
	email = models.EmailField(max_length=120,unique=True)
	gender = models.CharField(max_length=1, choices=_GENDER, default='*')

	objects = UserManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['name','phone',]


	def has_perm(self, perm, obj=None):
		if self.is_superuser:
			return True
		return _user_has_perm(self, perm, obj)

	def has_perms(self, perm_list, obj=None):
		return all(self.has_perm(perm, obj) for perm in perm_list)

	def has_module_perms(self, app_label):
		if self.is_superuser or self.is_staff:
			return True
		return False

	def get_username(self):
		return self.phone





class Profile(models.Model): 
	uid = models.AutoField(primary_key=True)
	account = models.OneToOneField(Account, on_delete=models.CASCADE)
	institute = models.CharField(max_length=250)
	bar = models.CharField(max_length=250)
	session = models.PositiveIntegerField(default=0)




class Reset(models.Model):
	uid = models.UUIDField(primary_key=True, default=uuid4)
	account = models.OneToOneField(Account, on_delete=models.CASCADE)
	date_time = models.DateTimeField(auto_now=True)