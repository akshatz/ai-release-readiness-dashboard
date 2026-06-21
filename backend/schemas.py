"""
Schemas Used in the app
"""
from pydantic import BaseModel


class ReleaseRequest(BaseModel):

    release_name: str

    development_complete: bool

    pr_merged: bool

    staging_deployed: bool

    qa_complete: bool

    release_notes_created: bool

    production_approval: bool


class ReleaseResponse(BaseModel):

    release_name: str

    score: int

    status: str

    risk: str

    blockers: list[str]

    recommendations: list[str]
