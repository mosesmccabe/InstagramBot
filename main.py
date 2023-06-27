from dotenv import load_dotenv
import os
from InstaFollower import InstaFollower

load_dotenv()

SIMILAR_ACCOUNT = "shittywinememes"
USER_NAME = os.getenv("IG_USER_NAME")
PASSWORD = os.getenv("IG_PASSWORD")

inst_bot = InstaFollower()
inst_bot.login(USER_NAME, PASSWORD)
inst_bot.find_followers()
# inst_bot.follow()
