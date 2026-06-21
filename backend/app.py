"""
app.py
"""

from fastapi import FastAPI

from database import Base,engine

from routers.release import router

from services.readiness_service import calculate_readiness

app=FastAPI(
    title="AI Release Readiness Dashboard"
)

Base.metadata.create_all(bind=engine)

app.include_router(router)

@app.get('/')
def health_check():
    """
    Health check
    """

    return {
        "status": "running"
    }
