from blog.models import MCQ
from cpanel.models import SupportBox
from rest_framework.serializers import ModelSerializer

class SupportBoxSerializer(ModelSerializer):
	class Meta:
		model = SupportBox
		fields = ['name','email','subject','message']

	def save(self):
		supprt_box = SupportBox.objects.create(
			name=self.validated_data.get('name'),
			email=self.validated_data.get('email'),
			subject=self.validated_data.get('subject'),
			message=self.validated_data.get('message')
			)
		return supprt_box




class MCQSerializer(ModelSerializer):
	class Meta:
		model = MCQ
		fields = ['question', 'answer', 'option1', 'option2', 'option3', 'option4', 'summary']


	def __init__(self, *args, **kwargs):
		instance = kwargs.pop('instance')
		super(MCQSerializer, self).__init__(*args, **kwargs)
		self.instance = instance


	def save(self):
		self.instance.question = self.validated_data['question']
		self.instance.answer = self.validated_data['answer']
		self.instance.option1 = self.validated_data['option1']
		self.instance.option2 = self.validated_data['option2']
		self.instance.option3 = self.validated_data['option3']
		self.instance.option4 = self.validated_data['option4']
		self.instance.summary = self.validated_data['summary']
		self.instance.save()
		return self.instance