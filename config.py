import logging
from logging.handlers import RotatingFileHandler

# Bot Configuration
LOG_FILE_NAME = "bot.log"
PORT = '5010'
OWNER_ID = 7654385403

MSG_EFFECT = 5046509860389126442

SHORT_URL = "shortxlinks.com/" # shortner url 
SHORT_API = "" 
SHORT_TUT = "https://t.me/+wekKcN1tjbAxY2U1"

# Bot Configuration
SESSION = "Kaya"
TOKEN = "7040063183:AAEaU_h8h19YfH5Zcp-qZFOh4A0CXs5x3gI"
API_ID = "29245477"
API_HASH = "0abc83883262245c90ca337b7a0375c4"
WORKERS = 5

DB_URI = "mongodb+srv://Kurumi:103oq6MdbXWdyI4A@cluster0.yfn0lmh.mongodb.net/"
DB_NAME = "cluster0"

FSUBS = [[-1001457313028, True, 10]] # Force Subscription Channels [channel_id, request_enabled, timer_in_minutes]
# Database Channel (Primary)
DB_CHANNEL = -1002011117693 # just put channel id dont add ""
# Multiple Database Channels (can be set via bot settings)
# DB_CHANNELS = {
#     "-1002595092736": {"name": "Primary DB", "is_primary": True, "is_active": True},
#     "-1001234567890": {"name": "Secondary DB", "is_primary": False, "is_active": True}
# }
# Auto Delete Timer (seconds)
AUTO_DEL = 300
# Admin IDs
ADMINS = [7654385403]
# Bot Settings
DISABLE_BTN = True
PROTECT = False

# Messages Configuration
MESSAGES = {
    "START": "<b><blockquote>Hᴇʏ! {mention} Wᴇʟᴄᴏᴍᴇ Tᴏ Cᴏᴍᴍᴜɴɪᴛʏ Iғ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ sᴜᴘᴘᴏʀᴛ ᴏᴜʀ ᴄᴏᴍᴍᴜɴɪᴛʏ ʏᴏᴜ ᴄᴀɴ ᴅᴏ sᴏ ʙʏ sᴜʙsᴄʀɪʙɪɴɢ ᴛᴏ ᴏᴜʀ ᴄʜᴀɴɴᴇʟ</blockquote></a>\n<blockquote expandable></a>Gᴜɪᴅᴇ Tᴏ Wᴀᴛᴄʜ Vɪᴅᴇᴏ Wɪᴛʜ Sᴜʙᴛɪᴛʟᴇs Iғ Sᴜʙᴛɪᴛʟᴇs Nᴏᴛ Sʜᴏᴡɪɴɢ\n</a>❏ ᴛᴜᴛᴏʀɪᴀʟ\n</a>├ <a href=https://telegra.ph/HOW-TO-WATCH-04-20-3>Cʟɪᴄᴋ Hᴇʀᴇ </a>\nTʜᴀɴᴋs Fᴏʀ ʏᴏᴜʀ Sᴜᴘᴘᴏʀᴛ</blockquote expandable></b>",
    "FSUB": "<b><blockquote>Hᴇʟʟᴏ!! {first} ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ <a href=https://t.me/Anime_Eternals>Aɴɪᴍᴇ Eᴛᴇʀɴᴀʟs</blockquote> </a> Yᴏᴜ ɴᴇᴇᴅ ᴛᴏ Jᴏɪɴ ɪɴ ᴍʏ Cʜᴀɴɴᴇʟ/Gʀᴏᴜᴘ ғɪʀsᴛ, Pʟᴇᴀsᴇ sᴜʙsᴄʀɪʙᴇ ᴛᴏ ᴏᴜʀ ᴄʜᴀɴɴᴇʟs ᴛʜʀᴏᴜɢʜ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ʙᴇʟᴏᴡ ᴀɴᴅ sᴛᴀʀᴛ ʙᴏᴛ ᴀɢᴀɪɴ</a></b>",
    "ABOUT": "<b><blockquote>◈sᴜᴘʀᴇᴀᴍ : <a href='https://t.me/AnimeNexusNetwork'>ɴᴇᴛᴡᴏʀᴋ</a>\n◈ᴀɴɪᴍᴇ : <a href='https://t.me/Anime_Eternals'>ᴀɴɪᴍᴇ ᴇᴛᴇʀɴᴀʟꜱ</a>\n◈ᴏɴɢᴏɪɴɢ ᴀɴɪᴍᴇ: <a href='https://t.me/Anime_Ongoing_Airing'>ᴏɴɢᴏɪɴɢ ᴀɪʀɪɴɢꜱ</a>\n◈ᴇᴄᴄʜɪ : <a href='https://t.me/Ecchi_Dex'>ᴇᴄᴄʜɪ ᴅᴇx</a>\n◈ʜᴇʟᴘʟɪɴᴇ : <a href='https://t.me/EternalsHelplineBot'>ʜᴇʟᴘʟɪɴᴇ</a></b></blockquote>",
    "REPLY": "<b>For More Join - @Anime_Eternals</b>",
    "SHORT_MSG": "<b>📊 ʜᴇʏ {first}, \n\n‼️ ɢᴇᴛ ᴀʟʟ ꜰɪʟᴇꜱ ɪɴ ᴀ ꜱɪɴɢʟᴇ ʟɪɴᴋ ‼️\n\n ⌯ ʏᴏᴜʀ ʟɪɴᴋ ɪꜱ ʀᴇᴀᴅʏ, ᴋɪɴᴅʟʏ ᴄʟɪᴄᴋ ᴏɴ ᴏᴘᴇɴ ʟɪɴᴋ ʙᴜᴛᴛᴏɴ..</b>",
    "START_PHOTO": "https://litter.catbox.moe/fz8604.jpg",
    "FSUB_PHOTO": "https://i.ibb.co/1GwHmz8S/tmpi2nff05y.jpg",
    "SHORT_PIC": "https://i.ibb.co/1GwHmz8S/tmpi2nff05y.jpg",
    "SHORT": "https://telegra.ph/file/8aaf4df8c138c6685dcee-05d3b183d4978ec347.jpg"
}

def LOGGER(name: str, client_name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    formatter = logging.Formatter(
        f"[%(asctime)s - %(levelname)s] - {client_name} - %(name)s - %(message)s",
        datefmt='%d-%b-%y %H:%M:%S'
    )
    file_handler = RotatingFileHandler(LOG_FILE_NAME, maxBytes=50_000_000, backupCount=10)
    file_handler.setFormatter(formatter)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.setLevel(logging.INFO)
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    return logger
