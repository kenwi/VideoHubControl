# VideoHub Control

## Installation

1. Clone this repository
2. Create a virtual environment (recommended/optional):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Configuration

The application can be run in two modes:

- Private mode (default): Only accessible from the local machine (localhost)
- Public mode: Accessible from other devices on the network

To change the mode, edit the `APP_PRIVATE_MODE` variable in `app.py`:

- `APP_PRIVATE_MODE = True` (default): Only accessible from localhost
- `APP_PRIVATE_MODE = False`: Accessible from other devices on the network

### VideoHub Connection Settings

The application sends control messages to a VideoHub device using the following configuration in `app.py`:

- `VIDEOHUB_HOST`: The IP address of the VideoHub device (default: "192.168.10.129")
- `VIDEOHUB_PORT`: The port number for the VideoHub connection (default: 4444)

These settings control where the button press messages are sent. Make sure to update these values to match your VideoHub device's network configuration.

The `SOCKET_CONFIG` dictionary in `app.py` defines the control messages sent to the VideoHub device when each button is pressed. The current messages ("Button X pressed") are placeholder values and should be replaced with the actual control commands as specified in your VideoHub device's documentation. Each button can send a different command to control various functions of the VideoHub.

### Button Naming Convention

For better code maintainability and clarity, buttons should be named according to their function rather than using generic names like "button1", "button2", etc. For example:

```python
SOCKET_CONFIG = {
    'button_turn_off_lights': {'ip': VIDEOHUB_HOST, 'port': VIDEOHUB_PORT, 'message': 'LIGHTS_OFF\n'},
    'button_turn_on_lights': {'ip': VIDEOHUB_HOST, 'port': VIDEOHUB_PORT, 'message': 'LIGHTS_ON\n'},
    'button_switch_input_1': {'ip': VIDEOHUB_HOST, 'port': VIDEOHUB_PORT, 'message': 'INPUT_1\n'},
    'button_switch_input_2': {'ip': VIDEOHUB_HOST, 'port': VIDEOHUB_PORT, 'message': 'INPUT_2\n'}
}
```

To implement this change, you need to update three sections of the code:

1. In `templates/index.html`:
   - Update the button IDs in the HTML:

     ```html
     <button id="button_turn_off_lights" class="button">Turn Off Lights</button>
     <button id="button_turn_on_lights" class="button">Turn On Lights</button>
     ```

2. In `templates/index.html`:
   - Update the CSS selectors if you want to maintain specific colors for each button:

     ```css
     #button_turn_off_lights { background-color: #4CAF50; }
     #button_turn_on_lights { background-color: #2196F3; }
     ```

3. In `app.py`:
   - Update the `SOCKET_CONFIG` dictionary keys to match the new button IDs
   - Update the messages to match your VideoHub's command protocol

   ```python
   # Before:
   SOCKET_CONFIG = {
       'button1': {'ip': VIDEOHUB_HOST, 'port': VIDEOHUB_PORT, 'message': 'Button 1 pressed\n'},
       'button2': {'ip': VIDEOHUB_HOST, 'port': VIDEOHUB_PORT, 'message': 'Button 2 pressed\n'},
       'button3': {'ip': VIDEOHUB_HOST, 'port': VIDEOHUB_PORT, 'message': 'Button 3 pressed\n'},
       'button4': {'ip': VIDEOHUB_HOST, 'port': VIDEOHUB_PORT, 'message': 'Button 4 pressed\n'}
   }

   # After:
   SOCKET_CONFIG = {
       'button_turn_off_lights': {'ip': VIDEOHUB_HOST, 'port': VIDEOHUB_PORT, 'message': 'LIGHTS_OFF\n'},
       'button_turn_on_lights': {'ip': VIDEOHUB_HOST, 'port': VIDEOHUB_PORT, 'message': 'LIGHTS_ON\n'},
       'button_switch_input_1': {'ip': VIDEOHUB_HOST, 'port': VIDEOHUB_PORT, 'message': 'INPUT_1\n'},
       'button_switch_input_2': {'ip': VIDEOHUB_HOST, 'port': VIDEOHUB_PORT, 'message': 'INPUT_2\n'}
   }
   ```

This naming convention makes the code more self-documenting and easier to maintain, as the purpose of each button is immediately clear from its identifier.

## Running the Application

1. Make sure your virtual environment is activated
2. Run the Flask application:

   ```bash
   python app.py
   ```

3. Access the application:
   - From the same machine: Open your web browser and navigate to `http://localhost:5000`
   - From other devices on the network (only if APP_PRIVATE_MODE is False): 
     Open your web browser and navigate to `http://<your-computer-ip>:5000`
     (Replace `<your-computer-ip>` with your computer's IP address on the local network)
