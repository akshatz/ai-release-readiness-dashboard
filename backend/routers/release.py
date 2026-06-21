"""
Release
"""
from fastapi import APIRouter

from schemas import (
    ReleaseRequest,
    ReleaseResponse
)

from services.readiness_service import (
    calculate_readiness,
    calculate_risk,
    get_blockers,
    get_recommendations
)

router = APIRouter(
    prefix="/release",
    tags=["Release"]
)


@router.post(
    "/readiness",
    response_model=ReleaseResponse
)
def get_readiness(payload: ReleaseRequest):
    """
    Get readiness
    """

    score = calculate_readiness(payload)

    risk = calculate_risk(score)

    blockers = get_blockers(payload)

    recommendations = get_recommendations(blockers)

    status = "READY" if score >= 90 else "NOT READY"

    return {

        "release_name": payload.release_name,

        "score": score,

        "status": status,

        "risk": risk,

        "blockers": blockers,

        "recommendations": recommendations
    }