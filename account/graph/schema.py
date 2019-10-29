from account.graph.types import AccountType,ProfileType
from account.models import Account,Profile
from django.core.exceptions import ObjectDoesNotExist
from graphene import Field, ID, List, Int



class Query(object):
	account = Field(type=AccountType, id=ID())
	all_accounts = List(AccountType, page=Int())
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



	def resolve_all_accounts(self, info, **kwargs):
		page = kwargs.get('page', None)
		if page:
			if page > 0:
				offset = (page-1)*10
				return Account.objects.all()[offset:offset+10]
		return Account.objects.all()[0:10]