from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext


def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Добрый день! Введите свою фамилию и имя на латинице (как в загранпаспорте):')


def receive_info(update: Update, context: CallbackContext) -> None:
    fullname = update.message.text
    context.user_data['fullname'] = fullname
    update.message.reply_text('Введите дату отправки самолета в формате ДД.ММ.ГГГГ:')


def receive_date(update: Update, context: CallbackContext) -> None:
    date = update.message.text
    context.user_data['date'] = date
    update.message.reply_text('Введите аэропорт отправления:')


def receive_departure(update: Update, context: CallbackContext) -> None:
    departure = update.message.text
    context.user_data['departure'] = departure
    update.message.reply_text('Введите аэропорт прибытия:')


def receive_arrival(update: Update, context: CallbackContext) -> None:
    arrival = update.message.text
    context.user_data['arrival'] = arrival

    # отправляем сообщение пользователю @developer_maxim с полученными данными
    message = f"ФИО: {context.user_data['fullname']}\nДата отправки: {context.user_data['date']}\nАэропорт отправления: {context.user_data['departure']}\nАэропорт прибытия: {context.user_data['arrival']}"
    context.bot.send_message(chat_id="@developer_maxim", text=message)


def main() -> None:
    updater = Updater("6284225440:AAHbFWdDCqTQrxwA2ucRjN7kqVrmvbtqaVA")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, receive_info))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, receive_date))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, receive_departure))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, receive_arrival))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()


