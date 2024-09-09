# Python Chat Application with Tkinter

A simple multi-client chat application built using Python's `socket` library for networking and `Tkinter` for the graphical user interface (GUI). The application consists of a server script that handles multiple client connections and a client script that provides a user-friendly GUI for chatting.

## Features

- **Multi-client support**: Multiple clients can connect to the server and communicate with each other in real-time.
- **GUI**: The client-side application provides a simple GUI using `Tkinter`.
- **Nicknames**: Users can choose a nickname when connecting to the server.
- **Broadcast Messaging**: Messages are broadcast to all connected clients.

## Prerequisites

Make sure you have the following installed:

- Python 3.x
- Required libraries: `socket`, `threading`, `tkinter`

## Getting Started

### Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/yourusername/chat-application.git
    cd chat-application
    ```

2. **Install Python**:

    Ensure you have Python 3.x installed on your machine. You can download it from the [official Python website](https://www.python.org/downloads/).

### Running the Server

1. Open a terminal or command prompt.
2. Navigate to the directory where `server.py` is located.
3. Run the server script:

    ```bash
    python server.py
    ```

   The server will start listening for incoming connections on `localhost` at port `12345`.

### Running the Client

1. Open another terminal or command prompt.
2. Navigate to the directory where `client.py` is located.
3. Run the client script:

    ```bash
    python client.py
    ```

4. When prompted, enter a nickname for the chat session.

5. The client GUI will open, and you can start chatting!

### Example Usage

- Start the server by running `server.py`.
- Run multiple instances of `client.py` to connect to the server.
- Enter your nickname in each client instance and start sending messages.
- Messages sent by any client will be broadcast to all connected clients.

## Files

- `server.py`: Server-side script that handles multiple client connections and message broadcasting.
- `client.py`: Client-side script that connects to the server and provides a chat GUI using `Tkinter`.

## Troubleshooting

- **Connection Errors**: Make sure the server is running before starting any client instances. Ensure that the server and client are on the same network or that the server's IP address is correctly configured in `client.py`.
- **Firewall Issues**: If you are unable to connect, check your firewall settings and allow traffic on port `12345`.
- **Port Conflicts**: Ensure that port `12345` is not being used by another application.


## Contributing

Contributions are welcome! Please fork this repository and submit a pull request with your changes. For major changes, please open an issue first to discuss what you would like to change.









