import time
import pytz
import telebot
from django.core.management.base import BaseCommand
from dotenv.main import load_dotenv
import os

from main.models import Contact

load_dotenv()

TELEGRAM_BOT_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
TELEGRAM_USER_ID = os.environ["TELEGRAM_USER_ID"]


class Command(BaseCommand):
    MESSAGE_COOLDOWN = 120

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # Правильный вызов конструктора родительского класса
        self.last_message_time = 0  # Инициализация времени последнего сообщения

    def add_arguments(self, parser):
        parser.add_argument('contact_id', type=int)

    def send_telegram_notification(self, contact_id, name, number, date):
        current_time = time.time()
        if current_time - self.last_message_time < self.MESSAGE_COOLDOWN:
            self.stdout.write(self.style.WARNING('Сообщение не отправлено: слишком частые отправки.'))
            return False

        bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)
        message = f'ID заявки - {contact_id},\nВремя заявки - {date.astimezone(pytz.timezone("Europe/Moscow")).strftime("%Y-%m-%d %H:%M:%S")},\nИмя клиента - {name},\nТелефон - {number}\n\n'
        bot.send_message(TELEGRAM_USER_ID, message)
        print(message)
        self.stdout.write(self.style.SUCCESS('Уведомление отправлено успешно!'))
        self.last_message_time = current_time
        return True

    def handle(self, *args, **options):
        contact_id = options['contact_id']
        try:
            contact = Contact.objects.get(id=contact_id)

            if self.send_telegram_notification(contact.id, contact.name, contact.number, contact.date):
                pass
            else:
                pass

        except Contact.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'Контакт с ID {contact_id} не найден.'))
