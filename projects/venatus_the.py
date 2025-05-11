from simple_blogger.poster.telegram import TelegramPoster
from simple_blogger.poster.instagram import InstagramPoster
from simple_blogger.poster.vk import VkPoster
from simple_blogger.blogger import Journalist
from simple_blogger.preprocessor.text import TagAdder
from simple_blogger.generator.openai import OpenAiTextGenerator
# from simple_blogger.generator.openai import OpenAiImageGenerator
from simple_blogger.generator.yandex import YandexImageGenerator
import datetime

class GamerBlogger(Journalist):
    # def _system_prompt(self):
    #     return 'Ты - игроман'

    def _message_generator(self):
        return OpenAiTextGenerator('Ты - игроман')
    
    def _image_generator(self):
        return YandexImageGenerator(style_prompt='Киберпанк, гиперреалистичный')

    # def _image_generator(self):
    #     return OpenAiImageGenerator(system_prompt="Нарисуй рисунок, вдохновлённый описанием")

    def _prompt_constructor(self, _):
        return f"Опиши рандомную существующую компютерную игру из категории '{self.category}', расскажи интересный факт об игре. Не упоминай авторов. Используй смайлики и не более 150 слов."

    def __init__(self, category, tags):
        self.category = category
        tagadder = TagAdder(['#игроман', '#игры', '#иллюстрации', *tags ])
        posters = [
            TelegramPoster(chat_id='@venatus_the', processor=tagadder),
            VkPoster(group_id='230445524', processor=tagadder),
            # TelegramPoster(processor=tagadder)
        ]
        super().__init__(posters)

def post(offset=0):
    start_date = datetime.date(2025, 5, 11)
    today = datetime.date.today()
    category = [
        ("Ужастик 90-х", ['#ужастик']),
        ("Файтинг 2010-х", ['#файтинг']),
        ("Шутер от первого лица 2000-х", ['#шутер']),
        ("Королевская битва 2020-х", ['#королевскаябитва']),
        ("Гонки 90-х", ['#гонки']),
        ("РПГ 80-х", ['#рпг']),
        ("Спорт 80-х", ['#спорт']),
        ("Пазлы 80-х", ['#пазл']),
        ("Экшн РПГ 2010-х", ['#рпг']),
        ("Файтинг 2000-х", ['#файтинг']),
        ("Платформер 2000-х", ['#платформер']),
        ("Ужастик 2010-х", ['#ужастик']),
        ("Гонки 90-х", ['#гонки']),
        ("Пазлы 90-х", ['#пазл']),
        ("Гонки 80-х", ['#гонки']),
        ("Открытый мир 2020-х", ['#открытыймир']),
        ("Гонки 2000-х", ['#гонки']),
        ("РПГ 2000-х", ['#рпг']),
        ("Приключения 89-х", ['#приключения']),
        ("Платформер 80-х", ['#платформер']),
        ("Визуальная новелла 2000-х", ['#визуальнаяновелла']),
        ("Экшн 80-х", ['#экшн']),
        ("Шутер 2010-х", ['#шутер']),
        ("Спорт 90-х", ['#спорт']),
        ("Выживание 2020-х", ['#выживач']),
        ("Аркада 80-х", ['#аркада']),
        ("Гонки 2020-х", ['#гонки']),
        ("Ремейк, ремастер 2020-х", ['#ремейк', '#ремастер']),
        ("Souls-like 2020-х", ['#soulslike']),
        ("Нарратив AAA 2020-х", ['#нарратив', '#AAA']),
        ("Открытый мир 2010-х", ['#открытыймир']),
        ("Платформер 90-х", ['#платформер']),
        ("Инди 2010-х", ['#инди']),
        ("Стратегия реального времени 90-х", ['#стратегия']),
        ("Файтинг 90-х", ['#файтинг']),
        ("Виртульная реальность 2010-х", ['#файтинг']),
        ("Инди 2020-х", ['#инди']),
        ("Открытый мир 2000-х", ['#открытыймир']),
        ("Файтинг 80-х", ['#файтинг']),
        ("Ужастик 2020-х", ['#ужастик']),
        ("Ужастик 2000-х", ['#ужастик']),
        ("Песочница 2010-х", ['#песочница']),
        ("РПГ 90-х", ['#рпг']),
        ("Нарратив 2010-х", ['#нарратив']),
        ("Виртульная реальность 2020-х", ['#файтинг']),
        ("Симулятор 2020-х", ['#симулятор']),
        ("Спорт 2000-х", ['#спорт']),
        ("Королевская битва 2010-х", ['#королевскаябитва']),
    ]
    index = ((today - start_date).days + offset) % len(category)
    blogger = GamerBlogger(category[index][0], category[index][1])
    blogger.post()

if __name__ == "__main__":
    post()