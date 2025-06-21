# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
import json
import os


def get_user_list(config, key):
    with open("{}/ShuKurenaiXRoBot/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]


# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = 23212132  # integer value, dont use ""
    API_HASH = "1c17efa86bdef8f806ed70e81b473c20"
    TOKEN = "7847667702:AAHgL2ILmtZ6Dh51kNP6zUOknqglRpapnQ0"  # This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = 7819315360  # If you dont know, run the bot and do /id in your private chat with it, also an integer
    OWNER_USERNAME = "FOS_FOUNDER"
    SUPPORT_CHAT = "FOS_BOTS"  # Your own group for support, do not add the @
    JOIN_LOGGER = (
        -1002620872464
    )  # Prints any new group the bot is added to, prints just the name and ID.
    EVENT_LOGS = (
        -1002620872464
    )  # Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = "mongodb+srv://TEAMBABY01:UTTAMRATHORE09@cluster0.vmjl9.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"  # needed for any database modules
    LOAD = []
    NO_LOAD = ["rss", "cleaner", "connection", "math"]
    WEBHOOK = False
    INFOPIC = True
    URL = None
    SPAMWATCH_API = "CC4u_6y7bNxxdyzSDT1zwkr0MG1oUpqdItHOVU~ZPSqTp7ZCOEa8HRVQgHY6s8w1"  # go to support.spamwat.ch to get key
    SPAMWATCH_SUPPORT_CHAT = "@FOS_BOTS"
    SESSION_STRING = None
    STRING_SESSION = None

    # OPTIONAL
    ##List of id's -  (not usernames) for users which have sudo access to the bot.
    DRAGONS = get_user_list("elevated_users.json", "sudos")
    ##List of id's - (not usernames) for developers who will have the same perms as the owner
    DEV_USERS = get_user_list("elevated_users.json", "devs")
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    DEMONS = get_user_list("elevated_users.json", "supports")
    # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    TIGERS = get_user_list("elevated_users.json", "tigers")
    WOLVES = get_user_list("elevated_users.json", "whitelists")
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True  # Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    STRICT_GBAN = True
    WORKERS = (
        8  # Number of subthreads to use. Set as number of threads your processor uses
    )
    BAN_STICKER = ""  # banhammer marie sticker id, the bot will send this sticker before banning or kicking a user in chat.
    ALLOW_EXCL = True  # Allow ! commands as well as / (Leave this to true so that blacklist can work)
    CASH_API_KEY = (
        "RLDK43KBRE6B9TTF"  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
    TIME_API_KEY = "JOBAXYAULTKF"  # Get your API key from https://timezonedb.com/api
    WALL_API = (
        ""  # For wallpapers, get one from https://wall.alphacoders.com/api.php
    )
    AI_API_KEY = ""  # For chatbot, get one from https://coffeehouse.intellivoid.net/dashboard
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
