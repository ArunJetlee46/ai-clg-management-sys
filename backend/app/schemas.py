from pydantic import BaseModel, EmailStr


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


class StudentCreate(BaseModel):
    roll_no: str
    name: str
    department: str
    semester: int


class StudentOut(StudentCreate):
    id: int

    class Config:
        from_attributes = True
