from simple_blogger.poster.telegram import TelegramPoster
from simple_blogger.poster.vk import VkPoster
from simple_blogger.blogger import Journalist
from simple_blogger.preprocessor.text import TagAdder
from simple_blogger.generator.openai import OpenAiTextGenerator, GptImageGenerator
from simple_blogger.generator.yandex import YandexTextGenerator, YandexImageGenerator
from datetime import date, timedelta

class LegendaryArtist(Journalist):
    def _message_generator(self):
        return OpenAiTextGenerator("Ты - искусствовед-историк. Я дам тебе стиль в искусстве. Выбери известного художника, рисовавшего в этом стиле, приведи интерсный факт, связанный с этим художником. Используй не более 150 слов. Не используй 'Окей' и 'Конечно'")
        # return YandexTextGenerator("Ты - искусствовед-историк. Я дам тебе стиль в искусстве. Выбери известного художника, рисовавшего в этом стиле, приведи интерсный факт, связанный с этим художником. Используй не более 150 слов. Не используй 'Окей' и 'Конечно'")
    
    def _image_generator(self):
        return GptImageGenerator(api_key_name="GPT_API_KEY", system_prompt="Нарисуй художника из описания")
        # return YandexImageGenerator(system_prompt="Нарисуй художника из описания")

    def _prompt_constructor(self, _):
        return self.style[0]

    def __init__(self, style):
        self.style = style
        tagadder = TagAdder(['#художник', '#великий', self.style[1]])
        posters = [
            TelegramPoster(chat_id='@masterpiece_the', processor=tagadder),
            VkPoster(group_id='229902850', processor=tagadder)
            # TelegramPoster(processor=tagadder)
        ]
        super().__init__(posters)


def post(offset=0):
    styles=[
        ("Концептуальное искусство", "#концептуальное"),
        ("Поп-арт", "#попарт"),
        ("Абстрактный экспрессионизм", "#абстрактныйэкспрессионизм"),
        ("Сюрреализм", "#сюрреализм"),
        ("Дадаизм", "#дадаизм"),
        ("Супрематизм", "#супрематизм"),
        ("Футуризм", "#футуризм"),
        ("Кубизм", "#кубизм"),
        ("Экспрессионизм", "#экспрессионизм"),
        ("Фовизм", "#фовизм"),
        ("Модерн (Ар-нуво)", "#модерн"),
        ("Постимпрессионизм", "#постимпрессионизм"),
        ("Импрессионизм", "#импрессионизм"),
        ("Реализм", "#реализм"),
        ("Романтизм", "#романтизм"),
        ("Классицизм", "#классицизм"),
        ("Рококо", "#рококо"),
        ("Барокко", "#барокко"),
        ("Ренессанс", "#ренессанс"),
        ("Готика", "#готика"),
        ("Византийский", "#византийский"),
        ("Античная живопись", "#античнаяживопись"),
    ]
    start_date = date(2025, 6, 15)-timedelta(days=offset)
    today = date.today()
    index = ((today - start_date).days // 7 + offset) % len(styles)
    blogger = LegendaryArtist(style=styles[index])
    blogger.post()

if __name__ == "__main__":
    post()