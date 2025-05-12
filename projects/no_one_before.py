from simple_blogger.poster.telegram import TelegramPoster
from simple_blogger.poster.instagram import InstagramPoster
from simple_blogger.poster.vk import VkPoster
from simple_blogger.blogger import Journalist
from simple_blogger.preprocessor.text import TagAdder
from simple_blogger.generator.openai import OpenAiTextGenerator
import datetime

class HistoricBlogger(Journalist):
    # def _system_prompt(self):
    #     return self.system_prompt

    def _message_generator(self):
        return OpenAiTextGenerator(self.system_prompt)
    
    def _prompt_constructor(self, _):
        return self.prompt_constructor

    def __init__(self, system_prompt, prompt_constructor, tags):
        self.system_prompt = system_prompt
        self.prompt_constructor = prompt_constructor
        tagadder = TagAdder(tags)
        posters = [
            TelegramPoster(chat_id='@no_one_before', processor=tagadder),
            VkPoster(group_id='229838140', processor=tagadder),
            InstagramPoster(account_token_name='NOONE_BEFORE_TOKEN', account_id='9635201363189685', processor=tagadder)
            # TelegramPoster(processor=tagadder)
        ]
        super().__init__(posters)

def post(day=None):
    match day or datetime.date.today().weekday():
        case 0:
            blogger = HistoricBlogger(
                "Ты - историк спорта", 
                "Выбери рандомный вид спорта. Расскажи про один спортивный рекорд этого вида спорта и о том, кто его поставил. Используй смайлики и не более 150 слов. Не используй 'Окей' и 'Конечно'",
                ['#рекорды', '#первые', '#спорт', '#лучшие']
            )
        case 1:
            blogger = HistoricBlogger(
                "Ты - историк изобретений", 
                "Расскажи про одно рандомное техническое изобретение и о том, кто его изобрёл. Используй смайлики и не более 150 слов. Не используй 'Окей' и 'Конечно'",
                ['#изобретения', '#первые', '#творчество', '#лучшие']
            )
        case 2:
            blogger = HistoricBlogger(
                "Ты - научный историк", 
                "Расскажи про одно рандомное физическое открытие и о том, кто его открыл. Используй смайлики и не более 150 слов. Не используй 'Окей' и 'Конечно'",
                ['#открытия', '#первые', '#наука', '#лучшие']
            )
        case 3:
            blogger = HistoricBlogger(
                "Ты - географический историк", 
                "Расскажи про одно рандомное географическое открытие и о том, кто его открыл. Используй смайлики и не более 150 слов. Не используй 'Окей' и 'Конечно'",
                ['#открытия', '#первые', '#география', '#лучшие']
            )
        case 4:
            blogger = HistoricBlogger(
                "Ты - научный историк", 
                "Расскажи про одно рандомное химическое открытие и о том, кто его открыл. Используй смайлики и не более 150 слов. Не используй 'Окей' и 'Конечно'",
                ['#открытия', '#первые', '#наука', '#лучшие']
            )
        case 5:
            blogger = HistoricBlogger(
                "Ты - философ-историк", 
                "Расскажи про одно рандомное философское открытие и о том, кто его открыл. Используй смайлики и не более 150 слов. Не используй 'Окей' и 'Конечно'",
                ['#открытия', '#первые', '#философия', '#лучшие']
            )
        case 6:
            blogger = HistoricBlogger(
                "Ты - историк", 
                "Расскажи про одно рандомное российское достижение и о том, кто его достиг. Используй смайлики и не более 150 слов. Не используй 'Окей' и 'Конечно'",
                ['#достижения', '#первые', '#россия', '#лучшие']
            )
    blogger.post()

if __name__ == "__main__":
    post()