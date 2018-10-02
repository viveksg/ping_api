# ping_api
Allow to check network status of individual interfaces.

## Requirements
python3
flask

## Installation
Open terminal, Go in top project directory and type  
pip install -r requirements.txt  
or  
pip3 install -r requirements.txt  

## Starting Server
Open terminal, Go in top project directory and type  
chmod +x start_server.sh  
./start_server.sh

## Request
http://0.0.0.0:5000/ping?host=<host name>  
So if you want to test using google.com  
http://0.0.0.0:5000/ping?host=google.com  

Output will be line_protocol_data in json
