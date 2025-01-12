import unittest
from unittest.mock import patch
from app.tasks import process_seed_phrase

class TestTasks(unittest.TestCase):
    @patch('app.tasks.recover_wallet')
    @patch('app.tasks.decrypt_seed_phrase')
    @patch('app.tasks.wallets_collection.insert_one')
    def test_process_seed_phrase_success(self, mock_insert, mock_decrypt, mock_recover):
        encrypted_phrase = "encrypted_seed_phrase"
        seed_phrase = "seed phrase example 1 2 3 4 5 6 7 8 9 10 11 12"
        mock_decrypt.return_value = seed_phrase
        mock_recover.return_value = {
            'seed_phrase': seed_phrase,
            'balance': 100,
            'transactions': []
        }

        result = process_seed_phrase(encrypted_phrase)

        mock_decrypt.assert_called_once_with(encrypted_phrase)
        mock_recover.assert_called_once_with(seed_phrase)
        mock_insert.assert_called_once_with(mock_recover.return_value)
        self.assertEqual(result['balance'], 100)

    @patch('app.tasks.recover_wallet')
    @patch('app.tasks.decrypt_seed_phrase')
    @patch('app.tasks.wallets_collection.insert_one')
    def test_process_seed_phrase_error(self, mock_insert, mock_decrypt, mock_recover):
        encrypted_phrase = "encrypted_seed_phrase"
        seed_phrase = "invalid seed phrase"
        mock_decrypt.return_value = seed_phrase
        mock_recover.return_value = {
            'seed_phrase': seed_phrase,
            'error': 'Invalid seed phrase'
        }

        result = process_seed_phrase(encrypted_phrase)

        mock_decrypt.assert_called_once_with(encrypted_phrase)
        mock_recover.assert_called_once_with(seed_phrase)
        mock_insert.assert_called_once_with(mock_recover.return_value)
        self.assertIn('error', result)

if __name__ == '__main__':
    unittest.main()
