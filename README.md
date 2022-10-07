# api_final_yatube

Документация в формате Redoc.
http://127.0.0.1:8000/redoc/

Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:

https://github.com/zotov001/api_final_yatube.git
cd api_final_yatube

Cоздать и активировать виртуальное окружение (mac os):

python3 -m venv venv
source venv/bin/activate
python3 -m pip install --upgrade pip

Установить зависимости из файла requirements.txt:

pip install -r requirements.txt

Выполнить миграции:

python3 manage.py migrate

Запустить проект:

python3 manage.py runserver