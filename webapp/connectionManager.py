from fastapi import WebSocket
from userNameException import UserNameException
from threading import Lock

class ConnectionManager:
    def __init__(self):
        # Use dict to map connections to usernames and aquiure lock when modifying
        self.active_connections = {}
        self.lock = Lock()

    async def connect(self, websocket: WebSocket, username: str):
        await websocket.accept()
        with self.lock:
            # First check if username is already used
            # If used raise exception without adding connection
            if username in self.active_connections:
                raise UserNameException(message="Username is already in use")
            # Add connections with username as index
            self.active_connections[username] = websocket

    def disconnect(self, username: str):
        # Remove closed connection from dict
        with self.lock:
            self.active_connections.pop(username)

    async def broadcast(self, message: str):
        # Aquire lock so that no connection change during broadcast
        with self.lock:
            for connection in self.active_connections.values():
                # Send message to all connected clients
                await connection.send_text(message)
