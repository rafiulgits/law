from draft.models import Pointer, Directory, Article
from rest_framework.serializers import ModelSerializer


class DirectorySerializer(ModelSerializer):
    class Meta:
        model = Directory
        fields = ['name' ,'root_loc']

    def __init__(self, *args, **kwargs):
        instance = kwargs.pop('instance', None)
        super(DirectorySerializer, self).__init__(*args, **kwargs)
        if instance:
            self.instance = instance


    def _validate_pointers(self, self_loc, root_loc):
        if self_loc.uid == root_loc.uid:
            raise ValidationError("invalid parent selected")
        return


    def validate(self, data):
        if self.instance:
            if data.get('root_loc',None):
                self._validate_pointers(self.instance.self_loc, data.get('root_loc'))
        return data


    def create(self, validated_data):
        directory = Directory.objects.create(
            name=validated_data.get('name'),
            root_loc=validated_data.get('root_loc'),
            self_loc=Pointer.objects.create()
            )
        return directory


    def update(self, validated_data):
        self.instance.name = validated_data.get('name')
        if validated_data.get('root_loc', None):
            self.instance.root_loc = validated_data.get('root_loc')
        self.instance.save()
        return self.instance



class ArticleSerailizer(ModelSerializer):
    class Meta:
        model = Article
        fields = ["title","label", "body", "directory"]

    def __init__(self, *args, **kwargs):
        article = kwargs.pop('article', None)
        super(ArticleSerailizer, self).__init__(*args, **kwargs)
        if article:
            self.article = article

    def create(self, validated_data):
        article = Article(
            title=validated_data.get('title'),
            body=validated_data.get('body'),
            label=validated_data.get('label'),
            directory=validated_data.get('directory')
            )
        article.save()
        return article


    def update(self, validated_data):
        self.article.title = validated_data.get('title')
        self.article.body = validated_data.get('body')
        self.article.label = validated_data.get('label')
        self.article.directory = validated_data.get('directory')
        self.article.save()
        return self.article