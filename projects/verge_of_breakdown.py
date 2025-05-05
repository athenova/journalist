from simple_blogger.blogger.auto import AutoSimpleBlogger
from simple_blogger.poster.telegram import TelegramPoster
from simple_blogger.poster.vk import VkPoster
from simple_blogger.preprocessor.text import TagAdder
from simple_blogger.generator.openai import OpenAiTextGenerator, OpenAiImageGenerator
from datetime import date

tagadder = TagAdder(['#pm', '#projectmanagement', '#it', '#ит', '#айти', '#проблемы', '#решения'])

class PmBlogger(AutoSimpleBlogger):
    def _tasks_file_path(self):
        return f"./files/verge_of_breakdown.json"
    
    def _system_prompt(self):
        return f"Ты - проектный менеджер, лидер проекта со 100% харизмой, всегда оптимистично настроенный и с отличным чувством юмора"
    
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
            TelegramPoster(chat_id='@verge_of_breakdown', processor=tagadder),
            VkPoster(group_id='229837997', processor=tagadder)
        ]

    def __init__(self, posters=None, first_post_date=date(2025, 3, 4)):
        super().__init__(posters=posters or self._posters(), first_post_date=first_post_date)

def post():
    blogger = PmBlogger()
    blogger.post()

if __name__ == "__main__":
    post()