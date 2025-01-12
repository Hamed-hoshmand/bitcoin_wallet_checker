from flask import Flask, request, jsonify
from .database import seed_phrases_collection, wallets_collection
from .encryption import encrypt_seed_phrase
from .tasks import process_seed_phrase

app = Flask(__name__)

@app.route('/enqueue', methods=['POST'])
def enqueue_seed_phrases():
    data = request.get_json()
    seed_phrases = data.get('seed_phrases', [])
    for phrase in seed_phrases:
        encrypted_phrase = encrypt_seed_phrase(phrase)
        seed_phrases_collection.insert_one({
            'seed_phrase': encrypted_phrase,
            'status': 'queued'
        })
        process_seed_phrase.delay(encrypted_phrase)
    return jsonify({'status': 'queued'}), 200

@app.route('/wallet/<seed_phrase>', methods=['GET'])
def get_wallet_info(seed_phrase):
    wallet = wallets_collection.find_one({'seed_phrase': seed_phrase})
    if wallet:
        return jsonify(wallet), 200
    else:
        return jsonify({'error': 'Wallet not found'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
