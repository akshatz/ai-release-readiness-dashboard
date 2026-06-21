"""
Models
"""


from sqlalchemy import Column,Integer,String,Boolean

from database import Base

class Release(Base):

    __tablename__="releases"

    id=Column(Integer,primary_key=True)

    name=Column(String)

    version=Column(String)

    development_complete=Column(Boolean)

    qa_complete=Column(Boolean)

    staging_complete=Column(Boolean)

    approval_complete=Column(Boolean)
