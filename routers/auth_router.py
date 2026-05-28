from fastapi import APIRouter

auth_router = APIRouter(prefix="/auth", tags=["auth"])


@auth_router.get("/")
async def authenticate():
    """
    Rota de autenticacao do Usuario.
    """
    return {"mensagem": "Usuario acessando rota de autenticacao", "auth": False}
