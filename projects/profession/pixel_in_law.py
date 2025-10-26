from simple_blogger.blogger.auto import AutoSimpleBlogger
from simple_blogger.poster.telegram import TelegramPoster
from simple_blogger.poster.vk import VkPoster
from simple_blogger.preprocessor.text import TagAdder
from simple_blogger.generator.deepseek import DeepSeekTextGenerator
from datetime import date

tagadder = TagAdder(['#design', '#шрифты', '#правик', '#креатив', '#макеты', '#проблемы', '#решения'])

class Designer(AutoSimpleBlogger):
    def _tasks_file_path(self):
        return f"./files/profession/pixel_in_law.json"
    
    def _system_prompt(self):
        return f"Ты - профессиональный дизайнер, лидер команды со 100% харизмой, всегда оптимистично настроенный и с отличным чувством юмора"
    
    def _message_prompt_constructor(self, task):
        return f"Выбери рандомно актуальную проблему по теме '{task['topic']}' из области '{task['category']}', опиши проблему, выбери рандомно метод решения, опиши метод решения, используй смайлики, используй менее 100 слов"
    
    def _image_prompt_constructor(self, task):
        return f"Нарисуй картинку, вдохновлённую темой '{task['topic']}' из области '{task['category']}'"
    
    def _message_generator(self):
        return DeepSeekTextGenerator(self._system_prompt())
    
    def _posters(self):
        return [
            # TelegramPoster(chat_id='-1002633483480', processor=tagadder),
            # VkPoster(group_id='230335670', processor=tagadder),
            TelegramPoster(processor=tagadder)
        ]

    def __init__(self, posters=None, first_post_date=date(2025, 5, 2)):
        super().__init__(posters=posters or self._posters(), first_post_date=first_post_date)

def post():
    blogger = Designer()
    blogger.post()

if __name__ == "__main__":
    post()