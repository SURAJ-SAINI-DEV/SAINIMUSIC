from SAINIMUSIC.core.bot import SAINI
from SAINIMUSIC.core.dir import dirr
from SAINIMUSIC.core.git import git
from SAINIMUSIC.core.userbot import Userbot
from SAINIMUSIC.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = SAINI()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
