import json 

with open("data/geography1/geography1_questions.json", "r") as json_file:
     questions = json.load(json_file)

# For loop to select question keyword variables
#items = []
#for item in questions:
#    items.append(item['question'])
#print(items)

# Print question keyword variables (same as above)
#print([db_item["question"] 
#  for  db_item 
#  in   questions])

# Print first record 
print(questions[0])  