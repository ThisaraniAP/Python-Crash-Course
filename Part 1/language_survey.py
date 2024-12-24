# 12/07/2021
from survey import AnonymousSurvey

# Define a question and make a survey.
question = "What language did you learn to speak first?"
my_survey = AnonymousSurvey(question)

# Show the question, and store responses to the question.
my_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
	response = input("Language: ")
	if response == 'q':
		break
	my_survey.store_response(response)

# Show the servey results.
print("\nThank you to everyone who partisipated in the survey!")
my_survey.show_results()