from pandas import ExcelFile, read_excel
from blog.models import MCQ
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
		for index , row in sheet.iterrows():
			ans = get_ans(row['Correct Option'])
			if ans:
				mcq = MCQ.objects.create(
					question=row['Question'], 
					answer=ans,
					option1=row['Option A'],
					option2=row['Option B'],
					option3=row['Option C'],
					option4=row['Option D'],
					summary=row['Note']
					)
			else:
				print("{} invalid answer".format(index))
	except Exception as e:
		print(e)