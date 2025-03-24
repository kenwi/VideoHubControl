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

To change the mode, edit the `PRIVATE_MODE` variable in `app.py`:

- `PRIVATE_MODE = True` (default): Only accessible from localhost
- `PRIVATE_MODE = False`: Accessible from other devices on the network

## Running the Application

1. Make sure your virtual environment is activated
2. Run the Flask application:

   ```bash
   python app.py
   ```

3. Access the application:
   - From the same machine: Open your web browser and navigate to `http://localhost:5000`
   - From other devices on the network (only if PRIVATE_MODE is False): 
     Open your web browser and navigate to `http://<your-computer-ip>:5000`
     (Replace `<your-computer-ip>` with your computer's IP address on the local network)
