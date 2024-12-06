# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "18077885"))
API_HASH = getenv("API_HASH", "96be0d8c8504f46cc20ea8dcbbca9c19")
BOT_TOKEN = getenv("BOT_TOKEN", "7694158072:AAEVSupdLFbBWQta0ILa_hRXBjr_cFmipow")
OWNER_ID = list(map(int, getenv("OWNER_ID", "6474452917").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://aknteam:ma622304@cluster0.gdok4pq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002278193937"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "0"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "500"))
