import random, json
from simple_blogger.blogger import Journalist
from simple_blogger.poster.telegram import TelegramPoster
from simple_blogger.poster.vk import VkPoster
from simple_blogger.preprocessor.text import TagAdder
from simple_blogger.generator.openai import OpenAiTextGenerator, GptImageGenerator
from simple_blogger.poster.instagram import InstagramPoster
from datetime import date

tagadder = TagAdder(['#иллюстрации', '#фантазии'])

class Objectifised(Journalist):
    subjects = [
            "animal" ,
            "book" ,
            "browser" ,
            "car brand" ,
            "car model" ,
            "city" ,
            "computer" ,
            "game console" ,
            "cosmic ship" ,
            "country(as nation, not music)" ,
            "cpu" ,
            "fashion brand" ,
            "delivery company" ,
            "flower" ,
            "fruit" ,
            "computer game" ,
            "famous house" ,
            "insect" ,
            "it brand" ,
            "language" ,
            "mobile phone" ,
            "movie" ,
            "photo camera" ,
            "point of interest" ,
            "river" ,
            "ship" ,
            "sneakers" ,
            "song" ,
            "stadium" ,
            "tree" ,
            "vegetable" 
        ]
    
    def _prompt_constructor(self, _):
        return f"Опиши, как бы выглядел {self.task['group']} '{self.task['name']}', если бы был {self.subject}. Дай ответ на русском языке, используй не более 150 слов, используй смайлики, не используй 'Конечно' и 'Okей'"
    
    def _message_generator(self):
        return OpenAiTextGenerator('Ты - художник с образованием психолога', api_key_name="GPT_API_KEY")
    
    def _image_generator(self):
        return GptImageGenerator(api_key_name="GPT_API_KEY", system_prompt=f"Draw {self.subject} by description")
        
    def _posters(self):
        return [
            TelegramPoster(chat_id='@objectized_the', processor=tagadder),
            VkPoster(group_id='230297352', processor=tagadder),
            # InstagramPoster(account_token_name='OBJECTIZED_TOKEN', account_id=None, processor=tagadder)
            # TelegramPoster(processor=tagadder)
        ]

    def __init__(self, posters=None):
        tasks = json.load(open("./files/objectized.json", "rt", encoding="UTF-8"))
        today = date.today()
        random.seed(today.toordinal())
        self.subject = random.choice(Objectifised.subjects)
        # self.subject = "cosmic ship"
        first_post_date=date(2025, 4, 25)
        index = (today - first_post_date).days % len(tasks)
        self.task = tasks[index]
        # self.task = tasks[3]
        super().__init__(posters or self._posters())

def post():
    blogger = Objectifised()
    blogger.post()

if __name__ == "__main__":
    post()