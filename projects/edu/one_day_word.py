import json, datetime
from simple_blogger.poster.telegram import TelegramPoster
from simple_blogger.poster.vk import VkPoster
from simple_blogger.blogger import Journalist
from simple_blogger.preprocessor.text import TagAdder
from simple_blogger.generator.deepseek import DeepSeekTextGenerator

class WordBlogger(Journalist):
    # def _system_prompt(self):
    #     return 'Ты - знаток русского языка, интересуешься новыми словами, знаешь значения старомодных слов, их этимологию и интересные факты, связанные со словами'
    
    def _message_generator(self):
        return DeepSeekTextGenerator('Ты - знаток русского языка. Я дам тебе слово и категорию. Объясни значение слова. Используй структуру: слово, пример использования, интересный факт о слове. Используй смайлики и не более 150 слов')
    
    def _prompt_constructor(self, _):
        return f"'{self.task['word']}', '{self.task['category']}'"

    def __init__(self, task):
        self.task = task
        tagadder = TagAdder(['#новыеслова', '#развитие', f"#{task['category']}"])
        posters = [
            TelegramPoster(chat_id='@one_day_word', processor=tagadder),
            VkPoster(group_id='230174990', processor=tagadder)
            # TelegramPoster(processor=tagadder)
        ]
        super().__init__(posters)


def post(offset=0):
    start_date = datetime.date(2025, 8, 8)
    today = datetime.date.today()
    tasks = json.load(open("./files/edu/one_day_word.json", "rt", encoding="UTF-8"))
    index = ((today - start_date).days + offset) % len(tasks)
    blogger = WordBlogger(tasks[index])
    blogger.post()

if __name__ == "__main__":
    post()