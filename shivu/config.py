class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "7079236910"
    sudo_users = "7079236910"
    GROUP_ID = -1002206526478
    TOKEN = "7895329270:AAGKuBEYNcklXeaRSgYXOuJ3Wb9jVcY3ka0"
    mongo_url = "mongodb+srv://HaremDBBot:ThisIsPasswordForHaremDB@haremdb.swzjngj.mongodb.net/?retryWrites=true&w=majority"
    PHOTO_URL = ["https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.deviantart.com%2Fnayareen%2Fart%2FMikasa-Ackerman-Tribute-984497035"]
    SUPPORT_CHAT = "waifucatcher00"
    UPDATE_CHAT = "waifucatcher00"
    BOT_USERNAME = "Marvelous_Waifu_Husbando_Bot"
    CHARA_CHANNEL_ID = "-1002420677845"
    api_id = 27152394
    api_hash = "f21ea95912cfd67e97df54c142191f20"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
