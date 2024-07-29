
import uvicorn
from fastapi import FastAPI
from fastapi.security import HTTPBearer
from app.routers import card 
from app.routers import user
from app.config.database_configure import engine, Base
from fastapi.middleware.cors import CORSMiddleware

# Create the database tables
Base.metadata.create_all(bind=engine)

# FastAPI app instance
app = FastAPI()

token_auth_scheme = HTTPBearer()

origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:4200",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Include the routers
app.include_router(card.router, tags=["Cards"])
app.include_router(user.router, tags=["Users"])

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
