from fastapi import FastAPI
import uvicorn
from routes import routes
from starlette.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="ui/static"), name="static")
app.include_router(routes.router)

if __name__ == '__main__':
    from utils.app_logger import logger
    from utils.config import cfg

    logger.info('starting application %s' % cfg.APP_NAME)
    uvicorn.run(app, host="0.0.0.0", port=9090)


