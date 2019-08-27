import telepot
from Chatbot import Chatbot
telegram = telepot.Bot("902305201:AAEwGowL7Jh25dcupOd3WUH1eUf2JIUrHQ0")
bot = Chatbot("Muisc_Master")
def receivingMsg (msg):
    frase = bot.escuta(frase = msg['text'])
    resp = bot.pensa(frase)
    bot.fala(resp)
    tipoMsg, tipoChat, chatID = telepot.glance(msg)
    telegram.sendMessage(chatID,resp)
telegram.message_loop(receivingMsg)
while True:
    pass