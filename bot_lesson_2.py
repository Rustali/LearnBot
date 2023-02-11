# Урок по медиафайлам, шрифтам и эмоджи

import asyncio

from aiogram import Bot, types, Dispatcher, executor
from aiogram.types import ParseMode, InputMediaVideo, InputMediaPhoto, ChatActions, ContentType
# from aiogram.utils.emoji import emojize
from aiogram.utils.markdown import text, bold, italic, code, pre
from emoji import emojize

from config import TOKEN

CAT_BIG_EYES = 'AgACAgIAAxkDAAMhY-JLXyFU1KHfIydQzOejVQAB1t_mAAI0xTEboiEQS7QNfO2e45pJAQADAgADeAADLgQ'
KITTENS = [
    'AgACAgIAAxkDAAMfY-JLXqyX8AosorRGOq94ykO-C-UAAjLFMRuiIRBLYF7v3F4WvJsBAAMCAAN3AAMuBA',
    'AgACAgIAAxkDAAMcY-JLXdYJ-h616QJPTEZy_BnCpWIAAjHFMRuiIRBL1XAkPaIVZqEBAAMCAAN4AAMuBA',
    'AgACAgIAAxkDAAMgY-JLXovJhX4CKxLrddVthXiPiPIAAjPFMRuiIRBLxRoWmFRqxi0BAAMCAANtAAMuBA',
]
VOICE = 'AwACAgIAAxkDAAMdY-JLXUMM-tY26MKQBGzrjQeTxmQAAi8nAAKiIRBLjiw4yoX3tmcuBA'
VIDEO = 'BAACAgIAAxkDAAMiY-JLX6gSLTj_mXpIR6iZqP7IMWIAAjEnAAKiIRBLhdpgFwACuSsuBA'
TEXT_FILE = 'BQACAgIAAxkDAAMbY-JLXOYHgnQSwZm_L5aSqaCjXdAAAi4nAAKiIRBLqsrJpNUVLbQuBA'
VIDEO_NOTE = 'DQACAgIAAxkDAAMeY-JLXtgKgvm0DikS6kd0KdxirYAAAjAnAAKiIRBL1OZjB32-F50uBA'

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


# Создаем message_handler для команды /start
@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply(f"Привет {message.from_user.full_name}!\nИспользуй /help, чтобы узнать список доступных команд!")


# Создаем message_handler для команды /help
@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    # text склеивает в одно целое все передаваемые ей строчки, перемежая сепаратором
    # bold обрамляет входящую строчку метками для жирного текста (используется разметка Markdown)
    # italic обрамляет входящую строчку метками для курсивного текста
    # code обрамляет входящую строчку метками для текста в виде адреса (можно скопировать нажатием на него)
    # parse_mode=ParseMode.MARKDOWN указывает тип разметки
    msg = text(bold('Я могу ответить на следующие команды:'),
               '/voice', '/photo', '/group', '/note', '/file', '/testpre', sep='\n')
    await message.reply(msg, parse_mode=ParseMode.MARKDOWN)


# Отправка аудио + ответ на определенное сообщение
@dp.message_handler(commands=['voice'])
async def process_voice_command(message: types.Message):
    # reply_to_message_id отвечает за ответ на конкретное сообщение - айди можно указать любой доступный в этом чате
    # (хоть просто поставить единицу). В данном случае берем айди сообщения, которое вызвало эту функцию.
    await bot.send_voice(message.from_user.id, VOICE, reply_to_message_id=message.message_id)


# Отправка фото с комментарием + эмоджи
@dp.message_handler(commands=['photo'])
async def process_photo_command(message: types.Message):
    caption = 'Какие глазки! :eyes:'
    await bot.send_photo(message.from_user.id, CAT_BIG_EYES, caption=emojize(caption),
                         reply_to_message_id=message.message_id)


# Отправка медиагруппы (где смешались фото и видео)
@dp.message_handler(commands=['group'])
async def process_group_command(message: types.Message):
    # создаем массив и кладем в него один элемент типа InputMediaVideo.
    # Первый входной параметр - само видео (в данном случае айди),
    # а второй элемент - caption (его передавать не обязательно)
    media = [InputMediaVideo(VIDEO, caption='ежик и котятки')]
    for photo_id in KITTENS:
        # заполняем массив элементами типа InputMediaPhoto
        media.append(InputMediaPhoto(photo_id))
    await bot.send_media_group(message.from_user.id, media)


# Отправка видеозаметки (видео в кружочке)
@dp.message_handler(commands=['note'])
async def process_note_command(message: types.Message):
    user_id = message.from_user.id
    await bot.send_chat_action(user_id, ChatActions.RECORD_VIDEO_NOTE)      # показывает, что записывается видесообщение
    await asyncio.sleep(3)      # конвертируем видео и отправляем его пользователю
    await bot.send_video_note(user_id, VIDEO_NOTE)


# Отправка файла
@dp.message_handler(commands=['file'])
async def process_file_command(message: types.Message):
    user_id = message.from_user.id
    await bot.send_chat_action(user_id, ChatActions.UPLOAD_DOCUMENT)      # показывает, что отправляется файл
    await asyncio.sleep(3)      # скачиваем файл и отправляем его пользователю
    await bot.send_document(user_id, TEXT_FILE, caption='Этот файл специально для тебя!')


# Преформатированный текст
@dp.message_handler(commands=['testpre'])
async def process_testpre_command(message: types.Message):
    # отправляем преформатированный текст. Обычно такая разметка необходима при отправке блоков кода
    message_text = pre(emojize('''@dp.message_handler(commands=['testpre'])
async def process_testpre_command(message: types.Message):
    message_text = pre(emojize('Ха! Не в этот раз :face_with_tongue:'))
    await bot.send_message(message.from_user.id, message_text)'''))
    await bot.send_message(message.from_user.id, message_text, parse_mode=ParseMode.MARKDOWN_V2)


# Обработка текстового сообщения, отвечаем пользователю эхом (текст его сообщения)
@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)


@dp.message_handler(content_types=ContentType.ANY)
async def unknown_message(msg: types.Message):
    message_text = text(emojize('Я не знаю, что с этим делать :astonished_face:'),
                        italic('\nЯ просто напомню,'), bold('что есть'),
                        code('команда'), '/help')
    await msg.reply(message_text, parse_mode=ParseMode.MARKDOWN)


if __name__ == '__main__':
    executor.start_polling(dp)      # получаем сообщения от серверов Телеграм
