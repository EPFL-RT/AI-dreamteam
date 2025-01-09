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
        # ask chat to anskwer the question
        pass
        


    def get_question_type(self, question: Question) -> QuestionType:
        # ask chat what is the type of the question
        client = OpenAI()
        question_image: Image = question.question
        # building the prompt
        text_prompt = """What is this question about ? 
        You can only chose between elec (electronic), meca (mechanics), 
        rules (rules about the formula student competition) or unknown if you don't know."""
        content = [
                {
                    "type": "text",
                    "text": text_prompt
                },
                { # see how to handle the case where the image is a np.ndarray
                    "type": "image_url",
                    "image_url": {
                        "url" : question_image.url 
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