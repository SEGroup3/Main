class Question():

	def __init__(self, q_type, contents, correct_ans = None):
		self.q_type = q_type
		self.contents = contents
		self.correct_ans = correct_ans

	def ask_q(self):
		print(self.contents)
		answer = input()
		if answer in self.correct_ans:
			print("Correct!")
			return True
		else:
			print("Wrong.")
			return False



if __name__ == "__main__":
	a_question = Question("Math", "1 + 1 = ?", "2")
	score = 0
	if a_question.ask_q():
		score += 1
	print(score)
