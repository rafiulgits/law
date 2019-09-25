from account.forms import SignupForm, SigninForm
from account.serializers import ProfileSerializer


from rest_framework.exceptions import NotFound,NotAcceptable
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenRefreshView


class SignIn(APIView):
	renderer_classes = (JSONRenderer,)

	def post(self, request, format=None):

		form = SigninForm(request.POST)
		if form.is_valid():
			user = form.user
			token = RefreshToken.for_user(user)
			data = {
				'refresh' : str(token),
				'access' : str(token.access_token)
			}
			return Response(data)
		else:
			raise NotFound({
				'errors' : form.errors
			})


class SignUp(APIView):
	renderer_classes = (JSONRenderer, )

	def post(self, request, format=None):
		form = SignupForm(request.POST)
		if form.is_valid():
			user = form.save()
			token = RefreshToken.for_user(user)
			data = {
				'refresh' : str(token),
				'access' : str(token.access_token)
			}
			return Response(data)
		else:
			raise NotAcceptable({
				'errors' : form.errors
			})
