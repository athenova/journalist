from simple_blogger.blogger.auto import AutoSimpleBlogger
from simple_blogger.poster.telegram import TelegramPoster
from simple_blogger.poster.vk import VkPoster
from simple_blogger.preprocessor.text import TagAdder
from simple_blogger.generator.openai import OpenAiTextGenerator, OpenAiImageGenerator
from datetime import date

tagadder = TagAdder(['#hr', '#кадры', '#it', '#ит', '#айти', '#проблемы', '#решения'])

class HrBlogger(AutoSimpleBlogger):
    def _tasks_file_path(self):
        return f"./files/coffee_and_nerves.json"
    
    def _system_prompt(self):
        return 'Ты - руководитель HR, лидер команды со 100% харизмой, всегда оптимистично настроенный и с отличным чувством юмора'
    
    def _message_prompt_constructor(self, task):
        return f"Выбери рандомно актуальную проблему по теме '{task['topic']}' из области '{task['category']}', опиши проблему, как если бы рассказывал подруге, выбери рандомно метод решения, опиши метод решения, используй смайлики, используй менее 100 слов"
    
    def _image_prompt_constructor(self, task):
        return f"Нарисуй картинку, вдохновлённую темой '{task['topic']}' из области '{task['category']}'"
    
    def _message_generator(self):
        return OpenAiTextGenerator(self._system_prompt())
    
    def _image_generator(self):
        return OpenAiImageGenerator()
        
    def _posters(self):
        return [
            TelegramPoster(chat_id='@coffee_and_nerves', processor=tagadder),
            VkPoster(group_id='229838019', processor=tagadder)
        ]

    def __init__(self, posters=None, first_post_date=date(2025, 3, 6)):
        super().__init__(posters or self._posters(), first_post_date)

def post():
    blogger = HrBlogger()
    blogger.post()

if __name__ == "__main__":
    post()