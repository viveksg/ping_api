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

    {
      "line_protocol_data": [
           "ping_data,interface=lo status=unsuccessful 1538514601", 
           "ping_data,interface=enp3s0 status=unsuccessful 1538514601", 
           "ping_data,interface=wlp2s0 status=successful 1538514603", 
           "ping_data,interface=docker0 status=unsuccessful 1538514603"
       ]
    }
