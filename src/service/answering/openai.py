import os
from domain.quizz import Image, Question, QuestionType, UserAnswer
from service.answering.base import AnsweringService
from openai import OpenAI
from pydantic import BaseModel


class OpenaiAnsweringService(AnsweringService):
    # api key from the environment (zshrc file)
    # add this line in the bashrc / zshrc file :
    #   export OPENAI_API_KEY="<KEY>"
    # using the API key of your platform.openai account
    API_KEY = os.getenv("OPENAI_API_KEY")

    def answer(self, question: Question) -> UserAnswer:
        """ask chat to answer the question"""
        client = OpenAI()

        # getting the question type
        if question.question_type == QuestionType.unknown or question.question_type is None:
            question.question_type = self.get_question_type(question)
        match question.question_type:
            case QuestionType.elec:
                question_type = "electronic"
            case QuestionType.meca:
                question_type = "mechanics"
            case QuestionType.rules:
                question_type = "the rules of the formula student competition"
            case QuestionType.unknown:
                question_type = "a subject I don't know"

        # building the prompt
        text_prompt = f"""This question is about {question_type}, what is the answer ? Express your certainty about your answer in percentage."""

        match question.question:
            case str(text):
                content = [
                    {
                        "type": "text",
                        "text": text_prompt
                    },
                    {
                        "type": "text",
                        "text": text
                    }
                ]
            case Image(url, _): # see how to handle the case of an np.ndarray
                content = [
                    {
                        "type": "text",
                        "text": text_prompt
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": url
                        }
                    }
                ]
        prompt = [
            {
                "role": "user",
                "content": content
            }
        ]
        # defining the structure of the output
        class Answer(BaseModel):
            text: str
            certainty: float
            explanation: str | None
        # generating chat response
        response = client.beta.chat.completions.parse(
            model="gpt-4o", # change to more recent models if needed
            messages=prompt,
            response_format=Answer
        )
        answer: Answer = response.choices[0].message.parsed
        return UserAnswer(
            question=question,
            user_answer=answer.text,
            certainty=answer.certainty,
            explanation=answer.explanation
        )
        


    def get_question_type(self, question: Question) -> QuestionType:
        """ask chat what is the type of the question"""
        client = OpenAI()
        # building the prompt
        text_prompt = """What is this question about ? You can only chose between elec (electronic), meca (mechanics), rules (rules about the formula student competition) or unknown if you don't know."""
        match question.question:
            case str(text):
                content = [
                    {
                        "type": "text",
                        "text": text_prompt
                    },
                    {
                        "type": "text",
                        "text": text
                    }
                ]
            case Image(url, _): # see how to handle the case of an np.ndarray
                content = [
                    {
                        "type": "text",
                        "text": text_prompt
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": url
                        }
                    }
                ]
        prompt = [
            {
                "role": "user",
                "content": content
            }
        ]
        # defining the structure of the output
        class SubjectOfQuestion(BaseModel):
            type: QuestionType
        # generating chat response
        response = client.beta.chat.completions.parse(
            model="gpt-4o", # change to more recent models if needed
            messages= prompt,
            response_format=SubjectOfQuestion
        )
        subject: SubjectOfQuestion = response.choices[0].message.parsed
        return subject.type