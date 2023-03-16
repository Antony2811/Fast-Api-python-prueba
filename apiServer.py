from flask import Flask, request 
from datetime import datetime 
from app import hello_world

app = Flask(__name__) 

@app.route('/api/time', methods=['GET']) 

def get_time(): 

    api_type = request.args.get('tipo_api', 'hour') # Get the requested API type, default to 'hour' 

    if api_type == 'hour': 

        return datetime.now().strftime('%H') # Respond with the current hour in 24-hour format 

    elif api_type == 'datetime': 

        return datetime.now().strftime('%Y-%m-%d %H:%M:%S') # Respond with the current datetime in YYYY-MM-DD HH:MM:SS format 
    
    elif api_type == "mensaje":

        return hello_world

    else: 

        return 'Invalid API type requested. Valid types are "hour" and "datetime"' 

 

if __name__ == '__main__': 

    app.run(debug=True) 