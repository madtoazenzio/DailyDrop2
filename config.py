#(©)CodeXBotz




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7599287095:AAGpwSxCAWasoJYMCktPFV3yxl41EyBPvmo")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "7236453"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "33010a70e94f80e55145980072cce969"")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002436226291"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "6891428437"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = "mongodb+srv://madtoazenzio:f9oDLc4c6H5zdP44@devutty.pk5so.mongodb.net/?retryWrites=true&w=majority&appName=devutty"
DB_NAME = os.environ.get("DATABASE_NAME", "filesharexbot")

SHORTLINK_URL = os.environ.get("SHORTLINK_URL", "droplink.co")
SHORTLINK_API = os.environ.get("SHORTLINK_API", "ba9397cf73004a7d5236f014af404ed712ca1544")
VERIFY_EXPIRE = int(os.environ.get('VERIFY_EXPIRE', 86400)) # Add time in seconds
IS_VERIFY = os.environ.get("IS_VERIFY", "True")
TUT_VID = os.environ.get("TUT_VID","https://t.me/howtoopen88/5")


#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002231278815"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "𝖧𝖾𝗅𝗅𝗈 {first}\n\n𝖨𝖺𝗆 𝖠 𝖡𝗈𝗍 𝖳𝗁𝖺𝗍 𝖬𝖺𝖽𝖾 𝖡𝗒 𝖬𝗒 𝖠𝖽𝗆𝗂𝗇 ☺︎︎.")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6891428437").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>You need to join in my Channel/Group to use me\n\nKindly Please join Channel</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "This video/Photo/anything is available on the internet. We doesn't Leaked or its subsidiary channel doesn't produce any of them.")

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't send me messages directly I'm only File Share bot!"

ADMINS.append(OWNER_ID)
ADMINS.append(6852649461)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
