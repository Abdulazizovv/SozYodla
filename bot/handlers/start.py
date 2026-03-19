from bot.loader import bot
from telebot import types
from botapp.models import BotUser
from main.models import Subject, Word


@bot.message_handler(commands=["start"])
def start_handler(message: types.Message):
    user, created = BotUser.objects.update_or_create(
        defaults={
            "username": message.from_user.username,
            "first_name": message.from_user.first_name,
            "last_name": message.from_user.last_name
        },
        chat_id=message.from_user.id
    )
    words_count = Word.objects.count()
    subjects_count = Subject.objects.count()
    
    text =  f"Bot sizga so'zlarni yod olishga yordam beradi\n"\
            f"Mavjud so'zlar soni: {words_count}\n"\
            f"Tillar soni: {subjects_count}"

    bot.send_message(message.chat.id, text)