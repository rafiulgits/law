from pandas import ExcelFile, read_excel
from blog.models import MCQ, Folder, MCQTag
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

def mcq_sheet(filename):
	try:
		work_book = ExcelFile(filename)
		sheet = read_excel(work_book, work_book.sheet_names[0])

		tag = None 
		current_flag = None

		for index , row in sheet.iterrows():
			ans = get_ans(row['Correct Option'])
			current_flag = row['Flag']
			if type(current_flag) != str:
				current_flag = ''
			if ans:
				mcq = MCQ.objects.create(
					question=row['Question'], 
					answer=ans,
					option1=row['Option A'],
					option2=row['Option B'],
					option3=row['Option C'],
					option4=row['Option D'],
					summary=row['Note'],
					meta=current_flag
					)
				current_tag = row['Chapter']
				if type(current_tag) == str:
					current_tag = current_tag.strip()
					tag = current_tag
					folder = Folder.objects.filter(name__iexact=current_tag).first()
					if folder:
						MCQTag.objects.create(mcq=mcq, folder=folder)
					else:
						print("Folder not found ", index)
				elif tag != None:
					folder = Folder.objects.filter(name__iexact=tag).first()
					if folder:
						MCQTag.objects.create(mcq=mcq, folder=folder)
					else:
						print("Folder not found[old] ", index)
				else:
					print("No TAG ", index)
			else:
				print("{} invalid answer".format(index))
	except Exception as e:
		print(e)