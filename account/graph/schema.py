from account.graph.types import AccountType
from account.models import Account
from django.core.exceptions import ObjectDoesNotExist
from graphene import Field, ID



class Query(object):
	account = Field(type=AccountType, id=ID())

	def resolve_account(self, info, **kwargs):
		_id = kwargs.get('id', None)
		if _id is None:
			raise ValueError('must provide an ID')
		try:
			return Account.objects.get(id=_id)
		except ObjectDoesNotExist as e:
			return None