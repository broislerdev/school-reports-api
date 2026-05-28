from datetime import datetime
from fastapi import APIRouter
from database.connection import SessionLocal
from db_models.report_model import Report
from schemas.report_schema import ReportCreate
from services.groq_service import classify_complaint
import logging

report_router = APIRouter(prefix="/reports", tags=["report"])
logger = logging.getLogger(__name__)


@report_router.get("/")
async def reports():
    session = SessionLocal()
    reports = session.query(Report).all()
    report_list = []

    for report in reports:
        report_dict = {
            "report_id": report.report_id,
            "student_name": report.student_name,
            "message": report.message,
            "category": report.category,
            "created_at": report.created_at,
            "status": report.status,
        }
        report_list.append(report_dict)

    session.close()
    return report_list

@report_router.post("/")
async def create_report(report: ReportCreate):
    try:
        category = classify_complaint(report.message)
    except Exception:
        logger.exception('Error classifying a report with Groq')
        category = 'pendente'

    new_report = Report(
        student_name=report.student_name,
        message=report.message,
        category=category,
        created_at=datetime.now().replace(microsecond=0),
        status="novo",
    )

    session = SessionLocal()
    session.add(new_report)
    session.commit()
    session.refresh(new_report)

    response = {
        "report_id": new_report.report_id,
        "student_name": new_report.student_name,
        "message": new_report.message,
        "category": new_report.category,
        "created_at": new_report.created_at,
        "status": new_report.status,
    }

    session.close()
    return response
