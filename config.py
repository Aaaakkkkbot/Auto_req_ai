from os import environ

API_ID = int(environ.get("API_ID", "21418386"))
API_HASH = environ.get("API_HASH", "aeac46b1d123e82fe6dcb43b6a26cfae")
BOT_TOKEN = environ.get("BOT_TOKEN", "7746109405:AAGY78jPwG0OUpf3YHWtEcPIpgSYTxwjR3Y")

AUTH_CHANNEL = int(environ.get("AUTH_CHANNEL", "-1002023325254"))
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002129492449"))
ADMINS = int(environ.get("ADMINS", "5496176944"))

# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = environ.get("DB_URI", "mongodb+srv://TaktAsahina99:TaktAsahina99@cluster0.iq3cx2j.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = environ.get("DB_NAME", "Aerobots")

# If this is True Then Bot Accept New Join Request 
NEW_REQ_MODE = bool(environ.get('NEW_REQ_MODE', True))
