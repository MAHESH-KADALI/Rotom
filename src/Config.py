import os

class Config:
    aid = int(os.environ.get("API_ID", "4857766"))
    ahash = os.environ.get("API_HASH", "6c3c6facf5598a4b318e138f8c407028")
    bot_token = os.environ.get("BOT_TOKEN", "6376375994:AAHf1MoPBq1RF5iCQ1dTRg1cp9jAkzkjkJQ")
    sudo = [1596559467]
    # try:
    #     sudo = set(int(x) for x in os.environ.get("SUDO", "").split(','))
    # except ValueError:
    #     raise Exception("Your sudo users list does not contain valid integers.")
    
