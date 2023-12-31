import requests


class QuestionGenerator:
    def __init__(self):
        self.API_URL = "https://api-inference.huggingface.co/models/mrm8488/t5-base-finetuned-question-generation-ap"
        self.API_KEY = "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"
        self.headers = {"Authorization": f"Bearer {self.API_KEY}"}

    def query(self, payload):
        response = requests.post(self.API_URL, headers=self.headers, json=payload)
        response.raise_for_status()
        return response.json()

    def generate_questions(self, text):
        passage_length = int(len(text) / 2)
        passages = [
            text[i : i + passage_length] for i in range(0, len(text), passage_length)
        ]
        try:
            output = []
            for passage in passages:
                result = self.query({"inputs": passage,})[0][
                    "generated_text"
                ][10:]
                if result[-1] == "?":
                    output.append(result)
            if output is None:
                output = ["There are no good questions."]
        except ConnectionError:
            return ["Network connection error."]
        except Exception as e:
            print(e)
        return output
