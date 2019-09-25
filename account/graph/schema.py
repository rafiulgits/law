from account.graph.types import AccountType,ProfileType
from account.models import Account,Profile
from django.core.exceptions import ObjectDoesNotExist
from graphene import Field, ID



class Query(object):
	account = Field(type=AccountType, id=ID())
	profile = Field(type=ProfileType, account_id=ID())

	def resolve_account(self, info, **kwargs):
		_id = kwargs.get('id', None)
		if _id is None:
			raise ValueError('must provide an ID')
		try:
			return Account.objects.get(id=_id)
		except ObjectDoesNotExist as e:
			return None


	def resolve_profile(self, info, **kwargs):
		_account_id = kwargs.get('account_id', None)
		if _account_id is None:
			raise ValueError('must provide the account id')
		try:
			return Profile.objects.get(account_id=account_id)
		except ObjectDoesNotExist as e:
			return None