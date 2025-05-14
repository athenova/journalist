from simple_blogger.blogger.auto import AutoSimpleBlogger
from simple_blogger.poster.telegram import TelegramPoster
from simple_blogger.poster.vk import VkPoster
from simple_blogger.preprocessor.text import TagAdder
from simple_blogger.generator import TextGenerator
from simple_blogger.generator.openai import GptImageGenerator
from datetime import date

tagadder = TagAdder(['#иллюстрации', '#фантазии'])

class MasterpieceBlogger(AutoSimpleBlogger):
    def _tasks_file_path(self):
        return f"./files/masterpiece_the.json"
    
    def _message_prompt_constructor(self, task):
        return f"{task['name']}, {task['author']}, {task['period']}. {task['location']}, {task['description']}"
    
    def _message_generator(self):
        return TextGenerator("Ты - профессиональный искусствовед")
    
    def _image_generator(self):
        return GptImageGenerator(api_key_name="GPT_API_KEY")

    def _image_prompt_constructor(self, task):
        return f"Нарисуй картину '{task['name']}' автора '{task['author']}' в стиле {self.style}"
        
    def _posters(self):
        return [
            TelegramPoster(chat_id='@masterpiece_the', processor=tagadder),
            VkPoster(group_id='229902850', processor=tagadder),
            # TelegramPoster(processor=tagadder),
        ]

    def __init__(self, posters=None, first_post_date=date(2025, 5, 14), style=None):
        self.style = style
        super().__init__(posters=posters or self._posters(), first_post_date=first_post_date)

def post(offset=0):
    styles=[
        "Концептуальное искусство"
        "Поп-арт",
        "Абстрактный экспрессионизм",
        "Сюрреализм",
        "Дадаизм",
        "Супрематизм",
        "Футуризм",
        "Кубизм",
        "Экспрессионизм",
        "Фовизм",
        "Модерн (Ар-нуво)",
        "Постимпрессионизм",
        "Импрессионизм",
        "Реализм",
        "Романтизм",
        "Классицизм",
        "Рококо",
        "Барокко",
        "Ренессанс",
        "Готика",
        "Византийский",
        "Античная живопись",
    ]
    start_date = date(2025, 5, 14)
    today = date.today()
    index = ((today - start_date).days + offset) % len(styles)
    blogger = MasterpieceBlogger(first_post_date=start_date, style=styles[index])
    blogger.post()

if __name__ == "__main__":
    post()