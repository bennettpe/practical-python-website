def get_question_sheet():
    
    #opens the question sheet which contains the questions
    
    with open("gamefiles/questions_sheet.json", "r") as f:
        questions_sheet = json.load(f)
        return questions_sheet
        
    with open("data/geography1/geography1_questions.json", "r") as json_file:
     questions = json.load(json_file)        