from asyncio import tasks
from simple_blogger.poster.telegram import TelegramPoster
from simple_blogger.poster.instagram import InstagramPoster
from simple_blogger.poster.vk import VkPoster
from simple_blogger.blogger import Journalist
from simple_blogger.preprocessor.text import TagAdder
from simple_blogger.generator.openai import OpenAiTextGenerator
# from simple_blogger.generator.openai import OpenAiImageGenerator
from simple_blogger.generator.yandex import YandexImageGenerator
import datetime, json

class CinemanBlogger(Journalist):
    # def _system_prompt(self):
    #     return 'Ты - киноман'

    def _message_generator(self):
        return OpenAiTextGenerator('Ты - киноман')
    
    def _image_generator(self):
        return YandexImageGenerator(style_prompt='Стиль мультяшный, анимация в стиле Хидэтака Миядзаки')

    # def _image_generator(self):
    #     return OpenAiImageGenerator(system_prompt="Нарисуй рисунок, вдохновлённый описанием")

    def _prompt_constructor(self, _):
        return f"Опиши фильм '{self.task['movie']}' из категории '{self.task['genre']}', расскажи интересный факт о фильме. Не упоминай авторов. Используй смайлики и не более 150 слов."

    def __init__(self, task):
        self.task = task
        tagadder = TagAdder(['#киноман', '#кино', '#иллюстрации', f"#{task['genre']}" ])
        posters = [
            TelegramPoster(chat_id='@cineman_the', processor=tagadder),
            VkPoster(group_id='230191211', processor=tagadder),
            # InstagramPoster(account_token_name='CINEMAN_THE_TOKEN', account_id='9573627319341163', processor=tagadder)
            # TelegramPoster(processor=tagadder)
        ]
        super().__init__(posters)

def post(offset=0):
    start_date = datetime.date(2025, 7, 30)
    today = datetime.date.today()
    tasks = json.load(open("./files/cineman_the.json", "rt", encoding="UTF-8"))
    index = ((today - start_date).days + offset) % len(tasks)
    blogger = CinemanBlogger(tasks[index])
    blogger.post()

if __name__ == "__main__":
    post()