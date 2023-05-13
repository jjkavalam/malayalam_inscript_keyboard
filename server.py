from flask import Flask, request
from ai4bharat.transliteration import XlitEngine
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)

e = XlitEngine("ml")

@app.route('/transliterate', methods=['GET'])
def transform_string():
    input_string = request.args.get('input')
    return e.translit_sentence(input_string)

if __name__ == '__main__':
    app.run(debug=False)
