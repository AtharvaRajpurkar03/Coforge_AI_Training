from config.database import engine,SessionLocal,Base
from config.logger import logger
from schemas.trainingfeedback_schema import FeedbackCreate,FeedbackResponse,FeedbackUpdate
from services import trainingfeedback_service as service
from sqlalchemy.exc import IntegrityError
from fastapi import FastAPI, HTTPException

app=FastAPI(
    title="Training Feedback API",
    version="1.0.0"
)

Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {
        "message":"Corporate Training Feedback API "
    }

@app.post("/feedbacks",response_model=FeedbackResponse,status_code=201)
def create_feedback(feedback:FeedbackCreate):
    db=SessionLocal()

    try:
        new_feedback=service.create_feedback(db,feedback)
        logger.info(f"Feedback Created {new_feedback.feedback_id}")
        return new_feedback

    except IntegrityError:
        db.rollback()
        logger.warning("Duplicate Feedback ID")
        raise HTTPException(status_code=409,detail="Feedback ID already exists")

    except Exception:
        logger.exception("Create Error")
        raise HTTPException(status_code=500,detail="Internal Server Error")

    finally:
        db.close()

@app.get("/feedbacks",response_model=list[FeedbackResponse])
def get_all_feedbacks(skip:int=0,limit:int=10):
    db=SessionLocal()

    return service.get_all_feedback(db,skip,limit)

@app.get("/feedbacks/{feedback_id}",response_model=FeedbackResponse)
def get_feedbacks_by_id(feedback_id:int):
    db=SessionLocal()

    feedback=service.feedback_by_id(db,feedback_id)

    if not feedback:
        logger.warning(f"Feedback ID {feedback_id} not found")
        raise HTTPException(status_code=404,detail="Feedback not found")

    return feedback

@app.put("/feedbacks/{feedback_id}",response_model=FeedbackResponse)
def update_feedback(feedback_id:int, data:FeedbackUpdate):
    db=SessionLocal()

    try:
        feedback=service.update_feedback(db,feedback_id,data)

        if not feedback:
            logger.warning(f"Feedback {feedback_id} not found")
            raise HTTPException(status_code=404,detail="Feedback not found")

        logger.info(f"Feedback {feedback_id} updated")

        return feedback

    except HTTPException:
        raise

    except Exception:
        logger.exception("Update Error")
        raise HTTPException(status_code=500,detail="Internal Server Error")

    finally:
        db.close()

@app.delete("/feedbacks/{feedback_id}")
def delete_feedback(feedback_id:int):
    db=SessionLocal()

    feedback=service.delete_feedback(db,feedback_id)

    if not feedback:
        logger.warning(f"Feedback {feedback_id} not found")
        raise HTTPException(status_code=404,detail="Feedback not found")

    logger.info(f"Feedback {feedback_id} deleted")
    return {
        "message":"Feedback deleted successfully"
    }

@app.get("/trainer/{trainer_name}",response_model=list[FeedbackResponse])
def trainer_feedbacks(trainer_name:str):
    db=SessionLocal()

    return service.trainer_feedback(db,trainer_name)

@app.get("/course/{course_name}",response_model=list[FeedbackResponse])
def course_feedbacks(course_name:str):
    db=SessionLocal()

    return service.course_feedback(db,course_name)

@app.get("/average-trainer-rating")
def average_rating():
    db=SessionLocal()

    data=service.average_trainer_rating(db)

    return [
        {
            "trainer_name":trainer,
            "average_rating": round(avg,2)
        }
        for trainer,avg in data
    ]

@app.get("/low-rated-sessions")
def low_ratings():
    db=SessionLocal()

    return service.low_rated_sessions(db)

@app.get("/recommendation-percentage/{course_name}")
def recommendation_percentage(course_name:str):
    db=SessionLocal()

    return service.recommendation_percentage(db,course_name)










