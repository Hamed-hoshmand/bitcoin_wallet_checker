from bitcoinlib.wallets import Wallet
from bitcoinlib.services.services import ServiceError

def recover_wallet(seed_phrase):
    try:
        wallet = Wallet.create('RecoveredWallet', keys=seed_phrase, network='bitcoin')
        balance = wallet.balance()
        transactions = wallet.transactions()
        return {
            'seed_phrase': seed_phrase,
            'balance': balance,
            'transactions': transactions
        }
    except ServiceError as e:
        return {
            'seed_phrase': seed_phrase,
            'error': str(e)
        }
    except Exception as e:
        return {
            'seed_phrase': seed_phrase,
            'error': str(e)
        }
