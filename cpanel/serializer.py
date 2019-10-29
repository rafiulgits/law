from cpanel.models import SupportBox
from rest_framework.serializers import ModelSerializer

class SupportBoxSerializer(ModelSerializer):
	class Meta:
		model = SupportBox
		fields = ['name','email','subject','message']

	def save(self):
		supprt_box = SupportBox.objects.create(
			name=self.validated_date.get('name'),
			email=self.validated_date.get('email'),
			subject=self.validated_date.get('subject'),
			message=self.validated_date.get('message')
			)
		return supprt_box