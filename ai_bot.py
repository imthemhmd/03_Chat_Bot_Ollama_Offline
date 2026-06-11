# Welcome To Project Chat Bot Offline Ollama
# In this file, we will create a simple Telegram 
# chatbot where we can talk to ollama herself in the chatbot.



import telebot
import token_bot
import ollama_api

bot = telebot.TeleBot(token_bot.TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    text_start = "سلام\nبه بات arlo خوش اومدید."
    bot.send_message(message.chat.id, text=text_start)


@bot.message_handler(commands=['menu'])
def show_menu(message):
    markup = telebot.types.InlineKeyboardMarkup(row_width=3)
    btn_1 = telebot.types.InlineKeyboardButton(text="Chat By AI", 
                                               callback_data="chat_by_ai")

    markup.add(btn_1)
    bot.reply_to(message, text="Choice Your Option", reply_markup=markup)

@bot.message_handler(commands=['exit'])
def exit_chat(message):
    show_menu(message)

@bot.callback_query_handler(func=lambda call:call.data == "chat_by_ai")
def process_menu(call):
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    btn_5 = telebot.types.InlineKeyboardButton(text="Chat By Ai Ollama Offline", callback_data="chat_by_ollama_offline")
    btn_6 = telebot.types.InlineKeyboardButton(text="Chat By Chat GPT", url="https://chatgpt.com/")
    btn_7 = telebot.types.InlineKeyboardButton(text="Chat By Grok", url="https://grok.com/")
    btn_8 = telebot.types.InlineKeyboardButton(text="Chat By DeepSeek", url="https://chat.deepseek.com/")
    markup.add(btn_5, btn_6, btn_7, btn_8)
    bot.send_message(call.message.chat.id, text="Choice Your Ai", reply_markup=markup)


@bot.callback_query_handler(func=lambda call:call.data == "chat_by_ollama_offline")
def question_answer(call):
    question = bot.send_message(call.message.chat.id, text="Enter Question:")
    bot.register_next_step_handler(question, answer_ai)

def answer_ai(message):
    if message.text == "/menu" or message.text == "/exit":
        show_menu(message)
        return
    result = ollama_api.call_ollama(message.text)
    msg = bot.reply_to(message, result)
    bot.register_next_step_handler(msg, answer_ai)


if __name__ == "__main__":
    bot.infinity_polling()