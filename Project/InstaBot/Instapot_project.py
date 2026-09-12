from instabot import Bot
bot=Bot()
bot.login(username="tatonmoy112",password="JoKeR@2274")
# bot.follow("")
# bot.upload_photo("C:/Users/Basit/Desktop/Course/FIGMA/Console.png",caption="")
# bot.send_message("",username="")
# bot.send_message("",["",""])
# print(k=bot.get_user_info("_farjuuu"))
infos=bot.get_user_followers("tatonmoy112")
for info in infos:
    print(bot.get_user_info(info))