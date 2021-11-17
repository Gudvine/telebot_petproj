import telebot
import config
import requests
import pytest

bot = telebot.TeleBot(config.TOKEN) #1 - инициализация бота

#2 - вывод приветсвенного сообщения
@bot.message_handler(commands=['start'])
def send_welcome_message(message):
    bot.send_message(message.chat.id, "🙌 Привет, " + str(message.from_user.username) + " Я - бот для показа погоды. \n \
Пожалуйста, введите город.")


@bot.message_handler(content_types=['text'])
def send_weather(message):
    s_city = message.text #3 - прием на вход названия города
    #4 - запуск работы с отловом исключения
    try: 
        api_parameters = {'APPID': config.API_KEY, 'q': s_city, 'units': 'metric'} #5 - инициализация праметров api
        get_weather = requests.get(config.API_LINK, params=api_parameters) #6 - получение данных с api
        weather_request = get_weather.json() #7 - запись и преобразование полученных данных

        #8 - вывод информации о погодных условиях в данном городе
        bot.send_message(message.chat.id,"В городе " + str(weather_request['name']) + ": " + " \n Температура: " + str(float(weather_request["main"]["temp"])) + " градусов" +
        "\n Максимальная температура: " + str(float(weather_request['main']['temp_max'])) + " градусов" +
        "\n Минимальная температура: " + str(float(weather_request['main']['temp_min'])) 
        + " градусов" +
        "\n Влажность: " + str(float(weather_request['main']['humidity']))
        + 
        "\n Давление: " + str(float(weather_request['main']['pressure'])) + " мм. рт. ст." ) 
        #9 - проверка на погодные условия
        if weather_request["main"]["temp"] < 13:
           bot.send_message(message.chat.id, "Сейчас холодно, оденься теплее!") #10 - вывод совета по холодной погоде
        elif weather_request["main"]["temp"] > 13:
           bot.send_message(message.chat.id, "Сейчас хорошая погода! Можно одеться свободнее!") #11 - вывод совета по теплой погоде
    except:
        bot.send_message(message.chat.id, " 😰 Город не найден") #12 - вывод информации, что город не найден

bot.polling(none_stop=True)
