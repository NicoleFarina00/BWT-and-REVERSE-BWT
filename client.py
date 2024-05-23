import requests
import argparse
from fasta_utils import read_fasta

def send_request(host, port, endpoint, data):
    url = f"http://{host}:{port}/{endpoint}"
    print(f"Sending request to URL: {url} with data: {data}")
    response = requests.post(url, json=data)
    print(f"Response status code: {response.status_code}")
    print(f"Response text: {response.text}")
    response.raise_for_status()
    return response.json()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='BWT Client')
    parser.add_argument('--host', required=True, help='Server host')
    parser.add_argument('--port', required=True, help='Server port')
    parser.add_argument('--sequence', help='DNA sequence')
    parser.add_argument('--bwt', help='BWT sequence')
    parser.add_argument('--fasta', help='Path to FASTA file')
    args = parser.parse_args()

    if args.fasta:
        sequence = read_fasta(args.fasta)
        endpoint = "bwt"
        data = {"sequence": sequence}
    elif args.sequence:
        endpoint = "bwt"
        data = {"sequence": args.sequence}
    elif args.bwt:
        endpoint = "reverse_bwt"
        data = {"bwt": args.bwt}
    else:
        raise ValueError("Either --fasta, --sequence or --bwt must be provided.")

    print(f"Arguments: {args}")
    response = send_request(args.host, args.port, endpoint, data)
    print("Response:", response)