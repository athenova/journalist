from simple_blogger.poster.telegram import TelegramPoster
from simple_blogger.poster.vk import VkPoster
from simple_blogger.blogger import Journalist
from simple_blogger.preprocessor.text import TagAdder
from simple_blogger.generator.openai import GptImageGenerator
from simple_blogger.generator.deepseek import DeepSeekTextGenerator
from simple_blogger.generator.yandex import YandexImageGenerator
from datetime import date
import json

class LegendaryWriterBlogger(Journalist):
    def _message_generator(self):
        # return OpenAiTextGenerator("Я дам тебе имя известного граффити-райтера. Приведи интересный факт, связанный с ним. Используй смайлики и не более 150 слов. Не используй 'Окей' и 'Конечно'")
        return DeepSeekTextGenerator("Я дам тебе имя известного граффити-райтера. Приведи интересный факт, связанный с ним. Используй смайлики и не более 150 слов. Не используй 'Окей' и 'Конечно'")
    
    def _image_generator(self):
        # return GptImageGenerator(api_key_name="GPT_API_KEY", system_prompt="Нарисуй граффити-райтера из описания")
        return YandexImageGenerator(system_prompt="Нарисуй граффити-райтера из описания")
    
    def _prompt_constructor(self, _):
        return self.task["writer"]

    def __init__(self, task):
        self.task = task
        tagadder = TagAdder(['#граффити', '#трибьют', '#легенды'])
        posters = [
            TelegramPoster(chat_id='@zaborgram', processor=tagadder),
            VkPoster(group_id='231425969', processor=tagadder)
            # TelegramPoster(processor=tagadder)
        ]
        super().__init__(posters)

def post(offset=0):
    tasks = json.load(open("./files/legendary/legendary_writer.json", "rt", encoding="UTF-8"))
    start_date = date(2025, 8, 3)
    today = date.today()
    index = ((today - start_date).days // 7 + offset) % len(tasks)
    blogger = LegendaryWriterBlogger(tasks[index])
    blogger.post()

if __name__ == "__main__":
    post()