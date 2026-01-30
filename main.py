from fastapi import FastAPI
from typing import List, Optional
from uuid import UUID, uuid4
from userModel import Genero,Rol,Usuario

app = FastAPI(
    title="User API",
    description="API para gestionar usuarios",
    version="1.0.0"
)

db:List[Usuario] = [
    Usuario(
        id=uuid4(),
        name="Uriel",
        lastname="Medina Torres",
        genero=Genero.masculino,
        roles=[Rol.admin]
    ),
    Usuario(
        id=uuid4(),
        name="Abdallah",
        lastname="Torres Medina",
        genero=Genero.masculino,
        roles=[Rol.user]
    ),
    Usuario(
        id=uuid4(),
        name="Diego",
        lastname="Bustamante Luján",
        genero=Genero.masculino,
        roles=[Rol.guess]
    )
]

@app.get("/")
async def root():
    return {"Saludo": "xd"}

@app.get("/api/v1/users")
async def get_users():
    return db