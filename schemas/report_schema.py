from pydantic import BaseModel
from enum import Enum

class StatusRegister(str, Enum):
    novo = 'novo'
    em_analise = 'em_analise' 
    encaminhado = 'encaminhado'
    resolvido = 'resolvido'
    arquivado = 'arquivado'

class ReportCreate(BaseModel):
    student_name: str | None = None
    message: str

class ReportStatusUpdate(BaseModel):
    status: StatusRegister 