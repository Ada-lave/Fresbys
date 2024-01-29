# Установка зависимостей проекта

**Этап I**

Для того что бы запустить проект необходимо создать виртуальное окружение python. Что бы его создать следует использовать команду *python -m venv venv*.

**Этап II**

не забудьте активировать виртуальное окружение с помощью команды *. venv/Scripts/activate* в дериктории проекта. после необходимо установить poetry. Сделать это можно с помощью команды *pip install poetry*

**Этап III**

Выполните команду *poetry install*.

**Этап IIII**

Необходимо выполнить команду *alembic upgrade head* для загрузки базы

# Запуск проекта

Для запуска проекта требуется выполнить команду *python main.py*
