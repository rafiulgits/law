# from draft.models import Article
# from rest_framework.serializers import ModelSerializer

# class ArticleSerailizer(ModelSerializer):
#     class Meta:
#         model = Article
#         fields = ["title", "body"]
    
#     def __init__(self, *args, **kwargs):
#         article = kwargs.pop('article', None)
#         super(ArticleSerailizer, self).__init__(*args, **kwargs)
#         if article:
#             self.article = article

#     def create(self, validated_data):
#         article = Article(
#             title=validated_data.get('title'),
#             body=validated_data.get('body')
#             )
#         article.save()
#         return article


#     def update(self, validated_data):
#         self.article.title = validated_data.get('title')
#         self.article.body = validated_data.get('body')
#         self.article.save()
#         return self.article