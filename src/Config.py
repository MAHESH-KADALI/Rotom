import os

class Config:
    api_id = int(os.environ.get("API_ID", None))
    api_hash = os.environ.get("API_HASH", None)
    bot_token = os.environ.get("BOT_TOKEN", None)
    try:
        sudo = set(int(x) for x in os.environ.get("SUDO", "").split())
    except ValueError:
        raise Exception("Your sudo users list does not contain valid integers.")
    
