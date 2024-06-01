from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from connectionManager import ConnectionManager
from userNameException import UserNameException

app = FastAPI()
manager = ConnectionManager()

index_page = ""
with open('index.html', 'r') as f:
    index_page = f.read()

# Chatroom webpage
@app.get("/ws")
async def get():
    return HTMLResponse(index_page)

# Handle connection and broadcast messages
@app.websocket("/ws/{username}")
async def websocket_endpoint(websocket: WebSocket, username: str):
    try:
        await manager.connect(websocket, username)
        await manager.broadcast("Client #{} joined the chat".format(username))
        while True:
            message = await websocket.receive_text()
            await manager.broadcast("{}: {}".format(username, message))
    except UserNameException:
        # When username is already used by another client, close connection with event code
        await websocket.close(code=1003)
    except WebSocketDisconnect:
        # Disconnect user from chatroom and release username
        manager.disconnect(username)
        # Broadcast to all users
        await manager.broadcast("Client #{} left the chat".format(username))
