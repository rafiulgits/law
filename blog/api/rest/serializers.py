from blog.forms import FolderForm, MCQForm, CQForm
from blog.models import Folder, CQ, MCQ 

from rest_framework.serializers import ModelSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView

class FolderREST(APIView):
	def get(self, request, format=None):
		pass

	def post(self, request, format=None):
		pass