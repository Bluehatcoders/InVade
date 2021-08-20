# EDIT THIS FILE AND RENAME TO config.py TO MAKE THIS BOT WORKING
# FILL THESE VALUES ACCORDINGLY.

from hell_config import Config

class Development(Config):
  # get these values from my.telegram.org. 
  APP_ID = 6512145    # 6 is a placeholder. Fill your 6 digit api id
  API_HASH = "8dfdd3ea0bf4ee3177470dbf355451c1"   # replace this with your api hash

  # the name to display in your alive message.
  # If not filled anything then default value is I'm Hêll.
  YOUR_NAME = "SATYA"

  # create any PostgreSQL database.
  # I recommend to use elephantsql and paste that link here
  DB_URI = "postgres://hqcsmyixqbhghm:b4f25c5c69e576b82d1f68170b6bb3826448fe7b2523a68b4627255fc7f635a5@ec2-54-156-85-145.compute-1.amazonaws.com:5432/d4ldvd9q1j3irl"

  # After cloning the repo and installing requirements...
  # Do `python string.py` and fill the on screen prompts.
  # String session will be saved in your saved message of telegram.
  # Put that string here.
  HELLBOT_SESSION = "1BVtsOIgBuyIpwt4UIGaXjj4hZa0XaJBxE3fylzgbo3SsupapAhQXmiw8KZguOcqwMD8p8hmZ6JZ6ekp4hasy5YCGAMdpLMsuB9rDkhSL5EXhVA6i1XJNd9y-9mvDUak7hZbWemjg_gHPI5Pnb82Rg1XfpV77zVY9r1U_2CLKFot3K6pGDbzBDPn6SVJlJfFZfDJJ28G8G68Mam9e7iTF0fwx6aMiNZCkELqCx1Edn_Rm4g1qFCwKgag322N4XqDEdgXtTdKlrEz6tqtR4r4xwFmTWHxaPpvib4vsyrglYnR9cFxVn0nmpRS_4aEglRtZp2DavOD3s1qocjAlaVPnxSLBmKRQbAE="

  # Create a bot in @BotFather
  # And fill the following values with bot token and username.
  BOT_TOKEN = "1989037296:AAFt_PGNz0kjsQ1OPsLklDiUykRh1-iSats" #token
  BOT_USERNAME = "catuserbottestsatyabot" #username

  # Create a private group and add rose bot to it.
  # and type /id and paste that id here.
  # replace that -100 with that group id.
  LOGGER_ID = -1001571245178

  # Custom Command Handler. 
  HANDLER = "."

  # enter the userid of sudo users.
  # you can add multiple ids by separating them by space.
  # fill values in [] only.
  SUDO_USERS = []

  # Custom Command Handler for sudo users.
  SUDO_HANDLER = "!"

# end of required config
# hellbot
