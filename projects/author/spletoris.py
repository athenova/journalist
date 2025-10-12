from simple_blogger.poster.telegram import TelegramPoster
from simple_blogger.poster.vk import VkPoster
from simple_blogger.blogger import SimplestBlogger
from simple_blogger.builder import PostBuilder
from simple_blogger.builder.content import ContentBuilder
from simple_blogger.generator.deepseek import DeepSeekTextGenerator
from simple_blogger.preprocessor.text import TagAdder
from simple_blogger.builder.prompt import IdentityPromptBuilder
from datetime import date
import json

class GossipBlogger(SimplestBlogger):
    def __init__(self, task):
        builder = PostBuilder(
            message_builder=ContentBuilder(
                generator=DeepSeekTextGenerator(system_prompt='Ты - исторический папарацци, автор канала «Гусиное перо сплетницы», женщина. Я буду давать тебе историческую личность. Расскажи известный слух интимного характера о ней как если бы это случилось вчера в стиле желтой прессы.'),
                prompt_builder=IdentityPromptBuilder(f"{task['person']}")
            )
        )
        processor = TagAdder(['#скандалы', '#сплетни', '#история'])
        posters = [
            # VkPoster(group_id=232292207, processor=processor)
            TelegramPoster(processor=processor)
        ]
        super().__init__(builder, posters)

def post(offset = 0):
    tasks = json.load(open("./files/author/spletoris.json", "rt", encoding="UTF-8"))
    start_date = date(2025, 8, 28)
    today = date.today()
    index = ((today - start_date).days + offset) % len(tasks)
    blogger = GossipBlogger(task=tasks[index])
    blogger.post()

if __name__ == "__main__":
    post()