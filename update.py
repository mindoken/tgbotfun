from telegram import *
from telegram.ext import  ContextTypes,ConversationHandler
import sqlalchemy as db
from db import members,connection,engine
from pathlib import Path

UPDATE,SHOW_FORM =range(2)

async def update_gender(update: Update,context: ContextTypes.DEFAULT_TYPE):
    reply_keyboard = [["Парень", "Девушка", "Другое"]]
    await update.message.reply_text("Какой ваш пол?",
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder="?"
        ),
    )

    return UPDATE    

async def set_update_gender(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_gender = update.message.text
    update_query = db.update(members).where(members.columns.tg_chat_id == update.effective_chat.id).values(gender = user_gender)
    connection.execute(update_query)
    connection.commit()
    reply_keyboard = [["ДА","НЕТ"]]

    await update.message.reply_text("Хотите посмотреть результат?",
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder="?"
        ),
    )

    return SHOW_FORM

async def update_age(update: Update,context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id,text="Сколько вам лет?")

    return UPDATE

async def set_update_age(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_age = int(update.message.text)
    update_query = db.update(members).where(members.columns.tg_chat_id == update.effective_chat.id).values(age = user_age)
    connection.execute(update_query)
    connection.commit()
    reply_keyboard = [["ДА","НЕТ"]]

    await update.message.reply_text("Хотите посмотреть результат?",
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder="?"
        ),
    )

    return SHOW_FORM

async def update_name(update: Update,context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id,text="Как вас зовут?")

    return UPDATE

async def set_update_name(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_name = update.message.text
    update_query = db.update(members).where(members.columns.tg_chat_id == update.effective_chat.id).values(name = user_name)
    connection.execute(update_query)
    connection.commit()
    reply_keyboard = [["ДА","НЕТ"]]

    await update.message.reply_text("Хотите посмотреть результат?",
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder="?"
        ),
    )

    return SHOW_FORM

async def update_faculty(update: Update,context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id,text="На каком факультете вы учитесь?")

    return UPDATE

async def set_update_faculty(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_faculty = update.message.text
    update_query = db.update(members).where(members.columns.tg_chat_id == update.effective_chat.id).values(faculty = user_faculty)
    connection.execute(update_query)
    connection.commit()
    reply_keyboard = [["ДА","НЕТ"]]

    await update.message.reply_text("Хотите посмотреть результат?",
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder="?"
        ),
    )

    return SHOW_FORM

async def update_networking(update: Update,context: ContextTypes.DEFAULT_TYPE):
    reply_keyboard = [["ДА","НЕТ"]]
    await update.message.reply_text("Интересует ли вас нетворкинг?",
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder="?"
        ),
    )

    return UPDATE

async def set_update_networking(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text=="ДА":    
        user_networking = True
    else:
        user_networking = False
    update_query = db.update(members).where(members.columns.tg_chat_id == update.effective_chat.id).values(networking = user_networking)
    connection.execute(update_query)
    connection.commit()
    reply_keyboard = [["ДА","НЕТ"]]

    await update.message.reply_text("Хотите посмотреть результат?",
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder="?"
        ),
    )

    return SHOW_FORM

async def update_friendship(update: Update,context: ContextTypes.DEFAULT_TYPE):
    reply_keyboard = [["ДА","НЕТ"]]
    await update.message.reply_text("Ищите ли вы дружбу?",
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder="?"
        ),
    )

    return UPDATE

async def set_update_friendship(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text=="ДА":    
        user_friendship = True
    else:
        user_friendship = False
    update_query = db.update(members).where(members.columns.tg_chat_id == update.effective_chat.id).values(friendship = user_friendship)
    connection.execute(update_query)
    connection.commit()
    reply_keyboard = [["ДА","НЕТ"]]

    await update.message.reply_text("Хотите посмотреть результат?",
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder="?"
        ),
    )

    return SHOW_FORM

async def update_relationship(update: Update,context: ContextTypes.DEFAULT_TYPE):
    reply_keyboard = [["ДА","НЕТ"]]
    await update.message.reply_text("Интересует ли вас отношения?",
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder="?"
        ),
    )

    return UPDATE

async def set_update_relationship(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text=="ДА":    
        user_relationship = True
    else:
        user_relationship = False
    update_query = db.update(members).where(members.columns.tg_chat_id == update.effective_chat.id).values(relationship = user_relationship)
    connection.execute(update_query)
    connection.commit()
    reply_keyboard = [["ДА","НЕТ"]]

    await update.message.reply_text("Хотите посмотреть результат?",
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder="?"
        ),
    )

    return SHOW_FORM

async def update_help(update: Update,context: ContextTypes.DEFAULT_TYPE):
    reply_keyboard = [["ДА","НЕТ"]]
    await update.message.reply_text("Нужна ли вам помощь?",
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder="?"
        ),
    )

    return UPDATE

async def set_update_help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text=="ДА":    
        user_help = True
    else:
        user_help = False
    update_query = db.update(members).where(members.columns.tg_chat_id == update.effective_chat.id).values(help = user_help)
    connection.execute(update_query)
    connection.commit()

    return SHOW_FORM

async def update_chatting(update: Update,context: ContextTypes.DEFAULT_TYPE):
    reply_keyboard = [["ДА","НЕТ"]]
    await update.message.reply_text("Хотите ли вы с кем-нибудь побеседовать?",
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder="?"
        ),
    )

    return UPDATE
    
async def set_update_chatting(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text=="ДА":    
        user_chatting = True
    else:
        user_chatting = False
    engine.connect()
    update_query = db.update(members).where(members.columns.tg_chat_id == update.effective_chat.id).values(networking = user_chatting)
    connection.execute(update_query)
    connection.commit()
    reply_keyboard = [["ДА","НЕТ"]]

    await update.message.reply_text("Хотите посмотреть результат?",
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder="?"
        ),
    )

    return SHOW_FORM

async def update_photo(update:Update,context:ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id,text="Пришлите ваше фото")

    return UPDATE

async def set_update_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    photo_file = await update.message.photo[-1].get_file()
    photo_path = Path("photo",f'{update.effective_chat.id}.jpg')
    await photo_file.download_to_drive(photo_path)
    user_photo = f'{update.effective_chat.id}.jpg'
    update_query = db.update(members).where(members.columns.tg_chat_id == update.effective_user.id).values(photo = user_photo)
    connection.execute(update_query)
    connection.commit()
    reply_keyboard = [["ДА","НЕТ"]]

    await update.message.reply_text("Хотите посмотреть результат?",
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder="?"
        ),
    )

    return SHOW_FORM

async def update_bio(update: Update,context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id,text="Расскажи что-нибудь о себе:)")
    return UPDATE
    
async def set_update_bio(update:Update, context:ContextTypes.DEFAULT_TYPE):
    user_bio = update.message.text
    update_query = db.update(members).where(members.columns.tg_chat_id == update.effective_chat.id).values(bio = user_bio)
    connection.execute(update_query)
    connection.commit()
    reply_keyboard = [["ДА","НЕТ"]]

    await update.message.reply_text("Хотите посмотреть результат?",
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder="?"
        ),
    )

    return SHOW_FORM

async def show_update_form(update: Update, context:ContextTypes.DEFAULT_TYPE):
    if update.message.text=="НЕТ":    
        pass
    else:
        select_query= db.select( members.columns.name ).where(members.columns.tg_chat_id == update.effective_chat.id)
        select_result=connection.execute(select_query)
        connection.commit()
        name_result=str(select_result.fetchall()[0][0])

        select_query= db.select( members.columns.age ).where(members.columns.tg_chat_id == update.effective_chat.id)
        select_result=connection.execute(select_query)
        connection.commit()
        age_result=str(select_result.fetchall()[0][0])

        select_query= db.select( members.columns.faculty ).where(members.columns.tg_chat_id == update.effective_chat.id)
        select_result=connection.execute(select_query)
        connection.commit()
        faculty_result=str(select_result.fetchall()[0][0])

        select_query= db.select( members.columns.bio ).where(members.columns.tg_chat_id == update.effective_chat.id)
        select_result=connection.execute(select_query)
        connection.commit()
        bio_result=str(select_result.fetchall()[0][0])

        select_query= db.select( members.columns.photo ).where(members.columns.tg_chat_id == update.effective_chat.id)
        select_result=connection.execute(select_query)
        connection.commit()
        photo_path=(select_result.fetchall()[0][0])
        photo_path = Path("photo",photo_path) 

        select_query= db.select( members.columns.networking ).where(members.columns.tg_chat_id == update.effective_chat.id)
        select_result=connection.execute(select_query)
        connection.commit()
        if select_result.fetchall()[0][0]==True:
            networking_result="Нетворкинг"
        else:
            networking_result=""

        select_query= db.select( members.columns.friendship ).where(members.columns.tg_chat_id == update.effective_chat.id)
        select_result=connection.execute(select_query)
        connection.commit()
        if select_result.fetchall()[0][0]==True:
            friendship_result="Дружба"
        else:
            friendship_result=""

        select_query= db.select( members.columns.relationship ).where(members.columns.tg_chat_id == update.effective_chat.id)
        select_result=connection.execute(select_query)
        connection.commit()
        if select_result.fetchall()[0][0]==True:
            relationship_result="Отношения"
        else:
            relationship_result=""

        select_query= db.select( members.columns.help ).where(members.columns.tg_chat_id == update.effective_chat.id)
        select_result=connection.execute(select_query)
        connection.commit()
        if select_result.fetchall()[0][0]==True:
            help_result="Помощь"
        else:
            help_result=""

        select_query= db.select( members.columns.chatting ).where(members.columns.tg_chat_id == update.effective_chat.id)
        select_result=connection.execute(select_query)
        connection.commit()
        if select_result.fetchall()[0][0]==True:
            chatting_result="Общение"
        else:
            chatting_result=""

        form=f'Твоя анкета: \n{networking_result} {friendship_result} {relationship_result} {help_result} {chatting_result}\n{name_result},{age_result},{faculty_result}\n {bio_result}'
        
        if name_result=="":
            await context.bot.send_message(chat_id=update.effective_chat.id,text=form)
        else:
            await context.bot.send_photo(chat_id=update.effective_chat.id,photo=photo_path,caption=form)

    
    return ConversationHandler.END
