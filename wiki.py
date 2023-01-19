import logging
import wikipedia
from aiogram import Bot, Dispatcher, executor, types
from utils.util import BOT_TOKEN


wikipedia.set_lang('uz')
API_TOKEN = BOT_TOKEN

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler()
async def send_wiki(message: types.Message):
    try:
        respond = wikipedia.summary(message.text)
        await message.answer(respond)
    except:
        await message.answer('Bu mavzu topilmadi')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)