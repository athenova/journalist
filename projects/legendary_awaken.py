from simple_blogger.poster.telegram import TelegramPoster
from simple_blogger.poster.instagram import InstagramPoster
from simple_blogger.poster.vk import VkPoster
from simple_blogger.blogger import Journalist
from simple_blogger.preprocessor.text import TagAdder
from simple_blogger.generator.openai import OpenAiTextGenerator

class LuxNexusBlogger(Journalist):
    def _message_generator(self):
        return OpenAiTextGenerator("Ты - блоггер-эзотерик с 1000000 подписчиков")
    
    def _prompt_constructor(self, _):
        return "Опиши рандомного просветлённого. Расскажи про него, приведи интересный факт, связанный с ним. Используй смайлики и не более 150 слов. Не используй 'Окей' и 'Конечно'"

    def __init__(self):
        tagadder = TagAdder(['#гармония', '#светвнутри', '#легенды'])
        posters = [
            TelegramPoster(chat_id='@lux_nexus', processor=tagadder),
            VkPoster(group_id='229822258', processor=tagadder),
            # InstagramPoster(account_token_name='LUX_NEXUS_TOKEN', processor=tagadder)
            # TelegramPoster(processor=tagadder)
        ]
        super().__init__(posters)


def post():
    blogger = LuxNexusBlogger()
    blogger.post()

if __name__ == "__main__":
    post()