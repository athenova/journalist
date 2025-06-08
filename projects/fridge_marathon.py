from simple_blogger.poster.telegram import TelegramPoster
from simple_blogger.poster.vk import VkPoster
from simple_blogger.blogger import Journalist
from simple_blogger.preprocessor.text import TagAdder
from simple_blogger.generator.openai import OpenAiTextGenerator
from simple_blogger.generator.deepseek import DeepSeekTextGenerator
import datetime

class FridgeMarathoner(Journalist):
    # def _system_prompt(self):
    #     return self.system_prompt

    def _message_generator(self):
        return OpenAiTextGenerator(self.system_prompt)
    
    def _prompt_constructor(self, _):
        return self.prompt_constructor

    def __init__(self, system_prompt, prompt_constructor, tags):
        self.system_prompt = system_prompt
        self.prompt_constructor = prompt_constructor
        tagadder = TagAdder(tags)
        posters = [
            TelegramPoster(chat_id='@fridgemarathon', processor=tagadder),
            VkPoster(group_id='230800710', processor=tagadder)
            # TelegramPoster(processor=tagadder)
        ]
        super().__init__(posters)

def post(day=None):
    system_prompt="Ты - начинающий бегун, блогер с 1000000 подписчиков, которых ты называешь 'танки' и 'улитки'. У тебя лишний вес, отличное чувство юмора и позитивный настрой по жизни. Ты бегаешь, чтобы есть, и ешь, чтобы бегать" 
    match day or datetime.date.today().weekday():
        case 0:
            blogger = FridgeMarathoner(
                system_prompt, 
                "Расскажи, как ты выглядишь на тренировках. Посмейся над собой, не комплексуй, расскажи почему очень круто быть тобой. Используй смайлики и не более 150 слов. Не используй 'Окей' и 'Конечно'",
                ['#Марафон', '#Холодильник', '#СпортДляВсех', '#ТелоСлучайностьДухРешает']
            )
        case 1:
            blogger = FridgeMarathoner(
                system_prompt, 
                "Расскажи про свою маленькую победу на тренировке. Используй смайлики и не более 150 слов. Не используй 'Окей' и 'Конечно'",
                ['#Марафон', '#Холодильник', '#СпортДляВсех', '#ПобедаНаВесахДуши']
            )
        case 2:
            blogger = FridgeMarathoner(
                system_prompt, 
                "Расскажи про профилактику травм бегунов с лишним весом. Используй смайлики и не более 150 слов. Не используй 'Окей' и 'Конечно'",
                ['#Марафон', '#Холодильник', '#СпортДляВсех', '#БегБезСлез']
            )
        case 3:
            blogger = FridgeMarathoner(
                system_prompt, 
                "Выбери актуальную в беговом сообществе тему. Посмейся над ней. Расскажи, почему она для тебя актуальна. Используй смайлики и не более 150 слов. Не используй 'Окей' и 'Конечно'",
                ['#Марафон', '#Холодильник', '#СпортДляВсех', '#БегПротивСтереотипов']
            )
        case 4:
            blogger = FridgeMarathoner(
                system_prompt, 
                "Расскажи про тренировку, которая сделала тебя лучше. Фокус на здоровье, а не на весах. Используй смайлики и не более 150 слов. Не используй 'Окей' и 'Конечно'",
                ['#Марафон', '#Холодильник', '#СпортДляВсех', '#НеВесАЖизнь']
            )
        case 5:
            blogger = FridgeMarathoner(
                system_prompt, 
                "Сегодня чит-мил день. Выбери блюдо с высоким содержанием сахара или углеводов. Расскажи его историю и о том, как ты, смакуя, съел его после тренировки. Используй смайлики и не более 150 слов. Не используй 'Окей' и 'Конечно'",
                ['#Марафон', '#Холодильник', '#СпортДляВсех', '#НабегалНаСъел']
            )
        case 6:
            blogger = FridgeMarathoner(
                system_prompt, 
                "Придумай креативную, смешную отмазку, почему ты прибежал последним на групповой тренировке. Используй смайлики и не более 150 слов. Не используй 'Окей' и 'Конечно'",
                ['#Марафон', '#Холодильник', '#СпортДляВсех', '#БегДляДушиАНеДляПодиума']
            )
    blogger.post()

if __name__ == "__main__":
    post()