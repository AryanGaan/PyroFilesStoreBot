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
This is 𝗘𝘃𝗲𝗹𝘆𝗻 𝗦𝘁𝗼𝗿𝗮𝗴𝗲 𝗦𝗲𝗰𝘁𝗼𝗿!

🤖 **My Name:** [Files Store Bot](https://t.me/{BOT_USERNAME})

👩‍💻 **Developer:** @Sonia_Mohapatra

🏩 **Support Group:** [Movie Buzz Group](https://t.me/MovieBuzzOfficialGroup)

📢 **Updates Channel:** [Movie Buzz®](https://t.me/MovieBuzzOfficial)
"""
	ABOUT_DEV_TEXT = f"""
👩‍💻 **Developer:** @Sonia_Mohapatra

Hello. I Will Not Brag About Something Which I Didnt Do. This Bot Was Officially Made By Abir Hasan. A Big Thank You To Him For Making This Bot. You Can Donate To Him By Clicking On The Link Given Below. Cheers! ! Please Donate the developer for Keeping the Service Alive.

Also remember that developer will 𝗣𝗢𝗥𝗡𝗢𝗚𝗥𝗔𝗣𝗛𝗜𝗖 𝗖𝗢𝗡𝗧𝗘𝗡𝗧𝗦 from Database. So better don't Store Those Kind of Things.

[Donate Now](https://www.paypal.me/AbirHasan2005) (PayPal)
"""
	HOME_TEXT = """
𝗛𝗲𝘆 𝗗𝗲𝗮𝗿, [{}](tg://user?id={})\n\n 𝗜 𝗮𝗺 𝗘𝘃𝗲𝗹𝘆𝗻 𝗣𝗲𝗿𝗺𝗮𝗻𝗲𝗻𝘁 𝗙𝗶𝗹𝗲 𝗦𝗵𝗮𝗿𝗲 & 𝗦𝘁𝗼𝗿𝗮𝗴𝗲  𝗥𝗼𝗯𝗼𝘁 😇.

📌 𝗛𝗢𝗪 𝗧𝗢 𝗨𝗦𝗘 & 𝗪𝗛𝗔𝗧 𝗕𝗘𝗡𝗜𝗙𝗜𝗧??

📫 Send Me any File i can upload
Your File in my Top secret Database 🤗 I will give you a permanent Sharable Link. I Support Channel Also! Add me to channel as Admin with Edit Permission, I will add Save Uploaded File in Channel & add Sharable Button Link.

⚠️ Benifit:  If You want to store something and worried about Copyright! Then Useful for you.You can Send me your File and I'll send you link of your file, So people will get File From me 😊 and Your Channel will safe NO COPYRIGHT issue🤩.
📍No one in the universe can access your file without your permission, if you share them your link only then they are able to get the file.
 
❌ 𝗣𝗢𝗥𝗡𝗢𝗚𝗥𝗔𝗣𝗛𝗜𝗖 𝗖𝗢𝗡𝗧𝗘𝗡𝗧𝗦 Are Strictly Prohibited & Will Get You Banned Permanently.Check **About Bot** Button.
"""
