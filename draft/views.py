# from django.core.exceptions import ObjectDoesNotExist
# from django.shortcuts import HttpResponse

# from draft.graph.engine import Query
# from draft.models import Article as ArticleModel
# from draft.serializers import ArticleSerailizer

# from rest_framework.exceptions import NotFound, PermissionDenied
# from rest_framework.views import APIView
# from rest_framework.permissions import IsAuthenticated


# class Article(APIView):
#     permission_classes = (IsAuthenticated,)

#     def post(self,request):
#         if not request.user.is_staff:
#             raise PermissionDenied("access denied")
#         serializer = ArticleSerailizer(data=request.POST)
#         if serializer.is_valid():
#             article = serializer.create(serializer.validated_data)
#             result = Query.article(article.uid)
#             return HttpResponse(result, content_type="application/json")
#         return HttpResponse(serializer.errors, status=400)


#     def get(self, request):
#         uid = request.GET.get('uid', None)
#         if not uid:
#             raise NotFound("required a UID")
#         result = Query.article(uid)
#         return HttpResponse(result, content_type="application/json")


#     def put(self, request):
#         if not request.user.is_staff:
#             raise PermissionDenied("access denied")
#         uid = request.GET.get('uid', None)
#         if not uid:
#             raise NotFound("required a UID")
#         try:
#             article = ArticleModel.objects.get(uid=uid)
#             serializer = ArticleSerailizer(data=request.POST, article=article)
#             if serializer.is_valid():
#                 article = serializer.update(serializer.validated_data)
#                 result = Query.article(article.uid)
#                 return HttpResponse(result, content_type="application/json")
#             else:
#                 return HttpResponse(serializer.errors, status=400)
#         except ObjectDoesNotExist:
#             return NotFound("required a valid UID")


#     def delete(self, request):
#         if not request.user.is_staff:
#             raise PermissionDenied("access denied")
#         uid = request.GET.get('uid', None)
#         if not uid:
#             raise NotFound("required a UID")
#         try:
#             article = ArticleModel.objects.get(uid=uid)
#             result = Query.article(article.uid)
#             article.delete()
#             return HttpResponse(result, content_type="application/json")
#         except ObjectDoesNotExist:
#             return NotFound("required a valid UID")



# class AllArticles(APIView):
#     permission_classes = (IsAuthenticated,)

#     def get(self, request):
#         result = Query.all_articles()
#         return HttpResponse(result, content_type="application/json")
