from simple_blogger.poster.vk import VkPoster
from simple_blogger.blogger import SimplestBlogger
from simple_blogger.builder import PostBuilder
from simple_blogger.builder.content import ContentBuilder
from simple_blogger.generator.deepseek import DeepSeekTextGenerator
from simple_blogger.preprocessor.text import TagAdder
from simple_blogger.builder.prompt import IdentityPromptBuilder
import json
from datetime import date

def old_post(task, author):
    processor = TagAdder(['#at_3_33am', '#ужасы', f"#{task["genre"].replace(' ', '').replace('-', '')}".lower()])

    blogger = SimplestBlogger(
        builder = PostBuilder(
                message_builder=ContentBuilder(
                    generator=DeepSeekTextGenerator(system_prompt='Ты - писатель. Специализируешься на хоррорах. Я буду давать тебе тему, жанр и автора. Придумай небольшой хоррор-рассказ на заданную тему, в заданном жанре, в стиле заданного автора.'),
                    prompt_builder=IdentityPromptBuilder(f"{task['theme']}, {task['genre']}, {author['author']}")
                )
            ),
        posters = [
                # VkPoster(processor=processor)
                VkPoster(group_id='232393870', processor=processor)
            ]
    )

    blogger.post()

def post(offset=0):
    today = date.today()
    start_date = date(2025, 8, 31)
    index =  (today - start_date).days + offset
    tasks = json.load(open(f"./files/3_33/3_33_themes.json", "rt", encoding="UTF-8"))
    authors = json.load(open(f"./files/3_33/3_33_authors.json", "rt", encoding="UTF-8"))
    old_post(task=tasks[index % len(tasks)], author=authors[index % len(authors)])

if __name__ == "__main__":
    post()