import google.cloud.logging
from dotenv import load_dotenv
from fastapi import FastAPI

from . import trucks

load_dotenv()

client = google.cloud.logging.Client()
client.setup_logging()


def create_app():
    app = FastAPI()
    app.include_router(trucks.router)
    return app
