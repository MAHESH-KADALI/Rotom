import os

class Config:
    aid = int(os.environ.get("API_ID", "2888382"))
    ahash = os.environ.get("API_HASH", "908a8a13c87a6c1899f6e788a05d3d0d")
    bot_token = os.environ.get("BOT_TOKEN", "1411304557:AAGIPGA03pzy7vUgDPJnwXkB3g3vJqvV8RY")
    sudo = [1377620841, 1152178636]
    # try:
    #     sudo = set(int(x) for x in os.environ.get("SUDO", "").split(','))
    # except ValueError:
    #     raise Exception("Your sudo users list does not contain valid integers.")
    
