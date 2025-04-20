from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class UserBase(BaseModel):
    username: str = Field(..., description="Nombre de usuario único")
    email: EmailStr = Field(..., description="Correo electrónico válido")

class UserCreate(UserBase):
    password: str = Field(..., min_length=6, description="Contraseña segura (mínimo 6 caracteres)")

class UserLogin(BaseModel):
    email: EmailStr = Field(..., description="Correo electrónico del usuario")
    password: str = Field(..., description="Contraseña del usuario")

class UserResponse(UserBase):
    id: int = Field(..., description="ID único del usuario")
    is_active: bool = Field(..., description="Indica si el usuario está activo")

    class Config:
        orm_mode = True
