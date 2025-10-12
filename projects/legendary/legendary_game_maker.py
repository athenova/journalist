from simple_blogger.poster.telegram import TelegramPoster
from simple_blogger.poster.vk import VkPoster
from simple_blogger.blogger import Journalist
from simple_blogger.preprocessor.text import TagAdder
from simple_blogger.generator.openai import OpenAiTextGenerator
from simple_blogger.generator.deepseek import DeepSeekTextGenerator
from datetime import date, timedelta
import json

class LegendaryGameBlogger(Journalist):
    def _message_generator(self):
        return OpenAiTextGenerator("Я дам тебе имя известного человека из игровой индустрии, профессию и его ключевую игру. Приведи интересный факт, связанный с ним. Используй смайлики и не более 150 слов. Не используй 'Окей' и 'Конечно'")
        # return DeepSeekTextGenerator("Я дам тебе имя известного человека из игровой индустрии, профессию и его ключевую игру. Приведи интересный факт, связанный с ним. Используй смайлики и не более 150 слов. Не используй 'Окей' и 'Конечно'")
    
    def _prompt_constructor(self, _):
        return f"{self.task["person"]}, {self.task["profession"]}, {self.task["game"]}"

    def __init__(self, task):
        self.task = task
        tagadder = TagAdder(['#геймер', '#игры', '#знаменитости', f"#{task["profession"]}"])
        posters = [
            TelegramPoster(chat_id='@venatus_the', processor=tagadder),
            VkPoster(group_id='230445524', processor=tagadder),
            # TelegramPoster(processor=tagadder)
        ]
        super().__init__(posters)

def post(offset=0):
    tasks = json.load(open("./files/legendary/legendary_game_maker.json", "rt", encoding="UTF-8"))
    start_date = date(2025, 8, 3)
    today = date.today()
    index = ((today - start_date).days // 7 + offset) % len(tasks)
    blogger = LegendaryGameBlogger(tasks[index])
    blogger.post()

if __name__ == "__main__":
    post()