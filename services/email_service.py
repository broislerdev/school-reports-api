from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import os 
from dotenv import load_dotenv

load_dotenv()

client = SendGridAPIClient(api_key=os.getenv('SENDGRID_API_KEY'))

def send_report_email(report_id, student_name, complaint_message, category, created_at, status):

    email_message = Mail(
    from_email='urielbroisler@gmail.com',
    to_emails='broisler.uriel@gmail.com',
    subject='Nova denúncia recebida!',
    html_content=f"""
        <h2>Nova denúncia recebida</h2>

        <p><strong>ID:</strong> {report_id}</p>
        <p><strong>Aluno:</strong> {student_name or "Anônimo"}</p>
        <p><strong>Categoria:</strong> {category}</p>
        <p><strong>Data:</strong> {created_at}</p>
        <p><strong>Status:</strong> {status}</p>

        <hr>

        <p><strong>Mensagem da denúncia:</strong></p>
        <p>{complaint_message}</p>
        """

)
    client.send(email_message)