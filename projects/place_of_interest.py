from simple_blogger.blogger.auto import AutoSimpleBlogger
from simple_blogger.poster.telegram import TelegramPoster
from simple_blogger.poster.vk import VkPoster
from simple_blogger.poster.instagram import InstagramPoster
from simple_blogger.preprocessor.text import TagAdder
from simple_blogger.generator.openai import OpenAiTextGenerator, OpenAiImageGenerator
from datetime import date

tagadder = TagAdder(['#путешествия', '#достопримечательности', '#города', '#страны'])

class AdventurerBlogger(AutoSimpleBlogger):
    def _tasks_file_path(self):
        return f"./files/place_of_interest.json"
    
    def _system_prompt(self):
        return f"Ты - блогер с 1000000 миллионном подписчиков"
    
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
            TelegramPoster(chat_id='@place_of_interest', processor=tagadder),
            VkPoster(group_id='229821893', processor=tagadder),
            # InstagramPoster(account_token_name='PLACE_OF_INTEREST_THE_TOKEN', account_id='28685424414437375', processor=tagadder)
        ]

    def __init__(self, posters=None, first_post_date=date(2025, 2, 23)):
        super().__init__(posters=posters or self._posters(), first_post_date=first_post_date)

def post():
    blogger = AdventurerBlogger()
    blogger.post()

def init():
    blogger = AdventurerBlogger()
    blogger.init_project()

def make_tasks():
    blogger = AdventurerBlogger()
    blogger.create_auto_tasks(day_offset=-53)

if __name__ == "__main__":
    post()