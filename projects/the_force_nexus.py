from simple_blogger.blogger.auto import AutoSimpleBlogger
from simple_blogger.poster.telegram import TelegramPoster
from simple_blogger.poster.vk import VkPoster
from simple_blogger.poster.instagram import InstagramPoster
from simple_blogger.preprocessor.text import TagAdder
from simple_blogger.generator.openai import OpenAiTextGenerator, OpenAiImageGenerator
from datetime import date

tagadder = TagAdder(['#местосилы', '#тайное'])

class ForceNexusBlogger(AutoSimpleBlogger):
    def _tasks_file_path(self):
        return f"./files/the_force_nexus.json"
    
    def _system_prompt(self):
        return "Ты - блогер-эзотерик с 1000000 подписчиков"
    
    def _message_prompt_constructor(self, task):
        return f"Расскажи интересный факт про {task['name']}, который находятся в {task['location']} {task['country']}, используй не более 100 слов, используй смайлики"
    
    def _image_prompt_constructor(self, task):
        return f"Нарисуй {task['name']}, который находятся в {task['location']} {task['country']}"
    
    def _message_generator(self):
        return OpenAiTextGenerator(self._system_prompt())
    
    def _image_generator(self):
        return OpenAiImageGenerator()
        
    def _posters(self):
        return [
            TelegramPoster(chat_id='@the_force_nexus', processor=tagadder),
            VkPoster(group_id='229821912', processor=tagadder),
            InstagramPoster(account_token_name='FORCE_NEXUS_THE_TOKEN', account_id='9642947449081447', processor=tagadder)
        ]

    def __init__(self, posters=None, first_post_date=date(2025, 2, 24), force_rebuild=False):
        super().__init__(posters=posters or self._posters(), first_post_date=first_post_date, force_rebuild=force_rebuild)

def post():
    blogger = ForceNexusBlogger()
    blogger.post()

if __name__ == "__main__":
    post()