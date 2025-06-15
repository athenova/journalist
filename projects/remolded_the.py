from simple_blogger.blogger.auto import AutoSimpleBlogger
from simple_blogger.poster.telegram import TelegramPoster
from simple_blogger.poster.vk import VkPoster
from simple_blogger.preprocessor.text import TagAdder
from simple_blogger.generator import TextGenerator
from simple_blogger.generator.openai import GptImageGenerator
from datetime import date, timedelta

class SculptorBlogger(AutoSimpleBlogger):
    def _tasks_file_path(self):
        return f"./files/remolded_the.json"
    
    def _message_prompt_constructor(self, task):
        return f"{task['name']}({task['material']}), {task['author']}, {task['period']}. {task['description']}"
    
    def _message_generator(self):
        return TextGenerator("Ты - профессиональный скульптор")
    
    def _image_generator(self):
        return GptImageGenerator(api_key_name="GPT_API_KEY", style_prompt="Стиль - гиперреализм")

    def _image_prompt_constructor(self, task):
        return f"Нарисуй скульптуру '{task['name']}' автора '{task['author']}' выполненную в стиле {self.style[0]}"
        
    def _posters(self):
        tagadder = TagAdder(['#скульптуры', '#фантазии', '#шедевр', self.style[1]])
        return [
            TelegramPoster(chat_id='@remolded_the', processor=tagadder),
            VkPoster(group_id='230996135', processor=tagadder),
            # TelegramPoster(processor=tagadder),
        ]

    def __init__(self, posters=None, first_post_date=None, style=None):
        self.style = style
        super().__init__(posters=posters or self._posters(), first_post_date=first_post_date)

def post(offset=28):
    styles=[
        ( "Конструктивизм", "#Конструктивизм" ),
        ( "Постмодернизм", "#Постмодернизм" ),
        ( "Ар-нуво", "#Арнуво" ),
        ( "Абстрактный экспрессионизм", "#АбстрактныйЭкспрессионизм" ),
        ( "Античная скульптура", "#Античная" ),
        ( "Символизм", "#Символизм" ),
        ( "Неоклассицизм", "#Неоклассицизм" ),
        ( "Сюрреализм", "#Сюрреализм" ),
        ( "Барокко", "#Барокко" ),
        ( "Романтизм", "#Романтизм" ),
        ( "Ренессанс", "#Ренессанс" ),
        ( "Готическая скульптура", "#Готическая"),
        ( "Рококо", "#Рококо" ),
        ( "Минимализм", "#Минимализм" ),
        ( "Романская скульптура","#Романская" ),
        ( "Футуризм", "#Футуризм" ),
        ( "Кубизм", "#Кубизм" ),
        ( "Маньеризм", "#Маньеризм" ),
        ( "Реализм", "#Реализм" ),
    ]
    start_date = date(2025, 6, 15)-timedelta(days=offset)
    today = date.today()
    index = ((today - start_date).days + offset) % len(styles)
    blogger = SculptorBlogger(first_post_date=start_date, style=styles[index])
    blogger.post()

if __name__ == "__main__":
    post()