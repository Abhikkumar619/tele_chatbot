
import logging
from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
import os


load_dotenv() # It automatically find .env file to load TOKEN.
# os.getenv("TOKEN")
API_TOKEN=os.getenv("TOKEN") 
# print(API_TOKEN)

# Configure logging.
logging.basicConfig(level=logging.INFO)

# Initializer bot and dispatcher.
bot=Bot(token=API_TOKEN)
dp=Dispatcher(bot)       # both and bot and dispatcher helps us to make conncection with telegram bot.



@dp.message_handler(commands=['start','help'])
async def command_start_handler(message: types.Message):

    """ 
    This handler receives messages with '/start' or '/help' commnad
    """
    
    await message.answer("Hi\n I am Echo Bot! \n Powered by aiogram.\n How can i help You.")

@dp.message_handler()
async def echo(message: types.Message):

    """
    This will return echo
    """
    await message.answer(message.text)




if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

