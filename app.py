from fastapi import FastAPI, Request
from pydantic import BaseModel
from dotenv import dotenv_values
from pymongo import MongoClient
from fastapi.responses import JSONResponse
from routes.route import router 
from rediss import rate_limiting
config = dotenv_values(".env")
app= FastAPI()

from fastapi.responses import JSONResponse

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    client_ip = request.client.host
    try:
        rate =await rate_limiting(client_ip)
        if rate:
            response =await call_next(request)
            return response
    except Exception as e:
        return JSONResponse(status_code=500, content={"detail": str(e)})
    return JSONResponse(status_code=429, content={"detail": "Rate limit exceeded. Try again in 5 seconds."})

@app.get('/')
def read_root():
    return {"msg": "Hello World"}


@app.on_event("startup")
def startup_db_client():
    app.mongodb_client = MongoClient(config["ATLAS_URI"])
    app.database = app.mongodb_client[config["DB_NAME"]]
    print("Starting up DATABASE")


@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()
    
    

app.include_router(router, tags=["students"], prefix="/students")

