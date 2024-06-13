from aiogram import types,executor,Bot,Dispatcher
from req import send_answer 



API = '7166336313:AAH7fuyx1pNSwdPSibZp0FpAII-Vz4nuhG0'
bot = Bot(token=API)
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=['start'])
async def say_hi(message:types.Message):
    await message.answer('bizge soraw jazin')

@dp.message_handler(text='Send message to admin')
async def to_admin(message:types.Message):
    answer = await send_answer(message.text)
    await message.answer(answer)
    

    


if __name__=='__main__':
    executor.start_polling(dp,skip_updates=True)
