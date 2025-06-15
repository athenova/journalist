from simple_blogger.poster.telegram import TelegramPoster
from simple_blogger.poster.vk import VkPoster
from simple_blogger.blogger import Journalist
from simple_blogger.preprocessor.text import TagAdder
from simple_blogger.generator.openai import OpenAiTextGenerator, GptImageGenerator
from simple_blogger.generator.yandex import YandexTextGenerator, YandexImageGenerator
from datetime import date, timedelta

class LegendarySculptor(Journalist):
    def _message_generator(self):
        return OpenAiTextGenerator("Ты - искусствовед-историк. Я дам тебе стиль в искусстве. Выбери известного скульптора, который творил в этом стиле, приведи интерсный факт, связанный с этим скульптором. Используй не более 150 слов. Не используй 'Окей' и 'Конечно'")
        # return YandexTextGenerator("Ты - искусствовед-историк. Я дам тебе стиль в искусстве. Выбери известного скульптора, который творил в этом стиле, приведи интерсный факт, связанный с этим скульптором. Используй не более 150 слов. Не используй 'Окей' и 'Конечно'")
    
    def _image_generator(self):
        return GptImageGenerator(api_key_name="GPT_API_KEY", system_prompt="Нарисуй скульптора из описания")
        # return YandexImageGenerator(system_prompt="Нарисуй скульптора из описания")

    def _prompt_constructor(self, _):
        return self.style[0]

    def __init__(self, style):
        self.style = style
        tagadder = TagAdder(['#скульптор', '#великий', self.style[1]])
        posters = [
            TelegramPoster(chat_id='@remolded_the', processor=tagadder),
            VkPoster(group_id='230996135', processor=tagadder)
            # TelegramPoster(processor=tagadder)
        ]
        super().__init__(posters)


def post(offset=0):
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
    start_date = date(2025, 6, 22)-timedelta(days=offset)
    today = date.today()
    index = ((today - start_date).days // 7 + offset) % len(styles)
    blogger = LegendarySculptor(style=styles[index])
    blogger.post()

if __name__ == "__main__":
    post()