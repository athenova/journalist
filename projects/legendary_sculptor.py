from simple_blogger.poster.telegram import TelegramPoster
from simple_blogger.poster.vk import VkPoster
from simple_blogger.blogger import Journalist
from simple_blogger.preprocessor.text import TagAdder
from simple_blogger.generator.openai import OpenAiTextGenerator, GptImageGenerator
from simple_blogger.generator.yandex import YandexTextGenerator, YandexImageGenerator
from datetime import date, timedelta
import json

class LegendarySculptor(Journalist):
    def _message_generator(self):
        return OpenAiTextGenerator("Ты - искусствовед-историк. Я дам тебе известного скульптора и стиль его искусства, приведи интерсный факт, связанный с этим скульптором. Используй не более 150 слов. Не используй 'Окей' и 'Конечно'")
        # return YandexTextGenerator("Ты - искусствовед-историк. Я дам тебе известного скульптора и стиль его искусства, приведи интерсный факт, связанный с этим скульптором. Используй не более 150 слов. Не используй 'Окей' и 'Конечно'")
    
    def _image_generator(self):
        return GptImageGenerator(api_key_name="GPT_API_KEY", system_prompt="Нарисуй скульптуру, посвящённую скульптору из описания", style_prompt=f"Стиль - гиперреализм, {self.task['genre']}")
        # return YandexImageGenerator(system_prompt="Нарисуй скульптуру, посвящённую скульптору из описания", style_prompt=f"Стиль - гиперреализм, {self.task['genre']}")

    def _prompt_constructor(self, _):
        return f"{self.task['sculptor']}, {self.task['genre']}"

    def __init__(self, task):
        self.task = task
        tagadder = TagAdder(['#скульптор', '#великий', f"#{task['genre']}"])
        posters = [
            TelegramPoster(chat_id='@remolded_the', processor=tagadder),
            VkPoster(group_id='230996135', processor=tagadder)
            # TelegramPoster(processor=tagadder)
        ]
        super().__init__(posters)


def post(offset=0):
    tasks = json.load(open("./files/legendary_sculptor.json", "rt", encoding="UTF-8"))
    start_date = date(2025, 8, 3)
    today = date.today()
    index = ((today - start_date).days // 7 + offset) % len(tasks)
    blogger = LegendarySculptor(tasks[index])
    blogger.post()

if __name__ == "__main__":
    post()