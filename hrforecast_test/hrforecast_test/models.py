from sqlalchemy import create_engine, Column, Table, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (Integer, String, DateTime)
from datetime import datetime
from sqlalchemy.types import ARRAY
from scrapy.utils.project import get_project_settings



DeclarativeBase = declarative_base()

def db_connect():
    """
    Performs database connection using database settings from settings.py.
    """
    return create_engine(get_project_settings().get("CONNECTION_STRING"))

def create_table(engine):
    DeclarativeBase.metadata.create_all(engine)

class HRForecastJobs(DeclarativeBase):
    __tablename__ = "hrforecast_jobs"
    job_id = Column(Integer(), primary_key=True)
    job_title = Column(String())
    employment_type = Column(String())
    company_name = Column(String())
    crawled_date = Column(DateTime(), default=datetime.now)
    location = Column(String())
    job_url = Column(String())
    ## Uncomment if you want PSQL Arrays instead of tables
    # tasks = Column(ARRAY(String)) 
    # your_profile = Column(ARRAY(String))
    # nice_to_have = Column(ARRAY(String))

class HRForecastTasks(DeclarativeBase):
    __tablename__ = "hrforecast_tasks"
    task_id = Column(Integer(), primary_key=True)
    job_id = Column(Integer(), ForeignKey('hrforecast_jobs.job_id'))
    job_task = Column(String())

class HRForecastProfile(DeclarativeBase):
    __tablename__ = "hrforecast_profile"
    profile_id = Column(Integer(), primary_key=True)
    job_id = Column(Integer(), ForeignKey('hrforecast_jobs.job_id'))
    profile = Column(String())

class HRForecastNiceToHave(DeclarativeBase):
    __tablename__ = "hrforecast_nicetohave"
    nice_id = Column(Integer(), primary_key=True)
    job_id = Column(Integer(), ForeignKey('hrforecast_jobs.job_id'))
    nice = Column(String())

class GazpromJobs(DeclarativeBase):
    __tablename__ = 'gazpom_jobs'
    id = Column(Integer(), primary_key=True)
    job_id = Column(String())
    job_title = Column(String())
    employment_type = Column(String())
    company_name = Column(String())
    location = Column(String())
    region = Column(String())
    posted_date = Column(DateTime())
    crawled_date = Column(DateTime(), default=datetime.now)
    job_url = Column(String())
    ## Uncomment if you want PSQL Arrays instead of tables
    # job_duties = Column(ARRAY(String))
    # job_requirements = Column(ARRAY(String))

class GazpromJobDuties(DeclarativeBase):
    __tablename__ = 'gazpom_duties'
    dutie_id = Column(Integer(), primary_key=True)
    job_id = Column(Integer(), ForeignKey('gazpom_jobs.id'))
    dutie = Column(String())

class GazpromJobRequirements(DeclarativeBase):
    __tablename__ = 'gazpom_requirements'
    requirement_id = Column(Integer(), primary_key=True)
    job_id = Column(Integer(), ForeignKey('gazpom_jobs.id'))
    requirement = Column(String())