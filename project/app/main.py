from app.api import ping, summaries
from app.config import log
from app.db import init_db
from fastapi import FastAPI


def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(ping.router)
    app.include_router(summaries.router, prefix="/summaries", tags=["summaries"])
    return app


app = create_app()


@app.on_event("startup")
async def startup_event():
    # Create an event start app
    log.info("Starting up...")
    init_db(app)


@app.on_event("shutdown")
async def shutdown_event():
    # Register an event for shutdown app
    log.info("Shutting down...")
