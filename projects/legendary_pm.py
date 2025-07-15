from simple_blogger.poster.telegram import TelegramPoster
from simple_blogger.poster.vk import VkPoster
from simple_blogger.blogger import Journalist
from simple_blogger.preprocessor.text import TagAdder
from simple_blogger.generator.openai import OpenAiTextGenerator
from datetime import date, timedelta

class LegendaryPmBlogger(Journalist):
    def _message_generator(self):
        return OpenAiTextGenerator("Я дам тебе имя известного проектного менеджера. Приведи интересный факт, связанный с ним. Используй смайлики и не более 150 слов. Не используй 'Окей' и 'Конечно'")
    
    def _prompt_constructor(self, _):
        return self.task['pm']

    def __init__(self, task):
        self.task = task
        tagadder = TagAdder(['#pm', '#projectmanagement', '#it', '#ит', '#айти', '#проблемы', '#легенды'])
        posters = [
            TelegramPoster(chat_id='-1002360664560', processor=tagadder),
            VkPoster(group_id='229837997', processor=tagadder)
            # TelegramPoster(processor=tagadder)
        ]
        super().__init__(posters)


def post(offset=0):
    tasks = [
        {"pm": "Джон Коттер"},
        {"pm": "Джеффри Пфеффер"},
        {"pm": "Генри Минцберг"},
        {"pm": "Михай Чиксентмихайи"},
        {"pm": "Питер Друкер"},
        {"pm": "Эдвард Лоулер"},
        {"pm": "Фредерик Герцберг"},
        {"pm": "Абрахам Маслоу"},
        {"pm": "Марк Липсон"},
        {"pm": "Кеннет Эндрюс"},
        {"pm": "Ричард Бойатт"},
        {"pm": "Стив Деннинг"},
        {"pm": "Ричард Дафт"},
        {"pm": "Джеральд Келли"},
        {"pm": "Брюс Хендерсон"},
        {"pm": "Дэвид Аллен"},
        {"pm": "Гэри Хамел"},
        {"pm": "Михаэль Портер"},
        {"pm": "Роберт Каплан"},
        {"pm": "Джером Голдштейн"},
        {"pm": "Том Питерс"},
        {"pm": "Фил Розенцвейг"},
        {"pm": "Филип Селзник"},
        {"pm": "Джанетт Роулинсон"},
        {"pm": "Грег Сайнс"},
        {"pm": "Марк Батчер"},
        {"pm": "Марк Коберн"},
        {"pm": "Роберт Хаус"},
        {"pm": "Айрис Бирнбаум"},
        {"pm": "Дэвид Коупленд"},
        {"pm": "Тимоти Галлуэй"},
        {"pm": "Стивен Кови"},
        {"pm": "Дэвид Беннетт"},
        {"pm": "Фрэнк Паркер"},
        {"pm": "Филип Роббинс"},
        {"pm": "Сюзанна Блэквелл"},
        {"pm": "Гэри Беккетт"},
        {"pm": "Стивен Барнс"},
        {"pm": "Майкл Басси"},
        {"pm": "Мария Йоханссен"},
        {"pm": "Дэвид Шеридан"},
        {"pm": "Рита Хейес"},
        {"pm": "Сьюзен Бейкер"},
        {"pm": "Питер Уилсон"},
        {"pm": "Джоанна Данкан"},
        {"pm": "Марк Дональдсон"},
        {"pm": "Клаудия Винсент"},
        {"pm": "Кейт Бакстер"},
        {"pm": "Джон Уайт"},
        {"pm": "Луиза Ричардсон"},
        {"pm": "Рэйчел Джонс"},
        {"pm": "Кэрол Мэйсон"},
        {"pm": "Кэролайн Форрест"},
        {"pm": "Барбара Стивенсон"},
        {"pm": "Питер Харрисон"},
        {"pm": "Джастин Паттерсон"}
    ]
    start_date = date(2025, 7, 6)-timedelta(days=offset)
    today = date.today()
    index = ((today - start_date).days // 7 + offset) % len(tasks)
    blogger = LegendaryPmBlogger(tasks[index])
    blogger.post()

if __name__ == "__main__":
    post()