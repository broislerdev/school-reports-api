from sqlalchemy import Column, DateTime, Integer, String
from database.connection import base

class Report(base):
    __tablename__ = "reports"

    report_id = Column(Integer, primary_key=True, autoincrement=True)
    student_name = Column(String, nullable=True)
    message = Column(String)
    category = Column(String)
    created_at = Column(DateTime)
    status = Column(String)