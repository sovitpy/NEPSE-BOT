from telegram.ext import Updater, CommandHandler
import requests



def nepse(update, context):
    given = update.message.text
    array_given = given.split(' ')

    r = requests.get('http://api-nepse.herokuapp.com/todays_price')
    api_json = r.json()

    if(len(array_given) > 1):
        response = array_given[1].strip()
        if response.lower() == 'companies':
            keys = api_json.keys()
            i = 1
            string = '<b><u> List of Symbols for checking Nepse </u></b>\n\n'
            for key in keys:
                string = string + str(i) + ' ) <code>' + key + '</code>   '
                i += 1
        else:
            try:
                response = response.upper()
                status = api_json[response]           
                string = f"<u><b>Nepse Stats For {response}</b></u>\n\n"
                string += f"<b>Name: </b>{status['name']}\n"
                string += f"<b>Conf: </b>{status['conf']}\n"
                string += f"<b>Open: </b>{status['open']}\n"
                string += f"<b>High: </b>{status['high']}\n"
                string += f"<b>Close: </b>{status['close']}\n"
                string += f"<b>Turnover: </b>{status['turnover']}\n"
                string += f"<b>Transfer: </b>{status['transfer']}\n"
                string += f"<b>Diff: </b>{status['diff']}\n"
                string += f"<b>Range: </b>{status['range']}\n"
                string += f"<b>Diff Percent: </b>{status['diff_per']}\n"
                string += f"<b>Range Percent: </b>{status['range_per']}\n"
                string += f"<b>Vwap Percent: </b>{status['vwap_per']}\n"
                string += f"<b>120 days: </b>{status['120 days']}\n"
                string += f"<b>180 days: </b>{status['180 days']}\n"
                string += f"<b>52 weeks High: </b>{status['52 weeks high']}\n"
                string += f"<b>52 weeks Low: </b>{status['52 weeks high']}\n"
            except KeyError:
                string = '<b> Please Check the Symbol and Try Again </b>'
    else:
        string = "<b> A NEPSE stats bot </b>\n\n<b>Do <code>/nepse companies</code> to get symbols of Companies Listed in Nepse</b>\n\n<b> Do <code>/nepse <symbol></code> to get the stats for that company<b>\n\nPlugin Credit: </b> @beast076<b>\n\nAPI Credit: </b> @scifidemon</b>"

    update.message.reply_text(string, parse_mode= "HTML")


def start(update, context):
    response = "<b> A Nepse stats bot </b>\n\n<b>Do <code>/nepse companies</code> to get symbols of Companies Listed in Nepse</b>\n\n<b> Do <code>/nepse symbol</code> to get the stats for that company<b>\n\nPlugin Credit: </b> @beast076<b>\n\nAPI Credit: </b> @scifidemon</b>"
    update.message.reply_text(response, parse_mode= "HTML")

updater = Updater('bot_token', use_context=True)


updater.dispatcher.add_handler(CommandHandler('nepse', nepse))
updater.dispatcher.add_handler(CommandHandler('start', start))

updater.start_polling()
updater.idle()
