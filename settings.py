import os

# The prefix that will be used to parse commands.
# It doesn't have to be a single character!
COMMAND_PREFIX = "~"

# The bot token. Keep this secret!
BOT_TOKEN = "ODE1MzM2MDkwOTI4MDIxNTE0.YDq66A.HUDTWVPfceMvROWkQZHUtbk5XTU"

# The now playing game. Set this to anything false-y ("", None) to disable it
NOW_PLAYING = COMMAND_PREFIX + "meow"

# Base directory. Feel free to use it if you want.
BASE_DIR = os.path.dirname(os.path.realpath(__file__))
