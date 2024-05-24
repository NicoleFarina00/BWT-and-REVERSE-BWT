import requests
import argparse
from fasta_utils import read_fasta

#Function to send a POST request to the server
def send_request(host, port, endpoint, data):
    #Construct the URL for the request
    url = f"http://{host}:{port}/{endpoint}"
    print(f"Sending request to URL: {url} with data: {data}")
    #Send the POST request with the provided data as JSON
    response = requests.post(url, json=data)
    print(f"Response status code: {response.status_code}")
    print(f"Response text: {response.text}")
    #Raise an exception if the request was unsuccessful
    response.raise_for_status()
    #Return the response JSON data
    return response.json()

if __name__ == "__main__":
    #Set up argument parser for command line arguments
    parser = argparse.ArgumentParser(description='BWT Client')
    parser.add_argument('--host', required=True, help='Server host')
    parser.add_argument('--port', required=True, help='Server port')
    parser.add_argument('--sequence', help='DNA sequence')
    parser.add_argument('--bwt', help='BWT sequence')
    parser.add_argument('--fasta', help='Path to FASTA file')
    args = parser.parse_args()

    #Determine which endpoint to use and prepare data based on provided arguments
    if args.fasta:
        #Read the sequence from a FASTA file
        sequence = read_fasta(args.fasta)
        endpoint = "bwt"
        data = {"sequence": sequence}
    elif args.sequence:
        #Use the provided DNA sequence
        endpoint = "bwt"
        data = {"sequence": args.sequence}
    elif args.bwt:
        #Use the provided BWT sequence
        endpoint = "reverse_bwt"
        data = {"bwt": args.bwt}
    else:
        #Raise an error if no valid argument is provided
        raise ValueError("Either --fasta, --sequence or --bwt must be provided.")

    print(f"Arguments: {args}")
    #Send the request to the server and print the response
    response = send_request(args.host, args.port, endpoint, data)
    print("Response:", response)