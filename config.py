#----------------------------------- https://github.com/m4mallu/clonebot --------------------------------------------#
import os
import logging


logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S'
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


class Config(object):

    # Get a bot token from botfather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6044156147:AAHyPcegp892CnRbr3xmVM9qNZON8drKgCU")

    # Get from my.telegram.org
    APP_ID = int(os.environ.get("APP_ID", "7350916"))

    # Get from my.telegram.org
    API_HASH = os.environ.get("API_HASH", "776fec9b07afa7d5cc74425852c9835b")

    # Authorized users to use this bot
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "5178642977").split())

    # Generate a user session string
    TG_USER_SESSION = os.environ.get("TG_USER_SESSION", "BQAkl4IC4LcDLorQ_FDLSkxx4fE4FCUZ-2woH4Gmy0ezbQHSJqUbgiV-_0vmpNo54ffXCifCpOzTcG9o4mJqqTkbzx_5SgtWdXvOMFYJ-8wMSg_eWVlyjgxwQUiLHP_Dt6OuebK_OlX0sFIniWsank59XDsWWIH1MpTsmc9TX7BUKlBhKQR1TfXki8ONqJHtYzK9UDXZfMmZlnHVPa27bjUhDuC_N7T7Hog3TFkj7j7cfQcpx5kMV6YM85hX4XsMFt1gPrVlf6tQtcbMuWCHu9jKHd6rW3ey_PxxarkvEcGeEtsEwxnJgw9j0F3BFrZzyulgMKr1-gZ8rE0hEKzd3fAAAAAT5_f78A")
    

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
