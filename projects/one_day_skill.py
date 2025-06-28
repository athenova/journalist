from simple_blogger.blogger.auto import AutoSimpleBlogger
from simple_blogger.poster.telegram import TelegramPoster
from simple_blogger.poster.vk import VkPoster
from simple_blogger.poster.instagram import InstagramPoster
from simple_blogger.preprocessor.text import TagAdder
from simple_blogger.generator.openai import OpenAiTextGenerator, OpenAiImageGenerator
from datetime import date

tagadder = TagAdder(['#скилы', '#развитие'])

class SkillBlogger(AutoSimpleBlogger):
    def _tasks_file_path(self):
        return f"./files/one_day_skill.json"
    
    def _message_prompt_constructor(self, task):
        return f"Расскажи как {task['name']}, используй не более 100 слов, используй смайлики"
    
    def _image_prompt_constructor(self, task):
        return f"Нарисуй рисунок, вдохновлённый темой '{task['name']}'"
        
    def _message_generator(self):
        return OpenAiTextGenerator(self._system_prompt())
    
    def _image_generator(self):
        return OpenAiImageGenerator()
    
    def _posters(self):
        return [
            TelegramPoster(chat_id='@one_day_skill', processor=tagadder),
            VkPoster(group_id='229822298', processor=tagadder),
            # InstagramPoster(account_token_name='ONE_DAY_SKILL_TOKEN', account_id='9799308313442110', processor=tagadder)
        ]

    def __init__(self, posters=None):
        super().__init__(posters=posters or self._posters(), first_post_date=date(2025, 3, 16))

def post():
    blogger = SkillBlogger()
    blogger.post()

if __name__ == "__main__":
    post()