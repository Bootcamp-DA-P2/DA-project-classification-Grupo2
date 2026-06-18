from fastapi import FastAPI, Depends, HTTPException, status
import pandas as pd

from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import declarative_base

from pydantic import BaseModel

import os

def df_to_dict(path):
    try:
        df = pd.read_csv(path)
        if not os.path.exists(path):
            raise FileNotFoundError(f'File {path} not found.')
        return df.to_dict('records')
    except Exception as e:
        raise Exception(f'Error en la trasformación del dataframe a diccionario: {e}')


app = FastAPI(title='Interships Data API')

engine = create_engine('sqlite:///interships_data.db', connect_args={'check_same_thread':False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, engine=engine)
Base = declarative_base()

class IntershipORM(Base):
    __tablename__ = 'interships'
    id = Column(Integer, primary_key=True, nullable=False, index=True)
    cgpa = Column(Float, nullable=False)
    skills_score = Column(Integer, nullable=False)
    projects_count = Column(Integer, nullable=False)
    interships_done = Column(Integer, nullable=False)
    communication_score = Column(Integer, nullable=False)
    aptitude_score = Column(Integer, nullable=False)
    coding_test_score = Column(Integer, nullable=False)
    resume_score = Column(Integer, nullable=False)
    extracurricular = Column(Boolean, nullable=False)
    collegue_tier = Column(String, nullable=False)
    hackatons_participated = Column(Integer, nullable=False)
    certifications_count = Column(Integer, nullable=False)
    linkedin_activity_score = Column(Integer, nullable=False)
    github_score = Column(Integer, nullable=False)
    soft_skills_score = Column(Integer, nullable=False)
    interview_score = Column(Integer, nullable=False)
    consistency_score = Column(Integer, nullable=False)
    backlogs = Column(Integer, nullable=False)
    placement_training = Column(Boolean, nullable=False)
    selected = Column(Integer, nullable=False)

Base.metadata.create_all(engine)

class IntershipsSchema(BaseModel):
    id: int
    cgpa: Float
    skills_score: int
    projects_count: int
    interships_done: int
    communication_score: int
    aptitude_score: int
    coding_test_score: int
    resume_score: int
    extracurricular: bool
    collegue_tier: str
    hackatons_participated: int
    certifications_count: int
    linkedin_activity_score: int
    github_score: int
    soft_skills_score: int
    interview_score: int
    consistency_score: int
    backlogs: int
    placement_training: bool
    selected: int

    class Config:
        from_attributes = True

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Endpoints
@app.get('/interships/')
def get_interships(db: Session = Depends(get_db)):
    interships = db.query(IntershipORM).all()
    if not interships:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='No interships found')
    return interships

@app.post('/interships/')
def create_interships(interships_path = '../data/clean/interships_clean.csv', db: Session = Depends(get_db)):
    try:
        interships = df_to_dict(interships_path)
        for intership in interships:
            try:
                db_intership = IntershipORM(
                    id = intership['id'],
                    cgpa = intership['cpga'],
                    skills_score = intership['skills_score'],
                    projects_count = intership['projects_count'],
                    interships_done = intership['interships_done'],
                    communication_score = intership['communication_score'],
                    aptitude_score = intership['aptitude_score'],
                    coding_test_score = intership['coding_test_score'],
                    resume_score = intership['resume_score'],
                    extracurricular = intership['extracurricular'],
                    collegue_tier = intership['collegue_tier'],
                    hackatons_participated = intership['hackatons_participated'],
                    certifications_count = intership['certifications_count'],
                    linkedin_activity_score = intership['linkedin_activity_score'],
                    github_score = intership['github_score'],
                    soft_skills_score = intership['soft_skills_score'],
                    interview_score = intership['interview_score'],
                    consistency_score = intership['consistency_score'],
                    backlogs = intership['backlogs'],
                    placement_training = intership['placement_training'],
                    selected = intership['selected']
                )
                db.add(db_intership)
            except Exception as e:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
        db.commit()
        return {'message': 'Interships added sucessfully', 'status':status.HTTP_201_CREATED}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
