import os
import django


# Configura Django antes de hacer cualquier importación relacionada
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'infrastructure.django.settings')
django.setup()  # Asegura que las apps están listas

from fastapi import FastAPI
from driving.api_rest.router.router import add_routers

app = FastAPI()
add_routers(app)


@app.get("/health")
async def health_check():
    return {"status": "ok"}
