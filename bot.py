from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from pycbrf import ExchangeRates
from emoji import emojize
from config import TOKEN, weathertoken
import requests

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await bot.send_message(message.from_user.id, "👋Привет, напиши мне название любого города, например: New York. Если есть вопросы, напиши команду /help")

@dp.message_handler(commands=['help'])
async def process_start_command(message: types.Message):
    await bot.send_message(message.from_user.id, "👋Просто введи в чат название города где вы желаете узнать погоду, писать можно на разных языках\n*Москва, Moscow*")

@dp.message_handler()
async def get_todays_weather(message: types.Message):
    try:
        r = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={weathertoken}&units=metric")
        data = r.json()

        city = data["name"]
        cur_weather = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        feels_like = data["main"]["feels_like"]
        wind = data["wind"]["speed"]
        country = data["sys"]["country"]
        if cur_weather >= 20.0:
            await message.reply("🔅отличная погода что бы погулять")
        if cur_weather <= 8.0:
            await message.reply("Холодно однако")
        if wind >= 5:
        	await message.reply("Сегодня ветрено")

        await message.reply(f"🌠Погода в городе: {city}\nСтрана: {country}\n🌡Температура {cur_weather} градусов\n🔅Ощущаеться как {feels_like} градусов\nДавление {pressure} гПа \n🌪скорость ветра {wind} км в час\n💦Влажность {humidity}%")
    except:
        await message.reply("Вы ввели не правильно название города, попробуйте ещё раз")
    
if __name__ == '__main__':
    executor.start_polling(dp)