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

4. Set up configuration:
   - Rename `config.py.sample` to `config.py`
   - Edit `config.py` with your specific settings

## Configuration

The application can be run in two modes:

- Private mode (default): Only accessible from the local machine (localhost)
- Public mode: Accessible from other devices on the network

To change the mode, edit the `APP_PRIVATE_MODE` variable in `config.py`:

- `APP_PRIVATE_MODE = True` (default): Only accessible from localhost
- `APP_PRIVATE_MODE = False`: Accessible from other devices on the network

### VideoHub Connection Settings

The application can send control messages to a VideoHub device using either TCP socket or Serial communication. The configuration in `config.py` includes settings for both methods:

#### TCP Socket Settings

- `VIDEOHUB_HOST`: The IP address of the VideoHub device (default: "192.168.10.129")
- `VIDEOHUB_PORT`: The port number for the VideoHub connection (default: 4444)

#### Serial Settings

- `TV0_PORT`: The serial port for TV0 (default: "COM1")
- `TV0_BAUD`: The baud rate for TV0 (default: 9600)
- `TV1_PORT`: The serial port for TV1 (default: "COM2")
- `TV1_BAUD`: The baud rate for TV1 (default: 9600)

These settings control where the button press messages are sent. Make sure to update these values to match your VideoHub device's network configuration.

The `BUTTON_CONFIG` dictionary in `config.py` defines the control messages sent to the VideoHub device when each button is pressed. Each button configuration can specify which method to use ('socket' or 'serial') and its corresponding settings. For example:

```python
BUTTON_CONFIG = {
    'button_turn_off_lights': {
        'method': 'socket',  # Use TCP socket communication
        'ip': VIDEOHUB_HOST,
        'port': VIDEOHUB_PORT,
        'message': 'LIGHTS_OFF\n'
    },
    'button_switch_input_1': {
        'method': 'serial',  # Use serial communication
        'port': TV0_PORT,
        'baud': TV0_BAUD,
        'message': 'INPUT_1\n'
    }
}
```

The current messages are placeholder values and should be replaced with the actual control commands as specified in your VideoHub device's documentation. Each button can send a different command to control various functions of the VideoHub.

### Button Naming Convention

For better code maintainability and clarity, buttons should be named according to their function rather than using generic names like "button1", "button2", etc. For example:

```python
BUTTON_CONFIG = {
    'button_turn_off_lights': {
        'method': 'socket',
        'ip': VIDEOHUB_HOST,
        'port': VIDEOHUB_PORT,
        'message': 'LIGHTS_OFF\n'
    },
    'button_turn_on_lights': {
        'method': 'socket',
        'ip': VIDEOHUB_HOST,
        'port': VIDEOHUB_PORT,
        'message': 'LIGHTS_ON\n'
    },
    'button_switch_input_1': {
        'method': 'serial',
        'port': TV0_PORT,
        'baud': TV0_BAUD,
        'message': 'INPUT_1\n'
    },
    'button_switch_input_2': {
        'method': 'serial',
        'port': TV1_PORT,
        'baud': TV1_BAUD,
        'message': 'INPUT_2\n'
    }
}
```

To implement this change, you need to update three sections of the code:

1. In `templates/index.html`:
   - Update the button IDs in the HTML:

     ```html
     <button id="button_turn_off_lights" class="button">Turn Off Lights</button>
     <button id="button_turn_on_lights" class="button">Turn On Lights</button>
     ```

   - Update the CSS selectors if you want to maintain specific colors for each button:

     ```css
     #button_turn_off_lights { background-color: #4CAF50; }
     #button_turn_on_lights { background-color: #2196F3; }
     ```

2. In `config.py`:
   - Update the `BUTTON_CONFIG` dictionary keys to match the new button IDs
   - Update the messages to match your VideoHub's command protocol

   ```python
   # Before:
   BUTTON_CONFIG = {
       'button1': {
           'method': 'socket',
           'ip': VIDEOHUB_HOST,
           'port': VIDEOHUB_PORT,
           'message': 'Button 1 pressed\n'
       },
       'button2': {
           'method': 'socket',
           'ip': VIDEOHUB_HOST,
           'port': VIDEOHUB_PORT,
           'message': 'Button 2 pressed\n'
       },
       'button3': {
           'method': 'serial',
           'port': TV0_PORT,
           'baud': TV0_BAUD,
           'message': 'Button 3 pressed\n'
       },
       'button4': {
           'method': 'serial',
           'port': TV1_PORT,
           'baud': TV1_BAUD,
           'message': 'Button 4 pressed\n'
       }
   }

   # After:
   BUTTON_CONFIG = {
       'button_turn_off_lights': {
           'method': 'socket',
           'ip': VIDEOHUB_HOST,
           'port': VIDEOHUB_PORT,
           'message': 'LIGHTS_OFF\n'
       },
       'button_turn_on_lights': {
           'method': 'socket',
           'ip': VIDEOHUB_HOST,
           'port': VIDEOHUB_PORT,
           'message': 'LIGHTS_ON\n'
       },
       'button_switch_input_1': {
           'method': 'serial',
           'port': TV0_PORT,
           'baud': TV0_BAUD,
           'message': 'INPUT_1\n'
       },
       'button_switch_input_2': {
           'method': 'serial',
           'port': TV1_PORT,
           'baud': TV1_BAUD,
           'message': 'INPUT_2\n'
       }
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
