import os

class Config:
    # MongoDB Configuration
    MONGO_URI = os.getenv('MONGO_URI', 'mongodb://mongo:27017/bitcoin_wallets')
    
    # Redis Configuration
    REDIS_URL = os.getenv('REDIS_URL', 'redis://redis:6379/0')
    
    # Encryption Key (برای تولید کلید جدید از Fernet.generate_key() استفاده کنید)
    ENCRYPTION_KEY = os.getenv('ENCRYPTION_KEY', 'your-encryption-key-here')
