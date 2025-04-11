from flask import Flask, render_template, request, jsonify
from socket import socket, AF_INET, SOCK_STREAM
from serial import Serial
from time import sleep
from os import path
from sys import exit

if not path.exists('config.py'):
    print("Error: config.py not found!")
    print("Please rename config.py.sample to config.py and update the settings.")
    print("This file contains your VideoHub and or serial port configuration.")
    exit(1)

from config import APP_PRIVATE_MODE, BUTTON_CONFIG

app = Flask(__name__)

def send_socket_message(ip, port, message):
    try:
        with socket(AF_INET, SOCK_STREAM) as sock:
            sock.connect((ip, port))
            sock.sendall(message.encode())
        return True, "Message sent successfully"
    except Exception as e:
        return False, str(e)

def send_serial_message(port, baud, message):
    try:
        with Serial(port, baud, timeout=1) as ser:
            sleep(0.1)
            if isinstance(message, str):
                message = message.encode()
            ser.write(message)
        return True, "Message sent successfully"
    except Exception as e:
        return False, str(e)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    button_id = request.json.get('button_id')
    if button_id in BUTTON_CONFIG:
        config = BUTTON_CONFIG[button_id]
        method = config['method']
        
        if method == 'socket':
            success, message = send_socket_message(config['ip'], config['port'], config['message'])
        elif method == 'serial':
            success, message = send_serial_message(config['port'], config['baud'], config['message'])
        else:
            return jsonify({'success': False, 'message': 'Invalid message sending method'})
            
        return jsonify({'success': success, 'message': message})
    return jsonify({'success': False, 'message': 'Invalid button ID'})

if __name__ == '__main__':
    host = '127.0.0.1' if APP_PRIVATE_MODE else '0.0.0.0'
    app.run(host=host, debug=True) 