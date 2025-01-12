import unittest
from app.wallet import recover_wallet

class TestWallet(unittest.TestCase):
    def test_recover_wallet_success(self):
        seed_phrase = "seed phrase example 1 2 3 4 5 6 7 8 9 10 11 12"
        result = recover_wallet(seed_phrase)
        self.assertIn('balance', result)
        self.assertIn('transactions', result)

    def test_recover_wallet_invalid_seed(self):
        seed_phrase = "invalid seed phrase"
        result = recover_wallet(seed_phrase)
        self.assertIn('error', result)

if __name__ == '__main__':
    unittest.main()
