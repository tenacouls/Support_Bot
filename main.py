import sqlite3
from typing import Final
from telegram import Update, Bot
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = '6332766112:AAEjq_fSBrHXA5WdMKFm_3zpIrVxQ4mvxw4'
BOT_USERNAME: Final = "@DocrobotSupport_bot"

#db_path = '/home/makeouthill/BOT_DB/Clients_DataBase'
#conn = sqlite3.connect(db_path)
#cursor = conn.cursor()

#Описание команд для (start,help custom)
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    await update.message.reply_text('Добрый день! Спасибо, что обратились за поддержкой именно ко мне, буду рад помочь вам, прошу, введите ваш ИНН чтобы я мог знать какой организации требуется моя помощь')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    await update.message.reply_text('Я могу выполнять следующие функции!')
    
async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    await update.message.reply_text('Здесь будет доп описание')

    
# Ответы от бота на сообщения пользователя

def handle_response(text: str) -> str:
    processed: str = text.lower()
    
    if 'привет' in processed:
        return 'Добрый день!'
    
    return 'Пока я не понимаю данные запросы'
    
    """
    try:
        inn: int = update.message.chat.type
    except ValueError:
        update.message.reply_text('Введите корректное число.')
        return
    try:
        cursor.execute('SELECT Comp_Name FROM Companys WHERE id=?', (inn,))
        row = cursor.fetchone()

        if row is not None:
            update.message.reply_text('Организация ' + row[0] + ' успешно обнаружена')
        else:
            update.message.reply_text('Организация не найдена')

    except sqlite3.Error as e:
        update.message.reply_text('Произошла ошибка при обработке вашего запроса.')
        print('Ошибка:', e)
    
    updater = Update(TOKEN, use_context=True)
    """

# Ответ от бота при если он числится в груповом чате.
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    message_type: str = update.message.chat.type
    text: str = update.message.text
    
    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')
    
    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response :str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)
    print('Bot', response)
    await update.message.reply_text(context)
    
#Обработка ошибок
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'{update} cause of error {context.error}')
    
    
if __name__ == '__main__':
    print('Бот Запускается...')
    app = Application.builder().token(TOKEN).build()
    
    # Команды
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))
    
    #Сообщения
    
    app.add_handler(MessageHandler(filters.TEXT, handle_message))
    
    #Ошибки
    app.add_error_handler(error)
    
    
    #Проверка новых сообщений
    print ('Проверяю сообщения')
    app.run_polling(poll_interval=3)