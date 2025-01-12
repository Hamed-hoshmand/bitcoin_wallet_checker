from pymongo import MongoClient
from .config import Config

client = MongoClient(Config.MONGO_URI)
db = client['bitcoin_wallets']
seed_phrases_collection = db['seed_phrases']
wallets_collection = db['wallets']
