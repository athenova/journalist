from simple_blogger.poster.telegram import TelegramPoster
from simple_blogger.poster.vk import VkPoster
from simple_blogger.blogger import Journalist
from simple_blogger.preprocessor.text import TagAdder
from simple_blogger.generator.openai import OpenAiTextGenerator
from datetime import date, timedelta

class LegendaryDesigner(Journalist):
    def _message_generator(self):
        return OpenAiTextGenerator("Я дам тебе имя известного промышленного дизайнера. Приведи интересный факт, связанный с ним. Используй смайлики и не более 150 слов. Не используй 'Окей' и 'Конечно'")
    
    def _prompt_constructor(self, _):
        return self.task['designer']

    def __init__(self, task):
        self.task = task
        tagadder = TagAdder(['#design', '#дизайн', '#правик', '#креатив', '#макеты', '#шрифты', '#легенды'])
        posters = [
            TelegramPoster(chat_id='-1002633483480', processor=tagadder),
            VkPoster(group_id='230335670', processor=tagadder)
            # TelegramPoster(processor=tagadder)
        ]
        super().__init__(posters)


def post(offset=0):
    tasks = [
        {"designer": "Диетер Рамс"},
        {"designer": "Джонатан Айв"},
        {"designer": "Филипп Старк"},
        {"designer": "Наото Фукасава"},
        {"designer": "Карлос Крукс-Диес"},
        {"designer": "Антонио Читтерио"},
        {"designer": "Луиджи Колани"},
        {"designer": "Росс Лавгроув"},
        {"designer": "Марсель Вандерс"},
        {"designer": "Константин Грчик"},
        {"designer": "Патрисия Уркиола"},
        {"designer": "Ора-Ито"},
        {"designer": "Дэниэл Вейл"},
        {"designer": "Ив Бехар"},
        {"designer": "Майкл Грейвс"},
        {"designer": "Этторе Соттсасс"},
        {"designer": "Микеле Де Лукки"},
        {"designer": "Инго Маурер"},
        {"designer": "Паола Навоне"},
        {"designer": "Матали Крассет"},
        {"designer": "Широ Курамата"},
        {"designer": "Вернер Айслер"},
        {"designer": "Штефан Дайц"},
        {"designer": "Норман Фостер"},
        {"designer": "Джейспер Моррисон"},
        {"designer": "Карим Рашид"},
        {"designer": "Жак Гарсия"},
        {"designer": "Марк Ньюсон"},
        {"designer": "Карло Моллино"},
        {"designer": "Хайме Хайон"},
        {"designer": "Франк Гери"},
        {"designer": "Томас Хезервик"},
        {"designer": "Дэвид Чипперфилд"},
        {"designer": "Сантьяго Калатрава"},
        {"designer": "Рензо Пиано"},
        {"designer": "Заха Хадид"},
        {"designer": "Тоё Ито"},
        {"designer": "Херцог и де Мерон"},
        {"designer": "Рем Колхас"},
        {"designer": "Тадао Андо"},
        {"designer": "Жан Нувель"},
        {"designer": "Арата Исодзаке"},
        {"designer": "Рене Матте"},
        {"designer": "Родольфо Боннетто"},
        {"designer": "Мартти Талвио"},
        {"designer": "Марио Беллини"},
        {"designer": "Виктор Папанек"},
        {"designer": "Энцо Мари"},
        {"designer": "Альвар Аалто"},
        {"designer": "Гарри Бертоя"},
        {"designer": "Реймонд Лоуи"},
        {"designer": "Генри Дрейфусс"},
        {"designer": "Шарль Имз"},
        {"designer": "Ле Корбюзье"}
    ]
    start_date = date(2025, 7, 6)-timedelta(days=offset)
    today = date.today()
    index = ((today - start_date).days // 7 + offset) % len(tasks)
    blogger = LegendaryDesigner(tasks[index])
    blogger.post()

if __name__ == "__main__":
    post()