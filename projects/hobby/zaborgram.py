from simple_blogger.poster.telegram import TelegramPoster
from simple_blogger.poster.instagram import InstagramPoster
from simple_blogger.poster.vk import VkPoster
from simple_blogger.blogger import Journalist
from simple_blogger.preprocessor.text import TagAdder
from simple_blogger.generator.openai import OpenAiTextGenerator, GptImageGenerator
from simple_blogger.generator.deepseek import DeepSeekTextGenerator
from simple_blogger.generator.yandex import YandexImageGenerator
import datetime, json

class WriterBlogger(Journalist):
    def _message_generator(self):
        return OpenAiTextGenerator('Ты - граффити-райтер')
        # return DeepSeekTextGenerator('Ты - граффити-райтер')
    
    def _image_generator(self):
        # return GptImageGenerator(api_key_name="GPT_API_KEY", system_prompt="Нарисуй граффити, вдохновлённое описанием")
        return YandexImageGenerator(system_prompt="Нарисуй граффити, вдохновлённое описанием")
    
    def _prompt_constructor(self, _):
        return f"Опиши граффити '{self.task['graf']}' райтера {self.task['artist']}, используй не более 100 слов, используй смайлики и не более 150 слов, не используй 'Конечно' и 'Okей'"

    def __init__(self, task):
        self.task = task
        tagadder = TagAdder(['#граффити', '#трибьют', f"#{task['genre']}"])
        posters = [
            TelegramPoster(chat_id='@zaborgram', processor=tagadder),
            VkPoster(group_id='231425969', processor=tagadder),
            # InstagramPoster(account_token_name='ILLUSTRATOR_THE_TOKEN', account_id='9351594524905971', processor=tagadder)
            # TelegramPoster(processor=tagadder)
        ]
        super().__init__(posters)

def post():
    start_day = datetime.date(2025, 8, 3)
    today = datetime.date.today()
    day_count = int((today - start_day).days // 3.5)
    tasks = json.load(open("./files/hobby/zaborgram.json", "rt", encoding="UTF-8"))
    index = day_count % len(tasks)
    task = tasks[index]

    blogger = WriterBlogger(task)
    blogger.post()

if __name__ == "__main__":
    post()