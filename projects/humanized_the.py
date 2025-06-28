from simple_blogger.poster.telegram import TelegramPoster
from simple_blogger.poster.instagram import InstagramPoster
from simple_blogger.poster.vk import VkPoster
from simple_blogger.blogger import Journalist
from simple_blogger.preprocessor.text import TagAdder
from simple_blogger.generator.openai import OpenAiTextGenerator, OpenAiImageGenerator, GptImageGenerator
import datetime

class HumanizedBlogger(Journalist):
    def _message_generator(self):
        # return GptImageGenerator('Ты - художник с образованием психолога')
        return OpenAiTextGenerator('Ты - художник с образованием психолога', api_key_name="GPT_API_KEY")
    
    def _image_generator(self):
        return GptImageGenerator(api_key_name="GPT_API_KEY", system_prompt="Нарисуй, как бы выглядел человек по описанию")
        # return OpenAiImageGenerator(api_key_name="GPT_API_KEY", system_prompt="Нарисуй, как бы выглядел человек по описанию")

    def _prompt_constructor(self, _):
        return f"Describe any random {self.subject}, if it were a human been. Дай ответ на русском языке, используй смайлики и не более 150 слов, не используй 'Конечно' и 'Okей'"

    def __init__(self, subject):
        self.subject = subject
        tagadder = TagAdder(['#иллюстрации', '#фантазии'])
        posters = [
            TelegramPoster(chat_id='@humanized_the', processor=tagadder),
            VkPoster(group_id='229862079', processor=tagadder),
            # InstagramPoster(account_token_name='HUMANIZED_THE_TOKEN', account_id='9396881250388941', processor=tagadder)
            # TelegramPoster(processor=tagadder)
        ]
        super().__init__(posters)

def post(offset=0):
    start_date = datetime.date(2025, 3, 26)
    today = datetime.date.today()
    subjects = [
        "animal",
        "book",
        "browser",
        "car brand",
        "capital city",
        "computer",
        "game console",
        "cosmic ship",
        "country",
        "cpu",
        "delivery company",
        "russian delivery company",
        "car model",
        "fashion brand",
        "flower",
        "fruit",
        "game",
        "famous house",
        "insect",
        "information technology brand",
        "programming language",
        "mobile phone",
        "movie",
        "photo camera",
        "point of interest",
        "river",
        "ship",
        "sneakers",
        "song",
        "stadium",
        "tree",
        "vegetable",
    ]
    index = ((today - start_date).days + offset) % len(subjects)
    blogger = HumanizedBlogger(subjects[index])
    blogger.post()

if __name__ == "__main__":
    post()