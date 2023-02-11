# Installing

1. Перейти в каталог, куда будет клонирован проект

2. Клонировать репозиторий с гита \
git clone ...

3. Создать виртуальное окружение \
python3 -m venv venv

4. Активировать виртуальное окружение \
source venv/bin/activate

5. Установить зависимости из requerements.txt \
pip install -r requerements.txt

6. Создать в проекте файл congig.py и прописать в него три аргумента: \
TOKEN = "сюда вписать токен своего бота" \
MY_ID = сюда вписать свой ID в телеграме \
DB_FILENAME = 'botuploads.db' \

7. Запустить бота \
python bot_lesson_2.py (отправка медиафайлов, шрифты и эмоджи)\
или \
python bot_lesson_5.py (кнопки в боте)