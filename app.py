from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import responses, requests
from uvicorn import run as _run

from pathlib import Path
import webview

import utils

app = FastAPI(docs_url=None)

BASE_DIR = Path(__file__).resolve().parent

def getapp():
    return app

def run(port: int):
    _run(getapp(), port=port, host="127.0.0.1")

app.mount("/scripts", StaticFiles(directory=BASE_DIR / "scripts"), name="scripts")

templates = Jinja2Templates(directory=BASE_DIR / "app" / "templates")
app.mount("/static", StaticFiles(directory=BASE_DIR / "app" / "static"), name="static")

app.add_middleware(utils.NoCacheMiddleware)

@app.get("/", response_class=responses.HTMLResponse)
def index(request: requests.Request):
    return templates.TemplateResponse(request=request, name="index.html")

@app.get("/api/close", response_class=responses.HTMLResponse)
async def index(request: requests.Request):
    webview.destroy_window()
    return responses.RedirectResponse("/")