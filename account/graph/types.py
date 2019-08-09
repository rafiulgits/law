from account.models import Account
from graphene_django.types import DjangoObjectType


class AccountType(DjangoObjectType):
	class Meta:
		model = Account