
from domain.quizz import Question, UserAnswer


def check_user_answer(question: Question, user_answer: UserAnswer) -> bool:
    # TODO: "Check if the user answer is correct according to the question"
    for answer in question.answers:
        if answer.is_correct and answer.answer == user_answer.user_answer:
            return True
    return False