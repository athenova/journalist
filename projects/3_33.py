from email.errors import MessageError
from simple_blogger.poster.vk import VkPoster
from simple_blogger.generator.deepseek import DeepSeekTextGenerator
from simple_blogger.generator.openai import GptImageGenerator
from simple_blogger.preprocessor.text import TagAdder
from simple_blogger.blogger import Journalist
from simple_blogger.preprocessor.text import ITextProcessor, SerialProcessor
import json, re
from datetime import date

class OkCleaner(ITextProcessor):        
    def process(self, message:str)->str:
        if re.match(r'\Aконечно|ок', message, re.IGNORECASE):
            message = re.sub(r'\A[^.!&]+.', '', message)
        return re.sub(r'\A\s+', '', message)

class HorrorWriter(Journalist):
    def _message_generator(self):
        # return OpenAiTextGenerator("Ты - писатель. Специализируешься на хоррорах. Я буду давать тебе тему, жанр и автора. Придумай небольшой хоррор-рассказ на заданную тему, в заданном жанре, в стиле заданного автора.")
        return DeepSeekTextGenerator("Ты - писатель. Специализируешься на хоррорах. Я буду давать тебе тему, жанр и автора. Придумай небольшой хоррор-рассказ на заданную тему, в заданном жанре, в стиле заданного автора.")
    
    def _image_generator(self):
        return GptImageGenerator(api_key_name="GPT_API_KEY", system_prompt="Нарисуй обложку для рассказа")
    
    def _prompt_constructor(self, _):
        return f"{self.task['theme']}, {self.task['genre']}, {self.author['author']}"

    def __init__(self, task, author):
        self.task = task
        self.author = author
        tagadder = TagAdder(['#at_3_33am', '#ужасы', f"#{task["genre"].replace(' ', '').replace('-', '')}".lower()])
        posters = [
            # VkPoster(processor=SerialProcessor([OkCleaner(), tagadder]))
            VkPoster(group_id='232393870', processor=SerialProcessor([OkCleaner(), tagadder]))
        ]
        super().__init__(posters)

def post(offset=0):
    today = date.today()
    start_date = date(2025, 8, 31)
    index =  (today - start_date).days + offset
    tasks = json.load(open(f"./files/3_33/3_33_themes.json", "rt", encoding="UTF-8"))
    authors = json.load(open(f"./files/3_33/3_33_authors.json", "rt", encoding="UTF-8"))
    blogger = HorrorWriter(task=tasks[index % len(tasks)], author=authors[index % len(authors)])
    blogger.post()

if __name__ == "__main__":
    post()