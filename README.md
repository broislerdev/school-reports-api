# 🏫 School Reports API

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![Supabase](https://img.shields.io/badge/Supabase-3ECF8E?style=for-the-badge&logo=supabase&logoColor=white)
![Status](https://img.shields.io/badge/Status-In%20Progress-orange)

A REST API for managing anonymous school reports. Students can submit complaints about bullying, violence, and other issues — automatically classified by AI and notified to school coordination via email.



## 🚀 How to run

**1. Clone the repository:**

```
git clone https://github.com/broislerdev/school-reports-api.git
cd school-reports-api
```

**2. Create a virtual environment and install dependencies:**

```
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

**3. Set up your `.env` file based on `.env.example`:**

```env
DATABASE_URL=your_supabase_connection_string
SUPABASE_KEY=your_supabase_key
SECRET_KEY=your_secret_key
GROQ_API_KEY=your_groq_api_key
SENDGRID_API_KEY=your_sendgrid_api_key
SENDGRID_FROM_EMAIL=your_verified_sender_email
COORDINATION_EMAIL=coordination_email
```

**4. Run the server:**

```
uvicorn main:app --reload
```

**5. Access the interactive docs:**

```
http://localhost:8000/docs
```



## 🕹️ Endpoints

|Method|Endpoint              |Description         |
|------|----------------------|--------------------|
|GET   |`/reports/`           |List all reports    |
|GET   |`/reports/{id}`       |Get report by ID    |
|POST  |`/reports/`           |Submit a new report |
|PATCH |`/reports/{id}/status`|Update report status|

-----

## 🔁 Report Flow

1. Student submits a report via `POST /reports/`
1. **Groq AI** automatically classifies the complaint
1. Report is saved to **Supabase** (PostgreSQL)
1. **SendGrid** sends an email notification to the coordinator
1. Coordinator can view all reports and update their status



## ✅ Features

- 🕵️ **Anonymous reports** — student name is optional
- 🤖 **AI classification** — automatically categorizes complaints using Groq (Llama 3.1)
- 📧 **Email notifications** — coordinator is notified via SendGrid on every new report
- 📋 **Status tracking** — reports can be tracked through `novo → em_analise → encaminhado → resolvido`
- 🛡️ **Input validation** — Pydantic schemas for all endpoints



## 🗂️ Project Structure

```
school-reports-api/
├── database/
│   └── connection.py       # SQLAlchemy engine and session
├── db_models/
│   └── report_model.py     # Report ORM model
├── routers/
│   ├── auth_router.py      # Auth routes
│   └── report_router.py    # Report CRUD routes
├── schemas/
│   └── report_schema.py    # Pydantic validation schemas
├── services/
│   ├── groq_service.py     # AI classification service
│   └── email_service.py    # Email notification service
├── main.py
├── .env.example
└── requirements.txt
```



## 🧠 Concepts applied

- REST API with FastAPI
- ORM with SQLAlchemy
- Data validation with Pydantic
- AI integration with Groq (Llama 3.1)
- Email notifications with SendGrid
- PostgreSQL on Supabase
- Environment variables with python-dotenv
- Separation of concerns (routers / services / models / schemas)



## 🛠️ Built with

- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Supabase](https://supabase.com/)
- [Groq](https://groq.com/)
- [SendGrid](https://sendgrid.com/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
