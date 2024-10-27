import subprocess
from fastapi import FastAPI
from app.db import initialize_db
from app.routers import api_router  # import the aggregated API router
from config import PORT

app = FastAPI()

# initializing db
try:
    initialize_db()
except Exception as e:
    print(f"An error occurred during database initialization: {e}")

# register the aggregated API router
app.include_router(api_router)

# shutdown event handler
@app.on_event("shutdown")
async def shutdown():
    print("Cleaning up resources and shutting down gracefully...")
    try:
        # find process using port
        result = subprocess.run(["lsof", "-t", "-i:{PORT}"], capture_output=True, text=True)
        pid = result.stdout.strip()
        
        if pid:
            print(f"Killing process {pid} on port {PORT}")
            subprocess.run(["kill", "-9", pid])  # kill it
        else:
            print("No process found using port {PORT}")

    except Exception as e:
        print(f"An error occurred while trying to kill the process on port {PORT}: {e}")