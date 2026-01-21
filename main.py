from fastapi import fastapi
from typing import List, Optional
from uuid import UUID, uuid4
from userModel import Genero,Rol,Usuario
app = FastApi()

db:List[Usuario] = [
    Usuario(
        id=uuid4(),
        name="Uriel",
        lastname="Medina Torres",
        genero=genero.masculino,
        roles=[Role.admin]
    ),
    Usuario(
        id=uuid4(),
        name="Abdallah",
        lastname="Torres Medina",
        genero=genero.masculino,
        roles=[Role.user]
    ),
    Usuario(
        id=uuid4(),
        name="Diego",
        lastname="Bustamante Luján",
        genero=genero.masculino,
        roles=[Role.guess]
    )
]

@app.get(/)
async def root():
    return("Saludo":"xd")

@app.get("/api/v1/users")
async def get_users():
    return db