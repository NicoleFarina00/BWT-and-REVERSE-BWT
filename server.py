import logging
from flask import Flask, request, jsonify
from bwt_utils import bwt, reverse_bwt

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)

@app.route('/bwt', methods=['POST'])
def bwt_endpoint():
    data = request.get_json()
    app.logger.debug(f"Received data: {data}")
    sequence = data.get('sequence', '')
    app.logger.debug(f"Received sequence for BWT: {sequence}")
    result = bwt(sequence)
    return jsonify(result=result)

@app.route('/reverse_bwt', methods=['POST'])
def reverse_bwt_endpoint():
    data= request.get_json()
    app.logger.debug(f"Received data: {data}")
    bwt_sequence = data.get('bwt', '')
    app.logger.debug(f"Received BWT sequence for reversal: {bwt_sequence}")
    try:
        result = reverse_bwt(bwt_sequence)
        return jsonify(result=result)
    except ValueError as e:
        app.logger.error(f"Error reversing BWT sequence: {str(e)}")
        return jsonify(error=str(e)), 400

if __name__ == '__main__':
    import configparser
    config = configparser.ConfigParser()
    config.read('config.cfg')
    host = config.get(section = 'server', option = 'host')
    port = config.getint(section='server', option='port')
    app.run(host=host, port=port)

