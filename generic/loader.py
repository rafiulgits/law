from pandas import ExcelFile, read_excel
from blog.models import MCQ, Folder, MCQTag, Path, Category
import math

def get_ans(ans):
	if type(ans) != str:
		return None
	if ans == 'A':
		return 1
	if ans == 'B':
		return 2
	if ans == 'C':
		return 3
	if ans == 'D':
		return 4
	return None


def clear(value):
	if type(value) == str:
		return value.strip()
	if type(value) == int or type(value) == float:
		value = str(value)
		return value.strip()
	return ''



def mcq_sheet(filename):
	try:
		work_book = ExcelFile(filename)
		sheet = read_excel(work_book, work_book.sheet_names[0])

		tag = None 
		current_flag = None

		saved_subject_name = None
		saved_subject_object = None
		is_subject_read = False
		saved_chapter_name = None
		saved_chapter_object = None

		category_subject = Category.objects.get_or_create(name='Subject')[0]
		category_chapter = Category.objects.get_or_create(name='Chapter')[0]

		for index , row in sheet.iterrows():

			subject = row['Subject']
			subject = clear(subject)

			chapter = row['Chapter']
			chapter = clear(chapter)

			if not is_subject_read:
				saved_subject_name = subject
				self_loc = Path.objects.create()

				subject_folder = Folder.objects.create(
					name=saved_subject_name,
					self_loc = self_loc,
					category = category_subject,
					distance = 0
					)
				saved_subject_object = subject_folder
				is_subject_read = True


			if chapter != saved_chapter_name:
				saved_chapter_name = chapter
				self_loc = Path.objects.create()

				chapter_folder = Folder.objects.create(
					name=saved_chapter_name,
					self_loc = self_loc,
					root_loc = saved_subject_object.self_loc,
					category = category_chapter,
					distance = 1
					)
				saved_chapter_object = chapter_folder

			question = row['Question']
			question = clear(question)

			option1=row['Option A']
			option1 = clear(option1)

			option2=row['Option B']
			option2 = clear(option2)

			option3=row['Option C']
			option3 = clear(option3)

			option4=row['Option D']
			option4 = clear(option4)


			mcq = MCQ(
				question=question,
				option1=option1,
				option2=option2,
				option3=option3,
				option4=option4,
				)

			__ans = row['Correct Option']
			__ans = clear(__ans)
			__ans = __ans.upper()
			ans = get_ans(__ans)
			if ans is None:
				continue
			mcq.answer = ans

			summary = row['Note']
			summary = clear(summary)
			mcq.summary = summary

			current_flag = row['Flag']
			current_flag = clear(current_flag)
			mcq.meta = current_flag
			mcq.save()

			MCQTag.objects.create(mcq=mcq, folder=saved_subject_object)
			MCQTag.objects.create(mcq=mcq, folder=saved_chapter_object)



			# ans = get_ans(row['Correct Option'])
			# current_flag = row['Flag']
			# if type(current_flag) != str:
			# 	current_flag = ''
			# if ans:
			# 	mcq = MCQ.objects.create(
			# 		question=row['Question'], 
			# 		answer=ans,
			# 		option1=row['Option A'],
			# 		option2=row['Option B'],
			# 		option3=row['Option C'],
			# 		option4=row['Option D'],
			# 		summary=row['Note'],
			# 		meta=current_flag
			# 		)
			# 	current_tag = row['Chapter']
			# 	if type(current_tag) == str:
			# 		current_tag = current_tag.strip()
			# 		tag = current_tag
			# 		folder = Folder.objects.filter(name__iexact=current_tag).first()
			# 		if folder:
			# 			MCQTag.objects.create(mcq=mcq, folder=folder)
			# 		else:
			# 			print("Folder not found ", index)
			# 	elif tag != None:
			# 		folder = Folder.objects.filter(name__iexact=tag).first()
			# 		if folder:
			# 			MCQTag.objects.create(mcq=mcq, folder=folder)
			# 		else:
			# 			print("Folder not found[old] ", index)
			# 	else:
			# 		print("No TAG ", index)
			# else:
			# 	print("{} invalid answer".format(index))
	

	except Exception as e:
		print(e)