from simple_blogger.poster.telegram import TelegramPoster
from simple_blogger.poster.instagram import InstagramPoster
from simple_blogger.poster.vk import VkPoster
from simple_blogger.blogger import Journalist
from simple_blogger.preprocessor.text import TagAdder
from simple_blogger.generator.openai import OpenAiTextGenerator, GptImageGenerator
from simple_blogger.generator.deepseek import DeepSeekTextGenerator
import datetime, json

class Illustrator(Journalist):
    def _message_generator(self):
        # return OpenAiTextGenerator('Ты - книгоман')
        return DeepSeekTextGenerator('Ты - книгоман')
    
    def _image_generator(self):
        return GptImageGenerator(api_key_name="GPT_API_KEY", system_prompt="Нарисуй героя книги по описанию")
    
    def _prompt_constructor(self, _):
        return f"Опиши '{self.task['hero']}' из книги '{self.task['book']}' автора {self.task['author']}, используй не более 100 слов, используй смайлики и не более 150 слов, не используй 'Конечно' и 'Okей'"

    def __init__(self, task):
        self.task = task
        tagadder = TagAdder(['#иллюстрации', '#книги', '#литература', task['tag']])
        posters = [
            TelegramPoster(chat_id='@illustrator_the', processor=tagadder),
            VkPoster(group_id='229821765', processor=tagadder),
            # InstagramPoster(account_token_name='ILLUSTRATOR_THE_TOKEN', account_id='9351594524905971', processor=tagadder)
            # TelegramPoster(processor=tagadder)
        ]
        super().__init__(posters)

def post():
    start_day = datetime.date(2025, 7, 27)
    today = datetime.date.today()
    day_count = (today - start_day).days
    tasks = json.load(open("./files/illustrator_the.json", "rt", encoding="UTF-8"))
    index = day_count % len(tasks)
    task = tasks[index]

    blogger = Illustrator(task)
    blogger.post()

if __name__ == "__main__":
    post()