from simple_blogger.blogger.auto import AutoSimpleBlogger
from simple_blogger.poster.telegram import TelegramPoster
from simple_blogger.poster.vk import VkPoster
from simple_blogger.poster.instagram import InstagramPoster
from simple_blogger.preprocessor.text import TagAdder
from datetime import date

tagadder = TagAdder(['#вмиреживотных', '#животныймир'])

class AnimalBlogger(AutoSimpleBlogger):
    def _tasks_file_path(self):
        return f"./files/cats_and_beasts.json"
    
    def _system_prompt(self):
        return "Ты - специалист по животным, блоггер с 1000000 подписчиков, умеющий заинтересовать аудиторию в изучении животного мира"
    
    def _message_prompt_constructor(self, task):
        return f"Расскажи интересный факт о животном породы '{task['species']}' из рода '{task['genus']}' семейства '{task['family']}', используй не более 100 слов"
    
    def _image_prompt_constructor(self, task):
        return f"Нарисуй животное породы '{task['species']}' из рода '{task['genus']}' семейства '{task['family']}'. Эстетично, красиво, реалистично, крупным планом"
        
    def _posters(self):
        return [
            TelegramPoster(chat_id='@cats_and_beasts', processor=tagadder),
            VkPoster(group_id='229821868', processor=tagadder),
            # InstagramPoster(account_token_name='CATS_AND_BEASTS_TOKEN', account_id='10002961023067113', processor=tagadder)
        ]

    def __init__(self, posters=None, first_post_date=date(2025, 3, 11)):
        super().__init__(posters=posters or self._posters(), first_post_date=first_post_date)

def post():
    blogger = AnimalBlogger()
    blogger.post()

if __name__ == "__main__":
    post()