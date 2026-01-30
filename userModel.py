"""User model definitions."""
from enum import Enum
from typing import List, Optional
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class Genero(str, Enum):
    """Enum para los generos de usuarios."""
    masculino = "masculino"
    femenino = "femenino"
    otro = "otro"


class Rol(str, Enum):
    """Enum para los roles de usuarios."""
    admin = "admin"
    user = "user"
    guess = "guess"


class Usuario(BaseModel):
    """Modelo de usuario."""

    id: Optional[UUID] = Field(default_factory=uuid4)
    name: str
    lastname: str
    genero: Genero
    roles: List[Rol]