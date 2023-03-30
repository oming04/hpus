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
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5858667400:AAFNhrQCUDyCeDqwUDop3pqd8cWXobz6teI")

    # Get from my.telegram.org
    APP_ID = int(os.environ.get("APP_ID", "7350916"))

    # Get from my.telegram.org
    API_HASH = os.environ.get("API_HASH", "776fec9b07afa7d5cc74425852c9835b")

    # Authorized users to use this bot
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "5178642977").split())

    # Generate a user session string
    TG_USER_SESSION = os.environ.get("TG_USER_SESSION", "BQGm8CMAxjWyscG0fyHQDl6CG9hWJPIkilRJaHZKKLhEFwS7XVDi03lrgSdg47LxFkLqYKqUBq67_G3btpg5WkGDjpfY6Yg-7gv5Qbl_9L7NwbrxMR7VUFbpqMaLsxE3CI_r5MHgqZfa1nY1FdY9cvW4frihWap2MaPSeTjZQwDyiuhY8Ap81K3NwshhyXqI0n9PKGlECABFtjWv0_MloDRDmiH8_LNixplUX7qybVq9Ppt_A5a933lbpUJd9vCx6DMOtAqx1RJx0YWFi0HRFhR_Di2WqCQodI92J7a1u842GSBobjdBCOjdG7zkn0M_6OtzrNjzFhgxhIlxrAy800HuwdjBdQAAAAFRfeP5AA")
    

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
