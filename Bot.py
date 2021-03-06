import pyowm
import telebot

owm = pyowm.OWM('6d00d1d4e704068d70191bad2673e0cc', language = "ru")
bot = telebot.TeleBot( "1031233548:AAFfUXO0e8bDuOTWaQbHQCCuA_YJwRbqQlY" )

@bot.message_handler(content_types=['text'])
def send_echo(message):
	observation = owm.weather_at_place( message.text )
	w = observation.get_weather()
	temp = w.get_temperature('celsius')["temp"]

	answer =  " В городе " + message.text + " сейчас " + w.get_detailed_status() + "\n"
	answer +=  " Температура сейчас в районе " + str(temp) + "\n\n"

	if temp < 0:
		answer += " Очень холодно "
	elif temp < 10:
		answer += " Одевайся теплее"
	elif temp < 20:
		answer +=" Прохладно "
	else:
		answer += " Можно и в шортиках "

	bot.send_message(message.chat.id, answer)

bot.polling( none_stop = True)