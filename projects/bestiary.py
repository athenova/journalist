from simple_blogger.poster.telegram import TelegramPoster
from simple_blogger.poster.instagram import InstagramPoster
from simple_blogger.poster.vk import VkPoster
from simple_blogger.blogger import Journalist
from simple_blogger.preprocessor.text import TagAdder
from simple_blogger.generator.openai import GptImageGenerator
from simple_blogger.generator.deepseek import DeepSeekTextGenerator
import datetime

class BestiaryBlogger(Journalist):
    def _message_generator(self):
        return DeepSeekTextGenerator('Ты - художник с образованием психолога, знакомый с современными мемами из интернета')
    
    def _image_generator(self):
        return GptImageGenerator(api_key_name="GPT_API_KEY", system_prompt="Нарисуй, как бы выглядело животное по описанию")

    def _prompt_constructor(self, _):
        return f"Придумай смешное итальянское название для фантастического животного похожего на {self.specie} с телом в виде в виде выбранного рандомно неодушевлённого предмета, придумай его родословную. Используй смайлики и не более 150 слов, не используй 'Конечно' и 'Okей'"

    def __init__(self, specie):
        self.specie = specie
        tagadder = TagAdder(['#иллюстрации', '#фантазии'])
        posters = [
            TelegramPoster(chat_id='@bestiary_the', processor=tagadder),
            VkPoster(group_id='230664245', processor=tagadder),
            # InstagramPoster(account_token_name='BESTIARY_THE_TOKEN', processor=tagadder)
            # TelegramPoster(processor=tagadder)
        ]
        super().__init__(posters)

def post(offset=0):
    start_date = datetime.date(2025, 5, 29)
    today = datetime.date.today()
    species = [
        "Кенгуру",
        "Геккон токи",
        "Кузнечик зелёный",
        "Тигр",
        "Монарх бабочка",
        "Гремучая змея",
        "Королевская кобра",
        "Летучая лисица",
        "Лебедь-шипун",
        "Дельфин-афалина",
        "Рыба-бабочка",
        "Осьминог обыкновенный",
        "Муравей-листорез",
        "Рыба-меч",
        "Чёрная мамба",
        "Морская звезда",
        "Лосось атлантический",
        "Тунец",
        "Комодский варан",
        "Фламинго",
        "Дождевой червь",
        "Ара макао",
        "Сокол-сапсан",
        "Морской конёк",
        "Таракан мадагаскарский",
        "Андский кондор",
        "Обыкновенная медуза",
        "Жук-геркулес",
        "Скат-хвостокол",
        "Капский варан",
        "Аллигатор миссисипский",
        "Морская игуана",
        "Хамелеон",
        "Красная панда",
        "Колибри",
        "Киви",
        "Горилла",
        "Африканский слон",
        "Галапагосская черепаха",
        "Лев",
        "Оса-наездник",
        "Павлин",
        "Коралл мозговик",
        "Стрекоза",
        "Капибара",
        "Светлячок",
        "Гигантская амёба",
        "Божья коровка",
        "Сова полярная",
        "Большая белая акула",
        "Манта",
        "Пингвин Адели",
        "Рыба-клоун",
        "Пчела медоносная",
        "Синий кит",
    ]

    index = ((today - start_date).days + offset) % len(species)
    blogger = BestiaryBlogger(species[index])
    blogger.post()

if __name__ == "__main__":
    post()