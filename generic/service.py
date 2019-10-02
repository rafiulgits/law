from django.core.mail import send_mail
from django.conf import settings


from jwt import decode as __decode
from jwt import encode as __encode
from jwt.exceptions import InvalidTokenError
from time import time



def verify_email(user):
	token = encode(data={'user_id':user.id, 'email':user.email})
	message = """Click Here to verify your account in AskRiashad.com
	https://dataserver.askriashad.com/api/account/verify/{}
	""".format(token)

	send_mail(
		subject="Ask Riashad verification",
		message = message,
		from_email=settings.EMAIL_HOST_USER,
		recipient_list = [user.email,]
	)


def decode(token):
	try:
		data = __decode(token, settings.SECRET_KEY, algorithms=['HS256'])
		return data
	except InvalidTokenError as e:
		return None


def encode(data, time_stamp=None):
	if time_stamp:
		data['time_stamp'] = int(time())
	token = __encode(data, settings.SECRET_KEY, algorithm='HS256')
	return token.decode()