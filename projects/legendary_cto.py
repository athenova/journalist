from simple_blogger.poster.telegram import TelegramPoster
from simple_blogger.poster.vk import VkPoster
from simple_blogger.blogger import Journalist
from simple_blogger.preprocessor.text import TagAdder
from simple_blogger.generator.openai import OpenAiTextGenerator
from datetime import date, timedelta

class LegendaryCtoBlogger(Journalist):
    def _message_generator(self):
        return OpenAiTextGenerator("Я дам тебе имя известного CTO. Приведи интересный факт, связанный с ним. Используй смайлики и не более 150 слов. Не используй 'Окей' и 'Конечно'")
    
    def _prompt_constructor(self, _):
        return self.task["cto"]

    def __init__(self, task):
        self.task = task
        tagadder = TagAdder(['#cto', '#it', '#ит', '#айти', '#легенды'])
        posters = [
            TelegramPoster(chat_id='@cto_in_fire', processor=tagadder),
            VkPoster(group_id='229837981', processor=tagadder)
            # TelegramPoster(processor=tagadder)
        ]
        super().__init__(posters)

def post(offset=0):
    tasks = [
        {"cto": "Джефф Дин"},
        {"cto": "Элон Маск"},
        {"cto": "Брендан Эйч"},
        {"cto": "Рэй Оззи"},
        {"cto": "Марк Бениофф"},
        {"cto": "Винт Серф"},
        {"cto": "Деннис Ритчи"},
        {"cto": "Джеймс Гослинг"},
        {"cto": "Энди Херцфельд"},
        {"cto": "Кен Томпсон"},
        {"cto": "Билл Джой"},
        {"cto": "Линус Торвальдс"},
        {"cto": "Гвидо ван Россум"},
        {"cto": "Алэн Кэй"},
        {"cto": "Тим Бернерс-Ли"},
        {"cto": "Дональд Кнут"},
        {"cto": "Дэвид Катлер"},
        {"cto": "Джон Кармак"},
        {"cto": "Адам Босуорт"},
        {"cto": "Майкл Лукидес"},
        {"cto": "Эрик Шмидт"},
        {"cto": "Эндрю Нг"},
        {"cto": "Янн ЛеКун"},
        {"cto": "Джеффри Хинтон"},
        {"cto": "Демис Хассабис"},
        {"cto": "Фей-Фей Ли"},
        {"cto": "Илья Суцкевер"},
        {"cto": "Питер Норвиг"},
        {"cto": "Майкл Стоунбрейкер"},
        {"cto": "Джарон Ланье"},
        {"cto": "Ричард Столмен"},
        {"cto": "Брайан Керниган"},
        {"cto": "Роб Пайк"},
        {"cto": "Дуг Энгельбарт"},
        {"cto": "Ада Лавлейс"},
        {"cto": "Грэйс Хоппер"},
        {"cto": "Стив Возняк"},
        {"cto": "Филипп Кан"},
        {"cto": "Дейв Катлер"},
        {"cto": "Брэд Силверберг"},
        {"cto": "Дэн Бриклин"},
        {"cto": "Боб Франкстон"},
        {"cto": "Тед Нельсон"},
        {"cto": "Эдгар Ф. Кодд"},
        {"cto": "Эрик Мейер"},
        {"cto": "Мартин Одерски"},
        {"cto": "Джеймс Гамильтон"},
        {"cto": "Джим Грей"},
        {"cto": "Рэнди Пауш"},
        {"cto": "Чарльз Симони"},
        {"cto": "Ларри Теслер"},
        {"cto": "Джонатан Айв"},
        {"cto": "Герман Холлерит"},
        {"cto": "Жозеф Мари Жаккар"},
        {"cto": "Джордж Буль"},
        {"cto": "Клод Шеннон"},
        {"cto": "Ноам Хомский"},
        {"cto": "Курт Гёдель"},
        {"cto": "Стивен Вольфрам"},
        {"cto": "Пол Грэм"},
        {"cto": "Роберт Нойс"},
        {"cto": "Уильям Шокли"},
        {"cto": "Джек Килби"},
        {"cto": "Дон Кнут"}
    ]
    start_date = date(2025, 7, 6)-timedelta(days=offset)
    today = date.today()
    index = ((today - start_date).days // 7 + offset) % len(tasks)
    blogger = LegendaryCtoBlogger(tasks[index])
    blogger.post()

if __name__ == "__main__":
    post()