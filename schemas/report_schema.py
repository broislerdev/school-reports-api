from pydantic import BaseModel

class ReportCreate(BaseModel):
    student_name: str | None = None
    message: str
