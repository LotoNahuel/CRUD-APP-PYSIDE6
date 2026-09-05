from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse

app = FastAPI(tittle="SCHOOL APP")

html = """
<!DOCTYPE html>
<html>
<head>
    <title>CHAT</title>
</head>
<body>
    <h1>CHAT</h1>
</body>
"""
@app.get("/")
def root():
# async def get():
    return HTMLResponse(content=html)

@app.get("/subjects")
def get_subjects():
    return [
        {"id": 0, "name": "Literature"},
        {"id": 1, "name": "History"},
    ]

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Mensaje Recibido: {data}")