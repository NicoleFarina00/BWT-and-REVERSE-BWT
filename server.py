import logging
from flask import Flask, request, jsonify
from bwt_utils import bwt, reverse_bwt

#Create a Flask application instance
app = Flask(__name__)
#Set up logging to display debug messages
logging.basicConfig(level=logging.DEBUG)

#Define an endpoint for BWT transformation
@app.route('/bwt', methods=['POST'])
def bwt_endpoint():
    #Get the JSON data from the request
    data = request.get_json()
    #Log the received data
    app.logger.debug(f"Received data: {data}")
    #Extract the sequence from the received data
    sequence = data.get('sequence', '')
    #Log the received sequence
    app.logger.debug(f"Received sequence for BWT: {sequence}")
    #Perform the BWT transformation
    result = bwt(sequence)
    #Return the result as a JSON response
    return jsonify(result=result)

#Define an endpoint for reversing the BWT transformation
@app.route('/reverse_bwt', methods=['POST'])
def reverse_bwt_endpoint():
    #Get the JSON data from the request
    data= request.get_json()
    #Log the received data
    app.logger.debug(f"Received data: {data}")
    #Extract the BWT sequence from the received data
    bwt_sequence = data.get('bwt', '')
    #Log the received BWT sequence
    app.logger.debug(f"Received BWT sequence for reversal: {bwt_sequence}")
    try:
        #Attempt to reverse the BWT transformation
        result = reverse_bwt(bwt_sequence)
       #Return the result as a JSON response
        return jsonify(result=result)
    except ValueError as e:
        #Log an error message if reversal fails
        app.logger.error(f"Error reversing BWT sequence: {str(e)}")
        #Return an error message as a JSON response with a 400 status code
        return jsonify(error=str(e)), 400

if __name__ == '__main__':
    #Import configparser to read the configuration file
    import configparser
    #Create a ConfigParser instance
    config = configparser.ConfigParser()
    #read the configuration file
    config.read('config.cfg')
    #Get the host and port from the configuration file
    host = config.get(section = 'server', option = 'host')
    port = config.getint(section='server', option='port')
    #Run the Flask application with the specified host and port
    app.run(host=host, port=port)

