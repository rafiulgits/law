from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import HttpResponse

from draft.graph.engine import Query
from draft.models import Article, Directory
from draft.serializers import DirectorySerializer, ArticleSerailizer

from rest_framework.exceptions import NotFound, PermissionDenied, ValidationError, NotAuthenticated
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated



def root_directories(request):
	if not request.user.is_authenticated:
		raise NotAuthenticated("authentication required")
	if not request.user.is_staff:
		raise PermissionDenied("access denied")
	result = Query.root_directories()
	return HttpResponse(result, content_type='application/json')



class DireactoryView(APIView):
	permission_classes = (IsAuthenticated,)

	def get(self, request):
		location = request.GET.get('location', None)
		if not location:
			raise NotFound('location required')
		result = Query.explore_directory(rootLoc=location)
		return HttpResponse(result, content_type='application/json')


	def post(self, request):
		if not request.user.is_staff:
			raise PermissionDenied("access denied")
		serializer = DirectorySerializer(data=request.POST)
		if serializer.is_valid():
			directory = serializer.create(serializer.validated_data)
			result = Query.explore_directory(rootLocUid=directory.self_loc_id)
			return HttpResponse(result, content_type='application/json')
		raise ValidationError(serializer.errors)


	def put(self, request):
		if not request.user.is_staff:
			raise PermissionDenied("access denied")
		self_loc_uid = request.GET.get('self_loc_uid', None)
		if not self_loc_uid:
			raise ValidationError('directory self location required')
		try:
			directory = Directory.objects.get(self_loc_id=self_loc_uid)
			serializer = DirectorySerializer(data=request.POST, instance=directory)
			if serializer.is_valid():
				directory = serializer.update(serializer.validated_data)
				result = Query.explore_folder(rootLocUid=directory.self_loc_id)
				return HttpResponse(result, content_type='application/json')
		except ObjectDoesNotExist:
			raise NotFound({"directory":"invalid directory UID"})



class ArticleView(APIView):
	permission_classes = (IsAuthenticated,)

	def post(self,request):
		if not request.user.is_staff:
			raise PermissionDenied("access denied")
		serializer = ArticleSerailizer(data=request.POST)
		if serializer.is_valid():
			article = serializer.create(serializer.validated_data)
			result = Query.article(article.uid)
			return HttpResponse(result, content_type="application/json")
		return HttpResponse(serializer.errors, status=400)


	def get(self, request):
		uid = request.GET.get('uid', None)
		if not uid:
			raise NotFound("required a UID")
		result = Query.article(uid)
		return HttpResponse(result, content_type="application/json")


	def put(self, request):
		if not request.user.is_staff:
			raise PermissionDenied("access denied")
		uid = request.GET.get('uid', None)
		if not uid:
			raise NotFound("required a UID")
		try:
			article = Article.objects.get(uid=uid)
			serializer = ArticleSerailizer(data=request.POST, article=article)
			if serializer.is_valid():
				article = serializer.update(serializer.validated_data)
				result = Query.article(article.uid)
				return HttpResponse(result, content_type="application/json")
			else:
				return HttpResponse(serializer.errors, status=400)
		except ObjectDoesNotExist:
			return NotFound("required a valid UID")


	def delete(self, request):
		if not request.user.is_staff:
			raise PermissionDenied("access denied")
		uid = request.GET.get('uid', None)
		if not uid:
			raise NotFound("required a UID")
		try:
			article = Article.objects.get(uid=uid)
			result = Query.article(article.uid)
			article.delete()
			return HttpResponse(result, content_type="application/json")
		except ObjectDoesNotExist:
			return NotFound("required a valid UID")



class AllArticles(APIView):
	permission_classes = (IsAuthenticated,)

	def get(self, request):
		result = Query.all_articles()
		return HttpResponse(result, content_type="application/json")
