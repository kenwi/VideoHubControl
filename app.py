from flask import Flask, render_template, request, jsonify
import socket
import json

app = Flask(__name__)

# Configuration
PRIVATE_MODE = True  # Set to False to allow access from other devices on the network
HOST = "192.168.10.129"
PORT = 4444
SOCKET_CONFIG = {
    'button1': {'ip': HOST, 'port': PORT, 'message': 'Button 1 pressed\n'},
    'button2': {'ip': HOST, 'port': PORT, 'message': 'Button 2 pressed\n'},
    'button3': {'ip': HOST, 'port': PORT, 'message': 'Button 3 pressed\n'},
    'button4': {'ip': HOST, 'port': PORT, 'message': 'Button 4 pressed\n'}
}

def send_socket_message(ip, port, message):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((ip, port))
        sock.sendall(message.encode())
        sock.close()
        return True, "Message sent successfully"
    except Exception as e:
        return False, str(e)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    button_id = request.json.get('button_id')
    if button_id in SOCKET_CONFIG:
        config = SOCKET_CONFIG[button_id]
        success, message = send_socket_message(config['ip'], config['port'], config['message'])
        return jsonify({'success': success, 'message': message})
    return jsonify({'success': False, 'message': 'Invalid button ID'})

if __name__ == '__main__':
    host = '127.0.0.1' if PRIVATE_MODE else '0.0.0.0'
    app.run(host=host, debug=True) 