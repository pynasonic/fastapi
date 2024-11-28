from fastapi import APIRouter

router = APIRouter()

@router.get("/bizentity-setup")
def biz_entity_setup():
    return {"message": "BizEntity Setup"}

@router.get("/initialization")
def system_initialization():
    return {"message": "System Initialization"}
