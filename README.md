# BWT Server and Client

This project implements a server and a client for Burrows-Wheeler 
Transform (BWT) and its reversal. The Burrows-Wheeler Transform is a 
lossless data compression algorithm.

## File Contents

- **bwt_utils.py**: Contains functions to perform BWT transformation, 
calculate lexicographic order, ranks, positions, and character counts, as 
well as to reverse the BWT transformation.
  
- **server.py**: Implements a Flask server that provides two API endpoints 
for performing BWT transformation and reversing BWT transformation.

- **client.py**: Implements a client to send requests to the server to 
perform BWT transformation and reverse BWT transformation.

- **fasta_utils.py**: Contains a function to read sequences from FASTA 
files.

- **requirements.txt**: Lists the required Python packages for the 
project.

- **config.cfg**: Configuration file specifying the host and port of the 
server.

## Functionality

1. **BWT Transformation**: When the client sends a sequence to the server 
via the `/bwt` endpoint, the server calculates the BWT transformation of 
the sequence and returns it to the client.

2. **Reversal of BWT Transformation**: When the client sends a BWT 
sequence to the server via the `/reverse_bwt` endpoint, the server 
reverses the BWT transformation and returns the original sequence to the 
client.

## Server and Client Setup

1. **Server Setup**:
   - Ensure Python is installed on your system.
   - Install the required packages by running `pip install -r 
requirements.txt`.
   - Modify the `config.cfg` file if you want to change the host and port 
of the server.
   - Start the server by running `python server.py`.

2. **Client Setup**:
   - Ensure Python is installed on your system.
   - Install the required packages by running `pip install -r 
requirements.txt`.
   - Run the client by specifying the host, port, and desired action (BWT 
transformation or reversal of BWT transformation). You can provide the 
sequence either directly from the command line or via a FASTA file using 
the `--fasta` option.

## Examples of Client Usage

1. **Perform BWT Transformation**:

python client.py --host <server_host> --port <server_port> --sequence 
"BANANA"


2. **Reverse BWT Transformation**:

python client.py --host <server_host> --port <server_port> --bwt "ANNB$AA"


3. **Perform BWT Transformation from a FASTA file**:

python client.py --host <server_host> --port <server_port> --fasta 
"sequence.fasta"


Note: Ensure to replace `<server_host>` and `<server_port>` with the host 
and port of the server specified in the `config.cfg` file.

