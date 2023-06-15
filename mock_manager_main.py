import uvicorn
import mock_manager
from fastapi import FastAPI

app: FastAPI = FastAPI()
base_url: str = "/api"
app.include_router(mock_manager.router, prefix=base_url)

if __name__ == '__main__':
    uvicorn.run('mock_manager_main:app', host='0.0.0.0', port=80, reload=True)
