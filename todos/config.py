from os import environ
from datetime import timedelta


class Config:
    # General Config
    SECRET_KEY = environ.get('SECRET_KEY')
    FLASK_APP = environ.get('FLASK_APP')
    JSON_SORT_KEYS = False

    # DBs
    # # Mongo
    MONGODB_SETTINGS = {
        'host': environ.get("MONGO_HOST"),
        'db': environ.get("MONGO_NAME") or 'defaultdbpi',
        'username': environ.get("MONGO_USER"),
        'password': environ.get("MONGO_PASS"),
        'authentication_source': environ.get("MONGO_AUTH_SOURCE") or 'admin'
    }

    REDIS_HOST = environ.get("REDIS_HOST")
    REDIS_URL = "redis://{}/".format(REDIS_HOST)

    # GOOGLE SECRETS
    GOOGLE_CLIENT_ID = environ.get("GOOGLE_CLIENT_ID", None)
    GOOGLE_CLIENT_SECRET = environ.get("GOOGLE_CLIENT_SECRET", None)
    GOOGLE_DISCOVERY_URL = (
        "https://accounts.google.com/.well-known/openid-configuration"
    )

    # TODO set me False to unlimited expire time (development only)
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)
