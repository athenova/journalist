import json
from simple_blogger.blogger import Journalist
from simple_blogger.poster.telegram import TelegramPoster
from simple_blogger.poster.vk import VkPoster
from simple_blogger.poster.instagram import InstagramPoster
from simple_blogger.preprocessor.text import TagAdder
from datetime import date, timedelta

class HistorianBlogger(Journalist):
    
    def _system_prompt(self):
        return "Ты - историк. Я дам тебе одну из пар: спортсмен-рекорд, изобретатель-изобретение, физик-открытие, химик-открытие, путешественник-открытие, философ-открытие, математик-открытие. Расскажи инетересный факт, связанный с этой парой, используй смайлики и не более 150 слов. Не используй 'Окей' и 'Конечно'"
    
    def _prompt_constructor(self, _):
        return f"{self.task['author']} - {self.task['invention']}"

    def __init__(self, task):
        self.task = task
        tagadder = TagAdder(['#первые', '#лучшие', '#ДоЭтогоНикто'])
        posters = [
            TelegramPoster(chat_id='@no_one_before', processor=tagadder),
            VkPoster(group_id='229838140', processor=tagadder),
            InstagramPoster(account_token_name='NOONE_BEFORE_TOKEN', account_id='9635201363189685', processor=tagadder)
            # TelegramPoster(processor=tagadder)
        ]
        super().__init__(posters)


def post(offset=0):
    tasks = json.load(open("./files/no_one_before.json", "rt", encoding="UTF-8"))
    start_date = date(2025, 6, 25)-timedelta(days=offset)
    today = date.today()
    index = ((today - start_date).days + offset) % len(tasks)
    blogger = HistorianBlogger(tasks[index])
    blogger.post()

if __name__ == "__main__":
    post()
