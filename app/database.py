from pymongo import MongoClient
from odmantic import SyncEngine
from app.config import settings

client = MongoClient(settings.MONGODB_URL)
engine = SyncEngine(client=client, database=settings.MONGODB_DATABASE)
