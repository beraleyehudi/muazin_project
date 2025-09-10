import os

import pymongo
from pymongo import AsyncMongoClient
from pymongo.server_api import ServerApi


class MongoConnection:
    """
    A class that holds the database connection and client,
    implementing a singleton design pattern with lazy initialization.
    """
    _client = None
    _db = None

    @classmethod
    def get_client(cls):
        """A class method that returns a singleton database client."""
        if cls._client is None:
            cls._client = pymongo.MongoClient(os.environ["MONGODB_URL"])
            cls._db = cls._client[os.environ["MONGODB_DATABASE"]]

    @classmethod
    def get_db(cls):
        """A class method that returns a singleton database collection."""
        if cls._db is None:
            cls.get_client()
        return cls._db


