
import uvicorn
from fastapi import FastAPI
from app.routers.card import router as card_router
from app.routers.user import router as user_router
from app.config.database_configure import engine, Base
from fastapi.middleware.cors import CORSMiddleware

# Create the database tables
Base.metadata.create_all(bind=engine)

# FastAPI app instance
app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:4200",
    # Add more origins as needed
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Include the routers
app.include_router(card_router)
app.include_router(user_router)

@app.get("/")
async def home():
    return "Welcome to home"

# @app.on_event("startup")
# async def startup():
#     await database.connect()
#     create_tables()

# @app.on_event("shutdown")
# async def shutdown():
#     await database.disconnect()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
