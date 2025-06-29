# import json
from simple_blogger.blogger import Journalist
from simple_blogger.poster.telegram import TelegramPoster
from simple_blogger.poster.vk import VkPoster
from simple_blogger.preprocessor.text import TagAdder
from datetime import date, timedelta

class HaikuBlogger(Journalist):
    
    def _system_prompt(self):
        return "Ты - автор хайку, последователь Мацуо Басё. Я дам тебе тему. Напиши хайку на заданную тему"
    
    def _prompt_constructor(self, _):
        return f"{self.task['theme']}"

    def __init__(self, task):
        self.task = task
        tagadder = TagAdder(['#хайку', '#хокку', '#17слогов', '#five_seven_five'])
        posters = [
            VkPoster(group_id='231330317', processor=tagadder),
            # TelegramPoster(processor=tagadder)
        ]
        super().__init__(posters)


def post(offset=0):
    tasks = [
        {"theme": "Природа"},
        {"theme": "Смена времен года"},
        {"theme": "Цветение сакуры"},
        {"theme": "Осень и увядание листьев"},
        {"theme": "Зима и снегопад"},
        {"theme": "Весеннее пробуждение природы"},
        {"theme": "Летний зной и дожди"},
        {"theme": "Ночное небо и звезды"},
        {"theme": "Рассвет и закат солнца"},
        {"theme": "Одиночество и размышления"},
        {"theme": "Горная тропинка"},
        {"theme": "Ручей в лесу"},
        {"theme": "Дождливый вечер"},
        {"theme": "Утро в деревне"},
        {"theme": "Полет журавлей"},
        {"theme": "Костер в ночи"},
        {"theme": "Морская волна"},
        {"theme": "Храм в тумане"},
        {"theme": "Звук колокольчика"},
        {"theme": "Запах хвои"},
        {"theme": "Тишина леса"},
        {"theme": "Каменная пагода"},
        {"theme": "Полёт бабочки"},
        {"theme": "Цветение лотоса"},
        {"theme": "Старый мост"},
        {"theme": "Мелодия ветра"},
        {"theme": "Свет луны"},
        {"theme": "Капли росы"},
        {"theme": "Свежий ветер"},
        {"theme": "Теплый камин"},
        {"theme": "Иней на ветках"},
        {"theme": "Закат над озером"},
        {"theme": "Поле подсолнухов"},
        {"theme": "Туманное утро"},
        {"theme": "Радуга после дождя"},
        {"theme": "Сквозняк в доме"},
        {"theme": "Шелест травы"},
        {"theme": "Голос кукушки"},
        {"theme": "Плеск рыбы"},
        {"theme": "Вечерняя прохлада"},
        {"theme": "Облако плывет"},
        {"theme": "Следы зверей"},
        {"theme": "Колосящиеся поля"},
        {"theme": "Песня соловья"},
        {"theme": "Звуки дождя"},
        {"theme": "Цветущие яблони"},
        {"theme": "Стрекот кузнечиков"},
        {"theme": "Взгляд на горы"},
        {"theme": "Голубое небо"},
        {"theme": "Шёпот волн"},
        {"theme": "Ранняя весна"},
        {"theme": "Поздняя осень"},
        {"theme": "Огонь свечи"},
        {"theme": "Серебряный месяц"},
        {"theme": "Морозный узор"},
        {"theme": "Запах цветов"},
        {"theme": "Шаги путника"},
        {"theme": "Спящий кот"},
        {"theme": "Медитация в саду"},
        {"theme": "Море и чайки"},
        {"theme": "Путешествие духа"},
        {"theme": "Безмолвие камней"}
    ]
    start_date = date(2025, 6, 29)-timedelta(days=offset)
    today = date.today()
    index = ((today - start_date).days + offset) % len(tasks)
    blogger = HaikuBlogger(tasks[index])
    blogger.post()

if __name__ == "__main__":
    post()
