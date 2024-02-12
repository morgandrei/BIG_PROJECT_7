import requests
from django.conf import settings

token = settings.TELEGRAM_BOT_TOKEN
chat_id = settings.TELEGRAM_CHAT_ID


def handle(message):  # функция отправки собщения в чат
    url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
    requests.get(url).json()
