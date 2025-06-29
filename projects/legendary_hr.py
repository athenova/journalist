from simple_blogger.poster.telegram import TelegramPoster
from simple_blogger.poster.vk import VkPoster
from simple_blogger.blogger import Journalist
from simple_blogger.preprocessor.text import TagAdder
from simple_blogger.generator.openai import OpenAiTextGenerator
from datetime import date, timedelta

class LegendaryHrBlogger(Journalist):
    def _message_generator(self):
        return OpenAiTextGenerator("Я дам тебе имя известного специалиста HR. Приведи интересный факт, связанный с ним. Используй смайлики и не более 150 слов. Не используй 'Окей' и 'Конечно'")
    
    def _prompt_constructor(self, _):
        return self.task['hr']

    def __init__(self, task):
        self.task = task
        tagadder = TagAdder(['#hr', '#кадры', '#it', '#ит', '#айти', '#легенды'])
        posters = [
            TelegramPoster(chat_id='@coffee_and_nerves', processor=tagadder),
            VkPoster(group_id='229838019', processor=tagadder)
            # TelegramPoster(processor=tagadder)
        ]
        super().__init__(posters)


def post(offset=0):
    tasks = [
        {"hr": "Лиза Ла Бушель"},
        {"hr": "Кейт Свини"},
        {"hr": "Люк Дюмон"},
        {"hr": "Мелисса Майерс"},
        {"hr": "Давид Уоллес"},
        {"hr": "Пэт Миллер"},
        {"hr": "Стив Эмерсон"},
        {"hr": "Дженнифер Янг"},
        {"hr": "Джессика Уильямс"},
        {"hr": "Роберт Джонсон"},
        {"hr": "Джейн Коултер"},
        {"hr": "Кайл Робертс"},
        {"hr": "Лора Мартин"},
        {"hr": "Майкл Харрис"},
        {"hr": "Кэролайн Дэвис"},
        {"hr": "Бенджамин Грин"},
        {"hr": "Андреа Льюис"},
        {"hr": "Дэвид Джексон"},
        {"hr": "Сьюзан Гриффин"},
        {"hr": "Марк Тейлор"},
        {"hr": "Сара Вильсон"},
        {"hr": "Кристофер Скотт"},
        {"hr": "Эмили Смит"},
        {"hr": "Дэниел Мур"},
        {"hr": "Элизабет Кларк"},
        {"hr": "Джейсон Кинг"},
        {"hr": "Ребекка Томас"},
        {"hr": "Дилан Райан"},
        {"hr": "Тереза Андерсон"},
        {"hr": "Ханна Эванс"},
        {"hr": "Кори Ричардс"},
        {"hr": "Камилла Санчес"},
        {"hr": "Лука Пирелли"},
        {"hr": "Адриано Дель Монте"},
        {"hr": "Лаура Ромеро"},
        {"hr": "Рафаэль Лопес"},
        {"hr": "София Эрнандес"},
        {"hr": "Фабио Коста"},
        {"hr": "Джованни Росати"},
        {"hr": "Катрин Валле"},
        {"hr": "Пьер Мишель"},
        {"hr": "Эмма Леруа"},
        {"hr": "Франсуа Дюран"},
        {"hr": "Симона Ларше"},
        {"hr": "Томас Бюиссон"},
        {"hr": "Марта Фернандес"},
        {"hr": "Карлос Гомес"},
        {"hr": "Сильвия Перес"},
        {"hr": "Луис Мартинес"},
        {"hr": "Анастасия Романова"},
        {"hr": "Петр Ковалёв"},
        {"hr": "Евгений Михайлов"},
        {"hr": "Наталья Семина"},
        {"hr": "Дмитрий Куликов"},
        {"hr": "Ирина Чернышёва"}
    ]
    start_date = date(2025, 7, 6)-timedelta(days=offset)
    today = date.today()
    index = ((today - start_date).days // 7 + offset) % len(tasks)
    blogger = LegendaryHrBlogger(tasks[index])
    blogger.post()

if __name__ == "__main__":
    post()