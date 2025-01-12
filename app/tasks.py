from celery import Celery
from .database import wallets_collection
from .wallet import recover_wallet
from .encryption import decrypt_seed_phrase
from .config import Config

celery_app = Celery('tasks', broker=Config.REDIS_URL, backend=Config.REDIS_URL)

@celery_app.task
def process_seed_phrase(encrypted_seed_phrase):
    try:
        seed_phrase = decrypt_seed_phrase(encrypted_seed_phrase)
        result = recover_wallet(seed_phrase)
        wallets_collection.insert_one(result)
        return result
    except Exception as e:
        return {'error': str(e)}
