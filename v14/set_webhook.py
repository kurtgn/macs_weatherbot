from bot import bot


server_url = 'https://r21xa74fya.execute-api.us-east-1.amazonaws.com/dev/'
# server_url = 'https://kurtgn.serveo.net/'
print(bot.setWebhook(server_url + 'telegram_notification/'))
# print(bot.setWebhook(None))
