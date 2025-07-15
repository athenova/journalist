from simple_blogger.poster.telegram import TelegramPoster
from simple_blogger.poster.vk import VkPoster
from simple_blogger.blogger import Journalist
from simple_blogger.preprocessor.text import TagAdder
from simple_blogger.generator.openai import OpenAiTextGenerator, GptImageGenerator
from simple_blogger.generator.deepseek import DeepSeekTextGenerator
import datetime, json

class GymCouch(Journalist):
    # def _system_prompt(self):
    #     return self.system_prompt

    def _message_generator(self):
        # return OpenAiTextGenerator(self.system_prompt)
        return DeepSeekTextGenerator(self.system_prompt)
    
    def _image_generator(self):
        return GptImageGenerator(api_key_name="GPT_API_KEY", system_prompt=self.image_prompt)
    
    def _prompt_constructor(self, _):
        return self.prompt_constructor

    def __init__(self, system_prompt, prompt_constructor, image_prompt, tags):
        self.system_prompt = system_prompt
        self.prompt_constructor = prompt_constructor
        self.image_prompt = image_prompt
        tagadder = TagAdder(tags)
        posters = [
            TelegramPoster(chat_id='@gymcouch', processor=tagadder),
            VkPoster(group_id='231578484', processor=tagadder)
            # TelegramPoster(processor=tagadder)
        ]
        super().__init__(posters)

def post(day=None):
    start_day = datetime.date(2025, 7, 15)
    today = datetime.date.today()
    day_count = (today - start_day).days
    index = day_count // 7
    system_prompt=f"Ты - начинающий атлет, блогер с 1000000 подписчиков. У тебя лишний вес, отличное чувство юмора и позитивный настрой по жизни. Это твой {day_count} день в тренажёрном зале. Ты тренируешься, чтобы есть, и ешь, чтобы тренироваться" 
    word_count = 150
    match day or (datetime.date.today().weekday() + 6) % 7:
        case 0:
            tasks = json.load(open("./files/gym_couch1.json", "rt", encoding="UTF-8"))
            index = index % len(tasks)
            task = tasks[index]
            blogger = GymCouch(
                system_prompt, 
                f"Расскажи про свою экипировку - {task['equip']}. Посмейся над собой, не комплексуй, расскажи почему очень круто быть тобой. Используй смайлики и не более {word_count} слов. Не используй 'Окей' и 'Конечно'",
                "Нарисуй человека по описанию",
                ['#Фитнес', '#Диван', '#СпортДляВсех', '#ТелоСлучайностьДухРешает']
            )
        case 1:
            blogger = GymCouch(
                system_prompt, 
                f"Расскажи про свою маленькую победу на тренировке. Используй смайлики и не более {word_count} слов. Не используй 'Окей' и 'Конечно'",
                "Нарисуй рисунок, вдохновлённый победой из описания",
                ['#Фитнес', '#Диван', '#СпортДляВсех', '#ПобедаНаВесахДуши']
            )
        case 2:
            tasks = json.load(open("./files/gym_couch3.json", "rt", encoding="UTF-8"))
            index = index % len(tasks)
            task = tasks[index]
            blogger = GymCouch(
                system_prompt, 
                f"Расскажи про профилактику травмы '{task['injury']}'. Используй смайлики и не более {word_count} слов. Не используй 'Окей' и 'Конечно'",
                "Нарисуй рисунок, вдохновлённый профилактикой травмы из описания, не рисуй текст",
                ['#Фитнес', '#Диван', '#СпортДляВсех', '#ТреняБезСлез']
            )
        case 3:
            tasks = json.load(open("./files/gym_couch4.json", "rt", encoding="UTF-8"))
            index = index % len(tasks)
            task = tasks[index]
            blogger = GymCouch(
                system_prompt, 
                f"Посмейся над темой '{task['theme']}'. Расскажи, почему она для тебя актуальна. Используй смайлики и не более {word_count} слов. Не используй 'Окей' и 'Конечно'",
                "Нарисуй рисунок, вдохновлённый темой из описания, не рисуй текст",
                ['#Фитнес', '#Диван', '#СпортДляВсех', '#ТреняПротивСтереотипов']
            )
        case 4:
            blogger = GymCouch(
                system_prompt, 
                f"Расскажи про тренировку, которая сделала тебя лучше. Фокус на здоровье, а не на весах. Используй смайлики и не более {word_count} слов. Не используй 'Окей' и 'Конечно'",
                "Нарисуй рисунок, вдохновлённый тренировкой из описания, не рисуй текст",
                ['#Фитнес', '#Диван', '#СпортДляВсех', '#НеВесАЖизнь']
            )
        case 5:
            tasks = json.load(open("./files/gym_couch6.json", "rt", encoding="UTF-8"))
            index = index % len(tasks)
            task = tasks[index]
            blogger = GymCouch(
                system_prompt, 
                f"Сегодня день чит-мил. Расскажи историю блюда '{task['food']}' и о том, как ты, смакуя, съел его после тренировки. Используй смайлики и не более {word_count} слов. Не используй 'Окей' и 'Конечно'",
                "Нарисуй блюдо из описания, не рисуй текст",
                ['#Фитнес', '#Диван', '#СпортДляВсех', '#НатренилНаСъел']
            )
        case 6:
            blogger = GymCouch(
                system_prompt, 
                f"Придумай креативную, смешную отмазку, почему ты не пришёл сегодня на тренировку. Используй смайлики и не более {word_count} слов. Не используй 'Окей' и 'Конечно'",
                "Нарисуй рисунок, вдохновлённый темой из описания, не рисуй текст",
                ['#Фитнес', '#Диван', '#СпортДляВсех', '#ТреняДляДушиАНеДляПодиума']
            )
    blogger.post()

if __name__ == "__main__":
    post()