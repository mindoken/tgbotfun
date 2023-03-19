# DSTU ConnectBot 
## Описание:
Телеграмм-бот , созданный для быстрого поиска полезных знакомств в любимом университете: 
-Поиск товарищей для реализации своих задумок, проектов или команды для хакатона;
-Поиск интересных собеседников , среди других прекрасных личностей;
-Поиск той самой второй половинки, с которой вы напишите прекрасный диплом и нарожаете много прекрасных номеров для студ весны.
На данный момент реализовано:
- создание/удаление собственной анкеты
- поиск и просмотр чужих анкет
- отправка заявки другому пользователю
- изменение всех параметров собственной анкеты

## Технологии в проекте:
Проект написан на Python 3 c использованием таких библиотек как:python-telegram-bot,sqlalchemy,random,pathlib.

## Техническое описание проекта:

проект предлагается в **исходном коде**. 
**Исходный код** состоит из запускающего файла - **main.py**
- **Файл run.py** -   файл запуска телеграм-бота
- **Файл utils.py**  -  файл с основными методами, такими как создание анкеты и тому подобное
- **Файл update.py** - файл с методами обновления данных
- **Файл search.py** - файл с методами взаимодействия с другими анкетами
- **Файл db.py** - файл инициализирующих работу БД

Так же **обязательными** является папка **photo**, в которой хранятся фотографии анкет и файл самой БД **members-sqlalchemy.db**, в которой хранятся сами анкеты пользователей

## Инструкция использования бота:

- перейдите в бота по ссылке https://t.me/m2_vkbot
- нажмите команду /start
- для создания анкеты напишите /create_form
- после создания анкеты вы можете ее посмотреть через /show_form
- для поиска других пользователей напишите /search_form , вам выдаст одну анкету. Для выдачи следующей анкеты напишите снова /search_form
- для того чтобы посмотреть полный функционал бота напишите /help

