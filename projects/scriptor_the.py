from simple_blogger.poster.telegram import TelegramPoster
from simple_blogger.poster.instagram import InstagramPoster
from simple_blogger.poster.vk import VkPoster
from simple_blogger.blogger import Journalist
from simple_blogger.preprocessor.text import TagAdder
from simple_blogger.generator.openai import OpenAiTextGenerator
# from simple_blogger.generator.openai import OpenAiImageGenerator
from simple_blogger.generator.yandex import YandexImageGenerator
import datetime, json

class ScriptorBlogger(Journalist):
    # def _system_prompt(self):
    #     return 'Ты - игроман'

    def _message_generator(self):
        return OpenAiTextGenerator('Ты - книгоман')
    
    def _image_generator(self):
        return YandexImageGenerator(style_prompt='Киберпанк, гиперреалистичный')

    # def _image_generator(self):
    #     return OpenAiImageGenerator(system_prompt="Нарисуй рисунок, вдохновлённый описанием")

    def _prompt_constructor(self, _):
        return f"Опиши книгу '{self.task['book']}' автора '{self.task['author']}', расскажи интересный факт о книге. Не упоминай авторов. Используй смайлики и не более 150 слов."

    def __init__(self, task):
        self.task = task
        tagadder = TagAdder(['#книгоман', '#книги', '#иллюстрации', f"#{task['genre']}" ])
        posters = [
            TelegramPoster(chat_id='@scriptor_the', processor=tagadder),
            VkPoster(group_id='230463742', processor=tagadder),
            # TelegramPoster(processor=tagadder)
        ]
        super().__init__(posters)

def post(offset=0):
    start_date = datetime.date(2025, 7, 29)
    today = datetime.date.today()
    tasks = json.load(open("./files/scriptor_the.json", "rt", encoding="UTF-8"))
    index = ((today - start_date).days + offset) % len(tasks)
    blogger = ScriptorBlogger(tasks[index])
    blogger.post()

if __name__ == "__main__":
    post()