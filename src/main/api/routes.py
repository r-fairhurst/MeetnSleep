from fastapi import APIRouter

router = APIRouter()

@router.get("/example")
def example_route():
    return {"message": "This is a testing route"}