# (c) @AbirHasan2005

import os
import logging

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'),
              logging.StreamHandler()],
    level=logging.INFO
)


class Config(object):
    API_ID = int(os.environ.get("API_ID", "10811400"))
    API_HASH = os.environ.get("API_HASH", "191bf5ae7a6c39771e7b13cf4ffd1279")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6487202001:AAEbvm06XeRJcwR0qZnStmsRKF9CQ0z_kvU")
    DOWNLOAD_DIR = os.environ.get("DOWNLOAD_DIR", "./downloads")
    LOGGER = logging
    OWNER_ID = int(os.environ.get("OWNER_ID", 6469754522))
    PRO_USERS = list(set(int(x) for x in os.environ.get("PRO_USERS", "0").split()))
    PRO_USERS.append(OWNER_ID)
    MONGODB_URI = os.environ.get("MONGODB_URI", "mongodb+srv://CONVERTER24BOT:CONVERTER24BOT@cluster0.2kl0qhx.mongodb.net/?retryWrites=true&w=majority")
    FORCE_SUB = os.environ.get("FORCE_SUB", "Sunrises24BotUpdates")
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002112896731"))
    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", "False"))
