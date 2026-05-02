from flask import Flask, jsonify
import random

quotes = Flask(__name__)
import random

def random_quotes():
    with open('quotes.txt', 'r') as f:
        quotes_list = f.readlines()
    return random.choice(quotes_list).strip()

@quotes.route('/random_quote')
def get_random_quote():
    quote = random_quotes()
    return jsonify({'quote': quote})

if __name__ == '__main__':
    quotes.run(debug=True)