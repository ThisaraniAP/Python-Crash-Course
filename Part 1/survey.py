# 12/07/2021
class AnonymousSurvey:
	"""Collect anonymous answers to a servey question."""

	def __init__(self, question):
		"""Store a question and prepare to store responses."""
		self.question = question
		self.responses = []

	def show_question(self):
		"""Show the servey question."""
		print(self.question)

	def store_response(self, new_response):
		"""Store a single responce to the servey."""
		self.responses.append(new_response)

	def show_results(self):
		"""Show all the responses that have been give."""
		print("Servey results:")
		for response in self.responses:
			print(f"- {response}")