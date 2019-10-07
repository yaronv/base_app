import os

from fastapi import APIRouter
from starlette.requests import Request
from starlette.responses import JSONResponse, StreamingResponse
from starlette.templating import Jinja2Templates
import datetime

router = APIRouter()
templates = Jinja2Templates(directory="ui/templates")
start_time = datetime.datetime.now()


@router.get("/")
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "date": datetime.datetime.now()})

@router.get("/health")
async def health():
    return JSONResponse({'status': 'API is running', 'start-time': '%s' % start_time})


@router.get('/log')
async def show_log():
    from utils.config import cfg
    f = open(os.path.join(cfg.APP_LOGS_DIR, cfg.APP_NAME + '.log'), 'r')
    return StreamingResponse(f)


@router.get('/read/{name}')
async def read(name):
    from utils.config import cfg
    from utils.app_logger import logger
    path = os.path.join(cfg.APP_BASE_DIR, name)
    logger.info('reading file %s' % path)
    f = open(path, 'r')
    return StreamingResponse(f)
