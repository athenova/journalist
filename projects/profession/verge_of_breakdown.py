from simple_blogger.poster.telegram import TelegramPoster
from simple_blogger.poster.instagram import InstagramPoster
from simple_blogger.poster.vk import VkPoster
from simple_blogger.blogger import Journalist
from simple_blogger.preprocessor.text import TagAdder
from simple_blogger.generator.openai import OpenAiTextGenerator, OpenAiImageGenerator
from simple_blogger.generator.yandex import YandexImageGenerator, YandexTextGenerator
import datetime, json

class PmBlogger(Journalist):
    def _message_generator(self):
        return OpenAiTextGenerator('Ты - проектный менеджер, лидер проекта со 100% харизмой, всегда оптимистично настроенный и с отличным чувством юмора')
        # return YandexTextGenerator('Ты - проектный менеджер, лидер проекта со 100% харизмой, всегда оптимистично настроенный и с отличным чувством юмора')
    
    def _image_generator(self):
        # return YandexImageGenerator(style_prompt='Нарисуй рисунок, вдохновлённый проблемой из описания. Не рисуй текст')
        return OpenAiImageGenerator(system_prompt="Нарисуй рисунок, вдохновлённый проблемой из описания. Не рисуй текст")

    def _prompt_constructor(self, _):
        return f"Опиши проблему '{self.task['problem']}' из категории '{self.task['category']}', выбери метод решения, опиши метод решения, используй смайлики, используй менее 100 слов"

    def __init__(self, task):
        self.task = task
        tagadder = TagAdder(['#pm', '#projectmanagement', '#it', '#ит', '#айти', '#проблемы', '#решения', f"#{task['category']}"])
        posters = [
            TelegramPoster(chat_id='-1002360664560', processor=tagadder),
            VkPoster(group_id='229837997', processor=tagadder),
            # TelegramPoster(processor=tagadder)
        ]
        super().__init__(posters)

def post(offset=0):
    start_date = datetime.date(2025, 8, 7)
    today = datetime.date.today()
    tasks = json.load(open("./files/profession/verge_of_breakdown.json", "rt", encoding="UTF-8"))
    index = ((today - start_date).days + offset) % len(tasks)
    blogger = PmBlogger(tasks[index])
    blogger.post()

if __name__ == "__main__":
    post()