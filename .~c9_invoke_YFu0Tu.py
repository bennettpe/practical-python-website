def my_question_numbers():
	with open ("./data/geography1/geography1_questions.json", "r") as json_data:
	data = json.load(json_data)
	return data
	
def count_my_question_numbers():
	 count = len(my_question_numbers())
	 return count











