# main.py
from fastapi import FastAPI, Depends
from contextlib import asynccontextmanager
from app.routers import dashboard, journal, reconciliation, financial_reporting, system_setup, coa, user
from app.db.db_asyncpg import db

@asynccontextmanager
async def lifespan(app: FastAPI):
    await db.connect()
    yield
    await db.disconnect()


app = FastAPI(
    lifespan=lifespan,
    title="AAAAA",
    description="An Async Ai Accounting API",   
    version="1.1.1"
)


# Include routers
app.include_router(user.router,          prefix="/user",      tags=["User"])
app.include_router(coa.router,          prefix="/coa",      tags=["COA"])
app.include_router(dashboard.router,    prefix="/dashboard",tags=["Dashboard"])
app.include_router(journal.router,      prefix="/journal",  tags=["Journal"])
app.include_router(reconciliation.router,       prefix="/reconciliation", tags=["Reconciliation"])
app.include_router(financial_reporting.router,  prefix="/financial-reporting", tags=["Financial Reporting"])
app.include_router(system_setup.router,         prefix="/system-setup", tags=["System Setup"])

@app.on_event("startup")
async def startup():
    try:
        await db.connect()
        print("Database connection established on startup.")
    except Exception as e:
        print(f"Startup connection failed: {e}")

@app.on_event("shutdown")
async def shutdown():
    """Close the database connection when the app shuts down."""
    if db.pool:
        await db.pool.close()
        
@app.get("/")
def read_root():
    return {"message": "Welcome to the Accounting System API"}
