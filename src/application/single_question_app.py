

class SingleQuestionApp:
    def __init__(self, question):
        self.question = question

    def run(self):
        print(self.question)
        answer = input("Your answer: ")
        print(f"Your answer is: {answer}")