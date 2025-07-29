from simple_blogger.poster.telegram import TelegramPoster
from simple_blogger.poster.instagram import InstagramPoster
from simple_blogger.poster.vk import VkPoster
from simple_blogger.blogger import Journalist
from simple_blogger.preprocessor.text import TagAdder
from simple_blogger.generator.openai import OpenAiTextGenerator, OpenAiImageGenerator
from simple_blogger.generator.yandex import YandexImageGenerator, YandexTextGenerator
import datetime, json

class MelomanBlogger(Journalist):
    # def _system_prompt(self):
    #     return 'Ты - меломан'

    def _message_generator(self):
        return OpenAiTextGenerator('Ты - меломан')
        # return YandexTextGenerator('Ты - меломан')
    
    def _image_generator(self):
        # return YandexImageGenerator(style_prompt='Стиль мультяшный, анимация в стиле Хидэтака Миядзаки')
        return OpenAiImageGenerator(system_prompt="Нарисуй рисунок, вдохновлённый песней из описания")

    def _prompt_constructor(self, _):
        return f"Опиши песню '{self.task['song']}' артиста '{self.task['artist']}' из категории '{self.task['genre']}', расскажи интересный факт о песне. Используй смайлики и не более 150 слов."

    def __init__(self, task):
        self.task = task
        tagadder = TagAdder(['#меломан', '#музыка', '#иллюстрации', '#песни', f"#{task['genre']}" ])
        posters = [
            TelegramPoster(chat_id='@meloman_the', processor=tagadder),
            VkPoster(group_id='229821806', processor=tagadder),
            # InstagramPoster(account_token_name='MELOMAN_THE_TOKEN', account_id='28744401475175260', processor=tagadder)
            # TelegramPoster(processor=tagadder)
        ]
        super().__init__(posters)

def post(offset=0):
    start_date = datetime.date(2025, 7, 30)
    today = datetime.date.today()
    tasks = json.load(open("./files/meloman_the.json", "rt", encoding="UTF-8"))
    index = ((today - start_date).days + offset) % len(tasks)
    blogger = MelomanBlogger(tasks[index])
    blogger.post()

if __name__ == "__main__":
    post()