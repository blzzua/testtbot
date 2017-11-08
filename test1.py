import telegram
import sys
import configparser
import logging

config = configparser.ConfigParser()
logging.debug('read config. begin')
config.read('bot.ini')
token = config.get('main', 'token')
chats=dict()
for (t_chatname,t_chatid) in config.items('chat') :
    chats[t_chatname]=t_chatid

print (config.sections() )

logging.debug('read config. done')

if __name__ == '__main__' :
    if len(sys.argv) > 1:
        target = sys.argv[1]
        message = sys.argv[2]
    else:
        print ('no args: target "text message" ')
        quit()
    if target not in chats:
        print ('target chat not exists in bot.ini')
        quit()

    bot = telegram.Bot(token=token)
    my_chatid=chats[target]
    bot.send_message(chat_id=my_chatid, text=message)
