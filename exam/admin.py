from django.contrib import admin
from exam import models

admin.site.register(models.MCQExamSource)
admin.site.register(models.MCQExamItem)
admin.site.register(models.MCQExam)