import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'infrastructure.django.settings')
django.setup()

from fastapi import FastAPI
from driving.api_rest.router.router import add_routers
from driving.api_rest.containers.containers import add_containers

app = FastAPI()
add_routers(app)
add_containers(app)


@app.get("api/health")
async def health_check():
    return {"status": "ok"}
