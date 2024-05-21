from os import getenv
from datetime import datetime
from fastapi import Request

def responders():
    startup_time = f'{datetime.now()}'
    api_version = getenv('SVC_VERSION')

    async def healthcheck_ping(request: Request):
        return {
            'startup_time': startup_time,
            'request_timestamp': f'{datetime.now()}',
            'hostname': request.client.host
        }

    async def healthcheck_status(request: Request):
        return {
            'service_name': 'total-rickall',
            'startup_time': startup_time,
            'hostname': request.client.host,
            'version': api_version
        }

    return [
        healthcheck_ping, 
        healthcheck_status
    ]