from account.models import Account, Profile
from graphene_django.types import DjangoObjectType


class AccountType(DjangoObjectType):
	class Meta:
		model = Account


class ProfileType(DjangoObjectType):
	class Meta:
		model = Profile 