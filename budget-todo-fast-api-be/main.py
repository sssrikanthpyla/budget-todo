
import uvicorn
from fastapi import FastAPI
from app.routers.card import router as card_router
from app.database.database_configure import engine, Base

# Create the database tables
Base.metadata.create_all(bind=engine)

# FastAPI app instance
app = FastAPI()

# Include the routers
app.include_router(card_router)

@app.get("/")
async def home():
    return "Welcome to home"

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
