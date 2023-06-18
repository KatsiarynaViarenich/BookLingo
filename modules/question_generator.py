from transformers import pipeline

class QuestionGenerator:
    def __init__(self, config):
        self.config = config

    def generate_questions(self, text):
        question_generator = pipeline("question-generation")
        questions = question_generator(text)
        return [q["question"] for q in questions]



