from fastapi import APIRouter

router = APIRouter()

@router.get("/clients")
def helloworld():
    return "Hello World"