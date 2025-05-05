from simple_blogger.blogger.auto import AutoSimpleBlogger
from simple_blogger.poster.telegram import TelegramPoster
from simple_blogger.poster.vk import VkPoster
from simple_blogger.poster.instagram import InstagramPoster
from simple_blogger.preprocessor.text import TagAdder
from simple_blogger.generator.openai import OpenAiTextGenerator, OpenAiImageGenerator
from datetime import date

tagadder = TagAdder(['#гармония', '#светвнутри', '#саморазвитие', '#личностныйрост', '#отношения'])

class LuxNexusBlogger(AutoSimpleBlogger):
    def _tasks_file_path(self):
        return f"./files/lux_nexus.json"
    
    def _message_prompt_constructor(self, task):
        return f"Выбери рандомно актуальную проблему по теме '{task['topic']}' из области '{task['category']}', опиши проблему, выбери рандомно метод решения, опиши метод решения, используй смайлики, используй менее 100 слов"
    
    def _image_prompt_constructor(self, task):
        return f"Нарисуй картинку, вдохновлённую темой '{task['topic']}' из области '{task['category']}'"
    
    def _message_generator(self):
        return OpenAiTextGenerator(self._system_prompt())
    
    def _image_generator(self):
        return OpenAiImageGenerator()
        
    def _posters(self):
        return [
            TelegramPoster(chat_id='@lux_nexus', processor=tagadder),
            VkPoster(group_id='229822258', processor=tagadder),
            InstagramPoster(account_token_name='LUX_NEXUS_TOKEN', account_id='9267090153358407', processor=tagadder)
        ]

    def __init__(self, posters=None, first_post_date=date(2025, 3, 4)):
        super().__init__(posters=posters or self._posters(), first_post_date=first_post_date)

def post():
    blogger = LuxNexusBlogger()
    blogger.post()

if __name__ == "__main__":
    post()