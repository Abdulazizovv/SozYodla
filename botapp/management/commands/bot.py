from django.core.management.base import BaseCommand
from bot.loader import bot
from bot import handlers



class Command(BaseCommand):
    help = 'Telegram-bot'

    def handle(self, *args, **options):
        pass

print("Bot ishga tushdi")
bot.infinity_polling()