from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from router import task_app
import uvicorn

from database import database_context

api = FastAPI()


def register_controller():
    api.include_router(task_app, prefix='/graphql')


# Enable CORS
api.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this based on your needs
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == '__main__':
    database_context.initialize()
    register_controller()

    uvicorn.run(app=api, host='0.0.0.0', port=8000)
