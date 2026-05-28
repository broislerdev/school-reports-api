from fastapi import FastAPI

from database.connection import base, db
from db_models.report_model import Report
from routers.auth_router import auth_router
from routers.report_router import report_router

app = FastAPI()

base.metadata.create_all(db)

with db.connect() as con:
    print("Conectado ao Supabase")

app.include_router(auth_router)
app.include_router(report_router)
