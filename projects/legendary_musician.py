from simple_blogger.poster.telegram import TelegramPoster
from simple_blogger.poster.vk import VkPoster
from simple_blogger.blogger import Journalist
from simple_blogger.preprocessor.text import TagAdder
from simple_blogger.generator.openai import OpenAiTextGenerator
from datetime import date, timedelta

class LegendaryMusicianBlogger(Journalist):
    def _message_generator(self):
        return OpenAiTextGenerator("Я дам тебе имя известного музыканта. Приведи интересный факт, связанный с ним. Используй смайлики и не более 150 слов. Не используй 'Окей' и 'Конечно'")
    
    def _prompt_constructor(self, _):
        return self.task["artist"]

    def __init__(self, task):
        self.task = task
        tagadder = TagAdder(['#меломан', '#музыка', '#иллюстрации', '#песни', '#легенды', task["tag"]])
        posters = [
            TelegramPoster(chat_id='@meloman_the', processor=tagadder),
            VkPoster(group_id='229821806', processor=tagadder)
            # TelegramPoster(processor=tagadder)
        ]
        super().__init__(posters)

def post(offset=0):
    tasks = [
        {"artist": "Шанайя Твейн", "tag": "#певец"},
        {"artist": "Томми Ли", "tag": "#барабанщик"},
        {"artist": "Ринго Старр", "tag": "#барабанщик"},
        {"artist": "Keane", "tag": "#певец"},
        {"artist": "Тони Айомми", "tag": "#гитарист"},
        {"artist": "Оззи Осборн", "tag": "#певец"},
        {"artist": "Джими Пейдж", "tag": "#гитарист"},
        {"artist": "Джонни Рамон", "tag": "#гитарист"},
        {"artist": "Санджив Шарма", "tag": "#гитарист"},
        {"artist": "Джейсон Боумен", "tag": "#барабанщик"},
        {"artist": "Канье Уэст", "tag": "#певец"},
        {"artist": "Кори Тейлор", "tag": "#барабанщик"},
        {"artist": "Билли Джо Армстронг", "tag": "#певец"},
        {"artist": "Адель", "tag": "#певец"},
        {"artist": "Зара Ларсон", "tag": "#певец"},
        {"artist": "Мартин Барр", "tag": "#гитарист"},
        {"artist": "Том Морелло", "tag": "#гитарист"},
        {"artist": "Йенс Сигмундсен", "tag": "#барабанщик"},
        {"artist": "Роберт Трухильо", "tag": "#гитарист"},
        {"artist": "Дэйв Гручински", "tag": "#барабанщик"},
        {"artist": "Ричард Берк", "tag": "#барабанщик"},
        {"artist": "Эдди Ван Хален", "tag": "#гитарист"},
        {"artist": "Клинт Байам", "tag": "#барабанщик"},
        {"artist": "Стив Люкатер", "tag": "#гитарист"},
        {"artist": "Арияна Гранде", "tag": "#певец"},
        {"artist": "Боно", "tag": "#певец"},
        {"artist": "Джерри Гранатта", "tag": "#барабанщик"},
        {"artist": "Брайан Мэй", "tag": "#гитарист"},
        {"artist": "Лу Рид", "tag": "#гитарист"},
        {"artist": "Tiesto", "tag": "#певец"},
        {"artist": "Иэн Гиллан", "tag": "#гитарист"},
        {"artist": "Йеспер Стромблад", "tag": "#гитарист"},
        {"artist": "Шон Мендейл", "tag": "#певец"},
        {"artist": "Маршалл Мэтерс III", "tag": "#певец"},
        {"artist": "Ричи Блэкмор", "tag": "#гитарист"},
        {"artist": "Джой Джордан", "tag": "#барабанщик"},
        {"artist": "Малкольм Янг", "tag": "#гитарист"},
        {"artist": "Дэвид Ломбардо", "tag": "#барабанщик"},
        {"artist": "Марк Нобл", "tag": "#гитарист"},
        {"artist": "Кирк Хэмметт", "tag": "#гитарист"},
        {"artist": "Кельвин Харрис", "tag": "#певец"},
        {"artist": "Томми Эммануэля", "tag": "#гитарист"},
        {"artist": "Ричи Котцен", "tag": "#гитарист"},
        {"artist": "Джон Финн", "tag": "#барабанщик"},
        {"artist": "Томми Хорн", "tag": "#барабанщик"},
        {"artist": "Марк Нопфлер", "tag": "#гитарист"},
        {"artist": "Пит Тауншенд", "tag": "#гитарист"},
        {"artist": "Принс", "tag": "#певец"},
        {"artist": "Фредди Меркьюри", "tag": "#певец"},
        {"artist": "Тайлер Джозеф", "tag": "#певец"},
        {"artist": "Трой Сент Джона", "tag": "#гитарист"},
        {"artist": "Робби Уильямс", "tag": "#певец"},
        {"artist": "Билли Гиббонс", "tag": "#гитарист"},
        {"artist": "Дуа Липа", "tag": "#певец"},
        {"artist": "Чарли Вотерс", "tag": "#барабанщик"},
        {"artist": "Джимми Пейдж", "tag": "#гитарист"},
        {"artist": "Джефф Линн", "tag": "#гитарист"},
        {"artist": "Ричи Фьюнес", "tag": "#гитарист"},
        {"artist": "Дэн Спиц", "tag": "#барабанщик"},
        {"artist": "Дэнни Маршалл", "tag": "#барабанщик"},
        {"artist": "Кэти Перри", "tag": "#певец"},
        {"artist": "Тревис Баркер", "tag": "#барабанщик"},
        {"artist": "Джереми Энжел", "tag": "#барабанщик"},
        {"artist": "Билл Бруфор", "tag": "#барабанщик"},
        {"artist": "Джоуи Джордисон", "tag": "#барабанщик"},
        {"artist": "Justin Timberlake", "tag": "#певец"},
        {"artist": "Майкл Манринг", "tag": "#барабанщик"},
        {"artist": "Авичи", "tag": "#певец"},
        {"artist": "Флойд Пинкстон", "tag": "#барабанщик"},
        {"artist": "Мадонна", "tag": "#певец"},
        {"artist": "Стив Морс", "tag": "#гитарист"},
        {"artist": "Майкл Джексон", "tag": "#певец"},
        {"artist": "Джефф Уотсон", "tag": "#гитарист"},
        {"artist": "Элтон Джон", "tag": "#певец"},
        {"artist": "Джон Бонэм", "tag": "#барабанщик"},
        {"artist": "Lady Antebellum", "tag": "#певец"},
        {"artist": "Штеффен Крамер", "tag": "#гитарист"},
        {"artist": "Брюс Спрингстин", "tag": "#певец"},
        {"artist": "Питер Фрэмптон", "tag": "#гитарист"},
        {"artist": "Стив Смит", "tag": "#барабанщик"},
        {"artist": "Стинг", "tag": "#певец"},
        {"artist": "Стив Гэдд", "tag": "#барабанщик"},
        {"artist": "Крис Имгелсон", "tag": "#гитарист"},
        {"artist": "Эрик Клэптон", "tag": "#гитарист"},
        {"artist": "Дэвид Гильмор", "tag": "#гитарист"},
        {"artist": "Макс Роуч", "tag": "#барабанщик"},
        {"artist": "Эдди Джексон", "tag": "#барабанщик"},
        {"artist": "Роберт Плант", "tag": "#певец"},
        {"artist": "Ричи Самбора", "tag": "#гитарист"},
        {"artist": "Дэвид Расселл", "tag": "#гитарист"},
        {"artist": "Леди Гага", "tag": "#певец"},
        {"artist": "Брэд Вилк", "tag": "#барабанщик"},
        {"artist": "Эд Ширан", "tag": "#певец"},
        {"artist": "Кармин Аппис", "tag": "#барабанщик"},
        {"artist": "Кэртис Салливан", "tag": "#барабанщик"},
        {"artist": "Брайан Тайлер", "tag": "#барабанщик"},
        {"artist": "Дэнни Кэреллис", "tag": "#барабанщик"},
        {"artist": "The Weeknd", "tag": "#певец"},
        {"artist": "Дэйв Мастейн", "tag": "#гитарист"},
        {"artist": "Теренс Ходжес", "tag": "#барабанщик"},
        {"artist": "Глен Типтон", "tag": "#гитарист"},
        {"artist": "Джефф Бек", "tag": "#гитарист"},
        {"artist": "Стив Вай", "tag": "#гитарист"},
        {"artist": "Рэнди Роадс", "tag": "#гитарист"},
        {"artist": "Крис Адлер", "tag": "#барабанщик"},
        {"artist": "Скотт Ян", "tag": "#гитарист"},
        {"artist": "Дэвид Филдинг", "tag": "#барабанщик"},
        {"artist": "Томми Дэдисон", "tag": "#барабанщик"},
        {"artist": "Стив Стивенс", "tag": "#гитарист"},
        {"artist": "Джейсон Бонавентуре", "tag": "#барабанщик"},
        {"artist": "Йохан Экстрём", "tag": "#гитарист"},
        {"artist": "Бритни Спирс", "tag": "#певец"},
        {"artist": "Ларс Ульрих", "tag": "#барабанщик"},
        {"artist": "Стиви Уандер", "tag": "#певец"},
        {"artist": "Дэвид Боуи", "tag": "#певец"},
        {"artist": "Гэри Мур", "tag": "#гитарист"},
        {"artist": "Керри Кинг", "tag": "#гитарист"},
        {"artist": "Кендрик Ламар", "tag": "#певец"},
        {"artist": "Крис Чемпен", "tag": "#барабанщик"},
        {"artist": "Джо Сатриани", "tag": "#барабанщик"},
        {"artist": "Джой Бауман", "tag": "#барабанщик"},
        {"artist": "Шон Кинни", "tag": "#барабанщик"},
        {"artist": "Фло Риффа", "tag": "#певец"},
        {"artist": "Джой Пеннингтон", "tag": "#барабанщик"},
        {"artist": "Хейли Стэнфилд", "tag": "#певец"},
        {"artist": "Эдди Веддер", "tag": "#певец"},
        {"artist": "Мартин Гаррикс", "tag": "#певец"},
        {"artist": "Джимми Хендрикс", "tag": "#певец"},
        {"artist": "Нил Пирт", "tag": "#барабанщик"},
        {"artist": "Джон Петерсон", "tag": "#гитарист"},
        {"artist": "Эдриан Смит", "tag": "#гитарист"},
        {"artist": "Ангус Янг", "tag": "#гитарист"},
        {"artist": "Гингер Бейкер", "tag": "#барабанщик"},
        {"artist": "Джой Джордж", "tag": "#барабанщик"},
        {"artist": "Рианна", "tag": "#певец"},
        {"artist": "Билли Кобхэм", "tag": "#барабанщик"},
        {"artist": "Брэд Уилсон", "tag": "#барабанщик"},
        {"artist": "Эдди Оттен", "tag": "#барабанщик"},
        {"artist": "Кит Мун", "tag": "#барабанщик"},
        {"artist": "Слэш", "tag": "#гитарист"},
        {"artist": "Честер Беннингтон", "tag": "#певец"},
        {"artist": "Брюс Дикинсон", "tag": "#певец"},
        {"artist": "Дэйв Грол", "tag": "#гитарист"},
        {"artist": "Джеймс Хэтфилд", "tag": "#гитарист"},
        {"artist": "Коби Брайант", "tag": "#певец"},
        {"artist": "Боб Дилан", "tag": "#певец"},
        {"artist": "Сэм Маллетт", "tag": "#барабанщик"},
        {"artist": "Кен Ватсона", "tag": "#барабанщик"},
        {"artist": "Селин Дион", "tag": "#певец"},
        {"artist": "Дэвид Варнье", "tag": "#барабанщик"},
        {"artist": "Крис Мартин", "tag": "#певец"},
        {"artist": "Энрике Иглесиас", "tag": "#гитарист"},
        {"artist": "Дрейк", "tag": "#певец"},
        {"artist": "Йорма Кауконен", "tag": "#гитарист"},
        {"artist": "Майкл Уокер", "tag": "#барабанщик"},
        {"artist": "Дэвид Гетта", "tag": "#певец"},
        {"artist": "Будди Рич", "tag": "#барабанщик"},
        {"artist": "Джеймс Холланд", "tag": "#барабанщик"},
        {"artist": "Эминем", "tag": "#певец"},
    ]
    start_date = date(2025, 7, 6)-timedelta(days=offset)
    today = date.today()
    index = ((today - start_date).days // 7 + offset) % len(tasks)
    blogger = LegendaryMusicianBlogger(tasks[index])
    blogger.post()

if __name__ == "__main__":
    post()