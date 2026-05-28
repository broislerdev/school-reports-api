from groq import Groq
import os 
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv('GROQ_API_KEY'))

def classify_complaint(complaint_text):
    response = client.chat.completions.create(
    model='llama-3.1-8b-instant',
    messages=[
        {'role': 'system', 'content': 'Você é um classificador de denuncias escolares. Classifique em: bullying: humilhação, perseguição, apelidos, exclusão repetida. violencia: ameaça, agressão física, briga, intimidação. assedio: toque sem consentimento, comentário sexual, perseguição sexual. discriminacao: racismo, homofobia, capacitismo, preconceito religioso etc. outro: quando não se encaixar nas anteriores Mas você deve retornar só a categoria'},
        {'role': 'user', 'content': complaint_text}
    ]
)
    category = response.choices[0].message.content.strip()
    return category
    
    