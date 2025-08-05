from simple_blogger.poster.telegram import TelegramPoster
from simple_blogger.poster.instagram import InstagramPoster
from simple_blogger.poster.vk import VkPoster
from simple_blogger.blogger import Journalist
from simple_blogger.preprocessor.text import TagAdder
from simple_blogger.generator.openai import OpenAiTextGenerator, OpenAiImageGenerator, GptImageGenerator
import datetime, json
from datetime import date

class HumanizedBlogger(Journalist):
    def _message_generator(self):
        # return GptImageGenerator("Ты - художник с образованием психолога. Я дам тебе категорию и элемент категории. Опиши элемент, как если бы он был человеком , используй не более 100 слов, используй смайлики и не более 150 слов, не используй 'Конечно' и 'Okей'")
        return OpenAiTextGenerator("Ты - художник с образованием психолога. Я дам тебе категорию и элемент категории. Опиши элемент, как если бы он был человеком , используй не более 100 слов, используй смайлики и не более 150 слов, не используй 'Конечно' и 'Okей'", api_key_name="GPT_API_KEY")
    
    def _image_generator(self):
        return GptImageGenerator(api_key_name="GPT_API_KEY", system_prompt="Нарисуй, как бы выглядел человек по описанию")
        # return OpenAiImageGenerator(api_key_name="GPT_API_KEY", system_prompt="Нарисуй, как бы выглядел человек по описанию")

    def _prompt_constructor(self, _):
        return f"{self.task['category']}, {self.task['subject']}"

    def __init__(self, task):
        self.task = task
        tagadder = TagAdder(['#иллюстрации', '#фантазии', f"#{task['category']}"])
        posters = [
            TelegramPoster(chat_id='@humanized_the', processor=tagadder),
            VkPoster(group_id='229862079', processor=tagadder),
            # InstagramPoster(account_token_name='HUMANIZED_THE_TOKEN', account_id='9396881250388941', processor=tagadder)
            # TelegramPoster(processor=tagadder)
        ]
        super().__init__(posters)

def post(offset=0):
    tasks = json.load(open("./files/humanized_the.json", "rt", encoding="UTF-8"))
    start_date = date(2025, 8, 5)
    today = date.today()
    index = ((today - start_date).days + offset) % len(tasks)
    blogger = HumanizedBlogger(tasks[index])
    blogger.post()

if __name__ == "__main__":
    post()