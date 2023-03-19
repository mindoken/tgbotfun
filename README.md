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

## Инструкция запуска своего бота на примере запуска через хостинг Glitch: 
- В Telegram перейти в бот https://t.me/BotFather для создания и получения токена своего бота.
- написать данные команды в бота: **/start** , **/newbot** . 
- после этого пишем имя бота, а после этого его  username(это будет ссылкой на вашего бота),далее получаем такое сообщение:![image](https://user-images.githubusercontent.com/81232295/226204701-0e6f0dcd-4ad5-4d0e-a0ef-56db4a201a0c.png)
- в данном сообщении нас интересует следующий элемент, который мы копируем:![image](https://user-images.githubusercontent.com/81232295/226204788-49a8a01e-e320-43b6-acdd-bb5942eea76f.png)
-вставляем токен в файле **run.py** в 15 строку и сохраняем изменения в файле.
![image](https://user-images.githubusercontent.com/81232295/226204889-71370e29-2829-46f2-a83a-824463926e94.png)
- создаем собственный репозиторий на github с данными файлами проекта( но если хотите получить чистую базу данных, то удалите все изображения из папки photo и удалите БД **members-sqlalchemy.db**(не волнуйтесь, при запуске проекта создастся новая)) 
- заходим на сайт https://glitch.com/ , где регистрируемся.
- нажимаем в вверхнем правом углу кнопку **new project** и добавляем ссылку на ваш git-репозиторий.
- затем в нижней строчке находим терминал куда прописываем **pip3 install -r requirements. txt**.
- и для запуска проекта прописываем в том же терминале **python3 main.py**.
- ГОТОВО!
- далее следуем инструкции ниже.


## Инструкция использования  данного бота(отличие от использования вашего бота только в ссылке):

- перейдите в бота по ссылке https://t.me/m2_vkbot
- нажмите команду /start
- для создания анкеты напишите /create_form
- после создания анкеты вы можете ее посмотреть через /show_form
- для поиска других пользователей напишите /search_form , вам выдаст одну анкету. Для выдачи следующей анкеты напишите снова /search_form
- для того чтобы посмотреть полный функционал бота напишите /help

