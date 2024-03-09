"""Пример работы с чатом через gigachain"""
from langchain.schema import HumanMessage, SystemMessage
from langchain.chat_models.gigachat import GigaChat

# Авторизация в сервисе GigaChat
chat = GigaChat(credentials='*', verify_ssl_certs=False)

messages = [
    SystemMessage(
        content='Ты чат-бот помощник. Твоя задача - переделывать текст для сообщетсва "Ultimate News". Аудитория - '
                'люди от 13 до 27 лет. Тон - свободный, спокойный, захватывающий. Необходимо разделять текст '
                'пустыми строчками. Так же, можешь добавлять смайлики для привлечения внимания. '
                'Вот текст: ')
]


def get_answer(message: str):
    messages.append(HumanMessage(content=message))
    res = chat(messages)
    messages.append(res)

    return res.content

