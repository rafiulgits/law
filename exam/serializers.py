from blog.models import Folder, MCQTag
from django.core.exceptions import ValidationError, PermissionDenied
from exam import models
from json import dumps as to_json
import random
from rest_framework.serializers import (ModelSerializer,IntegerField, 
	CharField, ListField)



class MCQExamSerializer(ModelSerializer):
	name = CharField(max_length=100)
	subjects = ListField(child=IntegerField())
	folder_list = []
	class Meta:
		model = models.MCQExamSource
		fields = ['name','public','created_by','total_mcq', 'duration','subjects']



	def set_current_user(self, user):
		self.current_user = user


	def validate(self, data):
		created_by = data.get('created_by')
		if self.current_user != created_by:
			raise PermissionDenied("access denied")

		duration = data.get('duration')
		total_mcq = data.get('total_mcq')
		subjects = data.get('subjects')

		self._validate_duration_vs_question(duration, total_mcq)
		self._validate_folders(subjects)

		return data

	def _validate_duration_vs_question(self, duration, total_mcq):
		if total_mcq == 25 and duration == 15:
			return
		if total_mcq == 50 and duration == 30:
			return
		if total_mcq == 100 and duration == 60:
			return
		raise ValidationError("duration and questions size combination doesn't matched")



	def _validate_folders(self, subjects):
		folder_list = []
		for item in subjects:
			folder = Folder.objects.filter(self_loc_id=item).first()
			if folder:
				folder_list.append(folder)
			else:
				raise ValidationError('selected subject is not available')
		self.folder_list = folder_list



	def create(self, validated_data):
		duration = validated_data.get('duration')
		total_mcq = validated_data.get('total_mcq')
		subjects = validated_data.get('subjects')
		name = validated_data.get('name')
		public = validated_data.get('public')
		created_by = validated_data.get('created_by')

		folder_combination = combination(len(subjects), total_mcq)
		statistics = self._make_statistics(self.folder_list, folder_combination)

		exam_source = models.MCQExamSource.objects.create(
			public = public,
			created_by = created_by,
			total_mcq = total_mcq,
			duration = duration,
			statistics = statistics
			)

		self._generate_exam_questions(exam_source, self.folder_list, folder_combination)

		exam = models.MCQExam.objects.create(name=name, is_clone=False, source=exam_source,
			is_public=public, created_by=created_by)

		return exam



	def _make_statistics(self, folder_list, folder_combination):
		statistics = []
		for index in range(len(folder_list)):
			obj = {
				"folder_self_loc" : folder_list[index].self_loc_id,
				"folder_name" : folder_list[index].name,
				"questions" : folder_combination[index]
			}
			statistics.append(obj)

		return to_json(statistics)




	def _generate_exam_questions(self, exam_source, folder_list, folder_combination):
		for index in range(len(folder_list)):
			folder = folder_list[index]
			questions = folder_combination[index]
			mcq_tags = MCQTag.objects.order_by('?').filter(folder=folder)[:questions]

			for tag in mcq_tags:
				models.MCQExamItem.objects.create(mcq=tag.mcq, exam=exam_source)


def combination(n, total):
    if n == 1:
    	return [total]

    minimum = int(total/(n*2))
    maximum = int(total/2)
    dividers = sorted(random.sample(range(minimum, maximum), n))
    return dividers
    # return [a - b for a, b in zip(dividers + [total], [0] + dividers)]



class MCQExamCloneSerializer(ModelSerializer):
	user = None
	class Meta:
		model = models.MCQExam
		fields = ['name', 'created_by', 'is_public', 'source']


	def set_current_user(self, user):
		self.user = user


	def validate(self, data):
		created_by = data.get('created_by')
		if self.user != created_by:
			raise PermissionDenied("access denied")
		source = data.get("source")
		if source.public == False:
			raise PermissionDenied("source exam is not in public mode")
		return data


	def create(self, validated_data):
		name = validated_data.get("name")
		source = validated_data.get("source")
		is_public = validated_data.get("is_public")
		created_by = validated_data.get("created_by")

		exam = models.MCQExam.objects.create(
				name=name,
				is_public=is_public,
				source=source,
				created_by=created_by,
				is_clone=True
			)

		return exam