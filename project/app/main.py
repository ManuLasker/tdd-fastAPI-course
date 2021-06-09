from app.db import init_db
from fastapi import FastAPI
from app.api import ping
from app.api import summaries
from app.config import log

def create_app() -> FastAPI:
    app = FastAPI()

    app.include_router(ping.router)
    app.include_router(summaries.router, prefix="/summaries", tags=["summaries"])
    
    return app

app = create_app()

# Create an event start app
@app.on_event("startup")
async def startup_event():
    log.info("Starting up...")
    init_db(app)

# Register an event for shutdown app
@app.on_event("shutdown")
async def shutdown_event():
    log.info("Shutting down...")