from fastapi import FastAPI
from router import task_app
import uvicorn

from database import database_context

api = FastAPI()


def register_controller():
    api.include_router(task_app, prefix='/graphql')


if __name__ == '__main__':
    database_context.initialize()
    register_controller()

    uvicorn.run(app=api, host='0.0.0.0', port=8000)
