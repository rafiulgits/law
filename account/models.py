from django.contrib.auth.models import (
	AbstractBaseUser, BaseUserManager,PermissionsMixin, 
	_user_has_module_perms, _user_has_perm, _user_get_all_permissions)

from django.contrib.auth import get_backends
from django.db import models


class UserManager(BaseUserManager):

	def create_user(self,phone,password=None,name=None,email=None,
		is_staff=False,is_admin=False):
		if not password:
			raise ValueError('password needed')
		if not name:
			raise ValueError('name needed')
		if not email:
			raise ValueError('email needed')

		user = self.model(phone=phone)
		user.name = name
		user.email = email
		user.is_admin = is_admin
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

	is_admin = models.BooleanField(default=False)
	is_staff = models.BooleanField(default=False)
	
	phone = models.CharField(max_length=12, unique=True)
	name = models.CharField(max_length=80)
	email = models.EmailField(max_length=120,unique=True)

	objects = UserManager()

	USERNAME_FIELD = 'phone'
	REQUIRED_FIELDS = ['name','email',]


	def has_perm(self, perm, obj=None):
		if self.is_admin:
			return True
		return _user_has_perm(self, perm, obj)

	def has_perms(self, perm_list, obj=None):
		return all(self.has_perm(perm, obj) for perm in perm_list)

	def has_module_perms(self, app_label):
		if self.is_admin or self.is_staff:
			return True
		return False

	def get_username(self):
		return self.name+' - '+self.phone