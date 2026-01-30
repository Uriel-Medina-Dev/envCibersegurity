from fastapi import FastAPI, HTTPException
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
    """Endpoint raiz que devuelve un saludo."""
    return {"Saludo": "xd"}

@app.get("/api/v1/users")
async def fetch_users() -> List[Usuario]:
    """Endpoint para obtener todos los usuarios."""
    return db

@app.post("/api/v1/users")
async def create_user(user: Usuario):
    """Endpoint para crear un nuevo usuario."""
    db.append(user)
    return {"message":"user created succesfully"}

@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    """Endpoint para eliminar a un usuario por su id"""
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return {"message":f"user with id {user_id} has been deleted succesfully"}
        
@app.put("/api/v1/users/{user_id}")
async def update_user(user_id:UUID, user_update:Usuario):
    """Endpoint para actualizar a un usuario por medio de su id"""
    for i, user in enumerate(db):
        if user.id == user_id:
            db[i] = user_update
            return {"message":f"user with id {user_id} has been updated succesfully"}
            """ Esto remplaza al usuario completo"""
            raise HTTPException(
                status_code=404, 
                detail=f"user with id {user_id} not found"
            )