from fastapi import FastAPI
from src.main.api.routes import router
import uvicorn
import threading
from src.main.services.speech_recognition_service import listen_for_speech

app = FastAPI()

# Include API routes
app.include_router(router)

@app.get("/")
def home():
    return {"message": "MeetnSleep is running!"}

def start_speech_listener():
    while True:
        listen_for_speech()

if __name__ == "__main__":
    # Start speech listener in a separate thread
    speech_thread = threading.Thread(target=start_speech_listener, daemon=True)
    speech_thread.start()
    
    # Run the FastAPI server
    uvicorn.run("src.main.app:app", host="0.0.0.0", port=8000, reload=True)