# (c) @AbirHasan2005

import os

class Config(object):
	API_ID = int(os.environ.get("API_ID"))
	API_HASH = os.environ.get("API_HASH")
	BOT_TOKEN = os.environ.get("BOT_TOKEN")
	BOT_USERNAME = os.environ.get("BOT_USERNAME")
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL"))
	BOT_OWNER = int(os.environ.get("BOT_OWNER"))
	DATABASE_URL = os.environ.get("DATABASE_URL")
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)
	LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL"))
	ABOUT_BOT_TEXT = f"""
This is 𝗘𝘃𝗲𝗹𝘆𝗻 𝗙𝗶𝗹𝗲 𝗦𝗵𝗮𝗿𝗲 & 𝗦𝘁𝗼𝗿𝗮𝗴𝗲  𝗥𝗼𝗯𝗼𝘁!
Send me any file I will save it in my Database Permanently. Also works for channel. Add me to channel as Admin with Edit Permission, I will add Save Uploaded File in Channel & add Sharable Button Link.

🤖 **My Name:** [Files Store Bot](https://t.me/{BOT_USERNAME})

📝 **Language:** [Python3](https://www.python.org)

📡 **Hosted on:** [Heroku](https://heroku.com)

🧑🏻‍💻 **Developer:** @Sonia_Mohapatra

👥 **Support Group:** [🏅 Movie Buzz ®](https://t.me/MovieBuzzOfficial)

📢 **Updates Channel:** [Movie Buzz Group🏩](https://t.me/Discovery_Updates)
"""
	ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 **Developer:** @Sonia_Mohapatra

Hello. I Will Not Brag About Something Which I Didnt Do. This Bot Was Officially Made By Abir Hasan.
And A Big Thank You To Him For Making This Bot. You Can Donate To Him By Clicking On The Link Given Below.
And Again A Big Thank You To The Bot Makers. Cheers! ! Please Donate the developer for Keeping the Service Alive.

Also remember that developer will Delete Adult Contents from Database. So better don't Store Those Kind of Things.

[Donate Now](https://www.paypal.me/AbirHasan2005) (PayPal)
"""
	HOME_TEXT = """
Hi, [{}](tg://user?id={})\n\nThis is Permanent **File Store Bot**.

𝗛𝗲𝘆 𝗗𝗲𝗮𝗿 𝗜 𝗮𝗺 𝗘𝘃𝗲𝗹𝘆𝗻 𝗙𝗶𝗹𝗲 𝗦𝗵𝗮𝗿𝗲 & 𝗦𝘁𝗼𝗿𝗮𝗴𝗲  𝗥𝗼𝗯𝗼𝘁 😁

📌𝗛𝗢𝗪 𝗧𝗢 𝗨𝗦𝗘 & 𝗪𝗛𝗔𝗧 𝗕𝗘𝗡𝗜𝗙𝗜𝗧??

📫Send Me any File i can upload
Your File in my Top secret Database 🤗 I will give you a permanent Sharable Link. I Support Channel Also!

⭕Benifit:  If You Have Telegram Movie Channel! Then Useful for you.You can Send me your File and I'll send you link of your file, So people will get File From me 😊 and Your Channel will safe NO COPYRIGHT issue🤩.
😎 Availability : Only people with the link can access the file. No one in the universe can access your file without your permission.
🔵𝗗𝗼𝗻'𝘁 𝗨𝘀𝗲 𝗣𝗼𝗿𝗻𝗼𝗴𝗿𝗮𝗽𝗵𝘆 𝗙𝗶𝗹𝗲
𝗢𝘁𝗵𝗲𝗿𝘄𝗶𝘀𝗲 𝘆𝗼𝘂 𝘄𝗶𝗹𝗹 𝗯𝗲 𝗯𝗮𝗻 Check **About Bot** Button.
"""
