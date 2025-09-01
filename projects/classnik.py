import array, json
from simple_blogger.poster.telegram import TelegramPoster
from simple_blogger.poster.vk import VkPoster
from simple_blogger.blogger import Journalist
from simple_blogger.preprocessor.text import TagAdder
from simple_blogger.generator.openai import OpenAiTextGenerator, OpenAiImageGenerator
from simple_blogger.generator.yandex import YandexImageGenerator, YandexTextGenerator
from simple_blogger.generator.deepseek import DeepSeekTextGenerator
from datetime import date, timedelta

class SchoolBlogger(Journalist):
    def _message_generator(self):
        return YandexTextGenerator("Ты - блоггер с 1000000 подписчиков, целевая аудитория - 13 лет, используешь в разговоре сленг и смайлики. Я дам тебе школьный предмет и тему. Расскажи интересный факт по данной теме. Используй не более 200 слов. Не используй 'Окей' и 'Конечно'")
        # return DeepSeekTextGenerator("Ты - блоггер с 1000000 подписчиков, целевая аудитория - 13 лет, используешь в разговоре сленг и смайлики. Я дам тебе школьный предмет и тему. Расскажи интересный факт по данной теме. Используй не более 200 слов. Не используй 'Окей' и 'Конечно'")
    
    def _prompt_constructor(self, _):
        return f"{self.task["category"]}, {self.task["topic"]}"
    
    def _image_generator(self):
        # return OpenAiImageGenerator(system_prompt="Нарисуй картинку, вдохновлённую описанием")
        return YandexImageGenerator(system_prompt="Нарисуй картинку, вдохновлённую описанием")

    def __init__(self, path: str, post_days: array.array):
        today = date.today()
        start_date = date(2025, 9, 1)
        # start_date = date(2025, 8, 18)
        week =  (today - start_date).days // 7
        weekday_index = post_days.index(today.weekday() + 1)
        index = week * len(post_days) + weekday_index
        tasks = json.load(open(f"./files/class6nik/{path}.json", "rt", encoding="UTF-8"))
        self.task = tasks[index]
        tagadder = TagAdder(['#школа', '#6класс', '#учёба', f"#{self.task["category"].replace(' ', '')}".lower()])
        posters = [
            TelegramPoster(chat_id='@class5nik', processor=tagadder),
            VkPoster(group_id='229821544', processor=tagadder),
            # TelegramPoster(processor=tagadder)
        ]
        super().__init__(posters)

def post(index='bio1'):
    try:
        post_days = None
        match index:
            case "bio1" | "bio3" | "bio3" | "bio4" : post_days = [2]
            case "ru_history1" | "ru_history3" | "ru_history3" | "ru_history4" : post_days = [1]
            case "history1" | "history2" | "history3" | "history4" : post_days = [5]
            case "math1" | "math2" | "math3" | "math4" : post_days = [2, 4]
            case "litra1" | "litra2" : post_days = [1, 3, 5]
            case "litra3" | "litra4" : post_days = [1, 5]
            case "rus1" | "rus2" : post_days = [1, 2, 3, 4]
            case "rus3" | "rus4" : post_days = [1, 3, 5]
            case _: raise ValueError("Index not found")
        blogger = SchoolBlogger(path=index, post_days=post_days)
        blogger.post()
    except ValueError:
        pass

if __name__ == "__main__":
    post('rus4')