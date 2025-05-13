from simple_blogger.blogger.auto import AutoSimpleBlogger
from simple_blogger.poster.telegram import TelegramPoster
from simple_blogger.poster.vk import VkPoster
from simple_blogger.preprocessor.text import TagAdder
from simple_blogger.generator import TextGenerator
from simple_blogger.generator.openai import GptImageGenerator
from datetime import date, datetime

tagadder = TagAdder(['#иллюстрации', '#фантазии'])

class MasterpieceBlogger(AutoSimpleBlogger):
    def _tasks_file_path(self):
        return f"./files/masterpiece_the.json"
    
    def _message_prompt_constructor(self, task):
        return f"{task['name']}, {task['author']}, {task['period']}. {task['location']}, {task['description']}"
    
    def _message_generator(self):
        return TextGenerator("Ты - профессиональный искусствовед")
    
    def _image_generator(self):
        return GptImageGenerator(api_key_name="GPT_API_KEY")

    def _image_prompt_constructor(self, task):
        return f"Нарисуй картину '{task['name']}' автора '{task['author']}' в стиле {self.style}"
        
    def _posters(self):
        return [
            TelegramPoster(chat_id='@masterpiece_the', processor=tagadder),
            VkPoster(group_id='229902850', processor=tagadder),
        ]

    def __init__(self, posters=None, first_post_date=date(2025, 5, 13), style=None):
        self.style = style
        super().__init__(posters=posters or self._posters(), first_post_date=first_post_date)

def post(offset=0):
    styles=[
        {
            "style": "Античная живопись",
            "period": "до V в. н.э.",
            "key_features": "фрески, энкаустика, мифологические сюжеты",
            "artists": ["Неизвестные мастера Помпеи"]
        },
        {
            "style": "Византийский",
            "period": "V–XV вв.",
            "key_features": "иконы, золотой фон, религиозная символика",
            "artists": ["Феофан Грек", "Андрей Рублёв"]
        },
        {
            "style": "Готика",
            "period": "XIII–XVI вв.",
            "key_features": "витражи, экспрессивные религиозные сцены",
            "artists": ["Симоне Мартини", "Братья Лимбург"]
        },
        {
            "style": "Ренессанс",
            "period": "XV–XVI вв.",
            "key_features": "перспектива, анатомия, гармония",
            "artists": ["Леонардо да Винчи", "Рафаэль", "Микеланджело"]
        },
        {
            "style": "Барокко",
            "period": "XVII – начало XVIII вв.",
            "key_features": "драма, контрасты света и тени",
            "artists": ["Караваджо", "Рубенс", "Рембрандт"]
        },
        {
            "style": "Рококо",
            "period": "XVIII в.",
            "key_features": "пастельные тона, галантные сцены",
            "artists": ["Ватто", "Фрагонар", "Буше"]
        },
        {
            "style": "Классицизм",
            "period": "XVII–XIX вв.",
            "key_features": "античные идеалы, строгие композиции",
            "artists": ["Пуссен", "Жак-Луи Давид"]
        },
        {
            "style": "Романтизм",
            "period": "конец XVIII – XIX вв.",
            "key_features": "эмоции, природа, экзотика",
            "artists": ["Делакруа", "Тёрнер", "Гойя"]
        },
        {
            "style": "Реализм",
            "period": "XIX в.",
            "key_features": "правдивое изображение жизни",
            "artists": ["Гюстав Курбе", "Жан-Франсуа Милле"]
        },
        {
            "style": "Импрессионизм",
            "period": "1870–1890-е",
            "key_features": "свет, мгновенные впечатления",
            "artists": ["Клод Моне", "Огюст Ренуар", "Эдгар Дега"]
        },
        {
            "style": "Постимпрессионизм",
            "period": "конец XIX в.",
            "key_features": "субъективный цвет и форма",
            "artists": ["Ван Гог", "Поль Сезанн", "Поль Гоген"]
        },
        {
            "style": "Модерн (Ар-нуво)",
            "period": "конец XIX – начало XX вв.",
            "key_features": "орнаменты, плавные линии",
            "artists": ["Густав Климт", "Альфонс Муха"]
        },
        {
            "style": "Фовизм",
            "period": "1905–1910",
            "key_features": "яркие цвета, агрессивные мазки",
            "artists": ["Анри Матисс", "Андре Дерен"]
        },
        {
            "style": "Экспрессионизм",
            "period": "1905–1920-е",
            "key_features": "деформация, эмоциональная напряжённость",
            "artists": ["Эдвард Мунк", "Эгон Шиле", "Эмиль Нольде"]
        },
        {
            "style": "Кубизм",
            "period": "1907–1920-е",
            "key_features": "геометрические формы, разложение объекта",
            "artists": ["Пабло Пикассо", "Жорж Брак", "Хуан Грис"]
        },
        {
            "style": "Футуризм",
            "period": "1910–1940-е",
            "key_features": "динамика, скорость, урбанизм",
            "artists": ["Умберто Боччони", "Джакомо Балла"]
        },
        {
            "style": "Супрематизм",
            "period": "1915–1930-е",
            "key_features": "геометрическая абстракция, «Чёрный квадрат»",
            "artists": ["Казимир Малевич", "Эль Лисицкий"]
        },
        {
            "style": "Дадаизм",
            "period": "1916–1923",
            "key_features": "абсурд, антиискусство, коллажи",
            "artists": ["Марсель Дюшан", "Ханна Хёх"]
        },
        {
            "style": "Сюрреализм",
            "period": "1920–1960-е",
            "key_features": "подсознание, фантастические образы",
            "artists": ["Сальвадор Дали", "Рене Магритт", "Макс Эрнст"]
        },
        {
            "style": "Абстрактный экспрессионизм",
            "period": "1940–1960-е",
            "key_features": "спонтанность, крупные мазки",
            "artists": ["Джексон Поллок", "Марк Ротко"]
        },
        {
            "style": "Поп-арт",
            "period": "1950–1960-е",
            "key_features": "массовая культура, ирония",
            "artists": ["Энди Уорхол", "Рой Лихтенштейн"]
        },
        {
            "style": "Концептуальное искусство",
            "period": "с 1960-х",
            "key_features": "идея важнее формы",
            "artists": ["Джозеф Кошут", "Сол ЛеВитт"]
        }
    ]
    start_date = datetime.date(2025, 5, 13)
    today = datetime.date.today()
    index = ((today - start_date).days + offset) % len(styles)
    blogger = MasterpieceBlogger(first_post_date=start_date, style=styles[index]['style'])
    blogger.post()

if __name__ == "__main__":
    post()