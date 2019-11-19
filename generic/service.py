from django.core.mail import send_mail
from django.conf import settings


from jwt import decode as __decode
from jwt import encode as __encode
from jwt.exceptions import InvalidTokenError
from time import time




def generate_token(data, expired_days=None):
	if expired_days != None:
		data['expired'] = generate_timestamp(expired_days)
	token = __encode(data, settings.SECRET_KEY, algorithm='HS256')
	return token.decode()




def verify_token(token):
	try:
		data = __decode(token, settings.SECRET_KEY, algorithms=['HS256'])
		if data.get('expired', None):
			if not verify_expired_date(data.get('expired')):
				return None
		return data
	except InvalidTokenError as e:
		return None




from datetime import datetime,timedelta

def generate_timestamp(days):
	date_time = datetime.now() + timedelta(days=days)
	return date_time.timestamp()


def verify_expired_date(expired_timestamp):
	current_timestamp = generate_timestamp(0)
	return current_timestamp <= expired_timestamp





from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template


def send_template_mail(to_mail,subject,body_path,template_path,context={}):
	plain_text = get_template(body_path)
	htmly = get_template(template_path)

	text_content = plain_text.render(context)
	html_content = htmly.render(context)

	from_email = settings.EMAIL_HOST_USER

	msg = EmailMultiAlternatives(
		subject=subject,
	 	body=text_content, from_email=from_email,
	 	to=[to_mail,])
	msg.attach_alternative(html_content, "text/html")
	msg.send()