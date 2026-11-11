from models.trainingfeedback_model import TrainingFeedback
from sqlalchemy.orm import Session
from sqlalchemy import select,func

def create_feedback(db:Session,data):
    feedback=TrainingFeedback(**data.model_dump())

    db.add(feedback)
    db.commit()
    db.refresh(feedback)
    return feedback

def get_all_feedback(db:Session,skip:int,limit:int):
    query=select(TrainingFeedback).offset(skip).limit(limit)
    result=db.scalars(query)
    return result.all()

def feedback_by_id(db:Session,feedback_id:int):
    return db.get(TrainingFeedback, feedback_id)

def update_feedback(db:Session,feedback_id:int,data):
    feedback=db.get(TrainingFeedback,feedback_id)

    if feedback is None:
        return None

    for key,value in data.model_dump().items():
        setattr(feedback,key,value)

    db.commit()
    db.refresh(feedback)
    return feedback

def delete_feedback(db:Session,feedback_id:int):
    feedback=db.get(TrainingFeedback,feedback_id)

    if feedback is None:
        return False

    db.delete(feedback)
    db.commit()
    return True

def trainer_feedback(db:Session,trainer_name:str):
    query=select(TrainingFeedback).where(TrainingFeedback.trainer_name==trainer_name)
    result=db.scalars(query)
    return result.all()

def course_feedback(db:Session,course_name:str):
    query=select(TrainingFeedback).where(TrainingFeedback.course_name==course_name)
    result=db.scalars(query)
    return result.all()

def average_trainer_rating(db:Session):
    query=select(TrainingFeedback.trainer_name,func.avg(TrainingFeedback.trainer_rating).label("average_trainer_rating")).group_by(TrainingFeedback.trainer_name)
    result=db.execute(query)
    return result.all()

def low_rated_sessions(db:Session):
    query=select(TrainingFeedback).where(TrainingFeedback.trainer_rating<=2).where(TrainingFeedback.content_rating<=2).where(TrainingFeedback.hands_on_rating<=2)
    result=db.scalars(query)
    return result.all()

def recommendation_percentage(db:Session,course_name:str):
    query=select(TrainingFeedback).where(TrainingFeedback.course_name==course_name)
    result=db.scalars(query)
    feedbacks=result.all()

    total=len(feedbacks)

    if total==0:
        return {
            "course_name":course_name,
            "recommendation_percentage":0
        }

    recommended=0
    for feedback in feedbacks:
        if feedback.would_recommend==True:
            recommended+=1

    percentage=round((recommended/total)*100, 2)
    
    return {
        "course_name":course_name,
        "recommendation_percentage":percentage
    }








