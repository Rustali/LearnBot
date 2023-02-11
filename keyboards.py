from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton


# создаем кнопку, обязательный параметр для KeyboardButton - это текст,
# который будет отправляться при нажатии на кнопку
button_hi = KeyboardButton('Привет! 👋')

# создаем объект класса ReplyKeyboardMarkup и добавляем кнопку с помощью метода add
greet_kb = ReplyKeyboardMarkup()
greet_kb.add(button_hi)

# создаем новую клавиатуру, добавив параметр уменьшить размер
greet_kb1 = ReplyKeyboardMarkup(resize_keyboard=True).add(button_hi)

# создаем новую клавиатуру, которая будет скрыта после нажатия
greet_kb2 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button_hi)

# Создаем несколько кнопок
button1 = KeyboardButton('1️⃣')
button2 = KeyboardButton('2️⃣')
button3 = KeyboardButton('3️⃣')

# Генерируем несколько разных клавиатур
# Метод add принимает в себя любое количество кнопок, всегда начинает добавление
# с новой строки и переносит ряд при достижении значения установленной ширины.
markup3 = ReplyKeyboardMarkup().add(button1).add(button2).add(button3)

# Метод row тоже принимает любое количество, но при этом не переносит кнопки
# на новый ряд, а добавляет всё полученное в одну строчку.
markup4 = ReplyKeyboardMarkup().row(button1, button2, button3)

markup5 = ReplyKeyboardMarkup().row(button1, button2, button3).add(
    KeyboardButton('Средний ряд'))

button4 = KeyboardButton('4️⃣')
button5 = KeyboardButton('5️⃣')
button6 = KeyboardButton('6️⃣')

markup5.row(button4, button5)

# Метод insert работает по схеме схожей с add, но только начинает добавлять
# к последнему ряду. И только если там уже достигнута максимальная ширина,
# начинает новую строку.
markup5.insert(button6)

# Добавляем кнопки отправки своего контакта и геопозиции
markup_request = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton('Отправить свой контакт ☎️', request_contact=True)).add(
    KeyboardButton('Отправить свою локацию 🗺️', request_location=True)
)

# Добавляем все кнопки вместе
markup_big = ReplyKeyboardMarkup()

markup_big.add(button1, button2, button3, button4, button5, button6)
markup_big.row(button1, button2, button3, button4, button5, button6, button1, button2, button3, button4, button5, button6)

markup_big.row(button4, button2)
markup_big.add(button3, button2)
markup_big.insert(button1)
markup_big.insert(button6)
markup_big.insert(KeyboardButton('9️⃣'))

# создаем кнопку для инлайн клавиатуры
inline_btn_1 = InlineKeyboardButton('Первая кнопка!', callback_data='button1')
# создаем инлайн клавиатуру и добавляем кнопку
inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1)

inline_kb_full = InlineKeyboardMarkup(row_width=2).add(inline_btn_1)
inline_kb_full.add(InlineKeyboardButton('Вторая кнопка', callback_data='btn2'))
inline_btn_3 = InlineKeyboardButton('кнопка 3', callback_data='btn3')
inline_btn_4 = InlineKeyboardButton('кнопка 4', callback_data='btn4')
inline_btn_5 = InlineKeyboardButton('кнопка 5', callback_data='btn5')
inline_kb_full.add(inline_btn_3, inline_btn_4, inline_btn_5)
inline_kb_full.row(inline_btn_3, inline_btn_4, inline_btn_5)
inline_kb_full.insert(InlineKeyboardButton("query=''", switch_inline_query=''))
inline_kb_full.insert(InlineKeyboardButton("query='qwerty'", switch_inline_query='qwerty'))
inline_kb_full.insert(InlineKeyboardButton("Inline в этом же чате", switch_inline_query_current_chat='wasd'))
inline_kb_full.add(InlineKeyboardButton('Уроки aiogram', url='https://surik00.gitbooks.io/aiogram-lessons/content/'))
