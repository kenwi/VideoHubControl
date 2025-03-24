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
