from fastapi import APIRouter, Depends
from app.db.db_asyncpg import AsyncDatabase

router = APIRouter()


@router.get("/")
async def get_default_coa(db: AsyncDatabase = Depends()):
    """
    Fetch all default COA records from the database.
    """
    try:
        if not db.pool:
            return {"error": "Database11 connection is not established."}
        else:
            print("good good ")

        default_coa = await db.get_default_coa()
        return {"default_coa": default_coa}
    except Exception as e:
        return {"error": str(e)}
