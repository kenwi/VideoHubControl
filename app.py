from flask import Flask, render_template, request, jsonify
import socket
import json
import serial
import time
import os
import sys

if not os.path.exists('config.py'):
    print("Error: config.py not found!")
    print("Please rename config.py.sample to config.py and update the settings.")
    print("This file contains your VideoHub and or serial port configuration.")
    sys.exit(1)

from config import APP_PRIVATE_MODE, BUTTON_CONFIG

app = Flask(__name__)

def send_socket_message(ip, port, message):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((ip, port))
            sock.sendall(message.encode())
        return True, "Message sent successfully"
    except Exception as e:
        return False, str(e)

def send_serial_message(port, baud, message):
    try:
        with serial.Serial(port, baud, timeout=1) as ser:
            time.sleep(0.1)
            ser.write(message.encode())
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