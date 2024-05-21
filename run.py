from pathlib import Path
from dotenv import load_dotenv
from fastapi import FastAPI, Request
from total_rickall import responders


if Path('.env').is_file():
    load_dotenv(Path('.env').resolve())
get_ping_response, get_status_response = responders()
app = FastAPI()


@app.get("/healthcheck/ping")
async def get_healthcheck_ping(request: Request):
    return await get_ping_response(request)


@app.get("/healthcheck/status")
async def get_healthcheck_status(request: Request):
    return await get_status_response(request)