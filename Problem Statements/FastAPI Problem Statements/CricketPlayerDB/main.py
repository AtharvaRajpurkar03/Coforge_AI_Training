from fastapi import FastAPI, HTTPException
from sqlalchemy.exc import IntegrityError
from services import cricketplayer_service as service
from schemas.cricketplayer_schema import CricketPlayerCreate,CricketPlayerUpdate,CricketPlayerResponse
from config.logger import logger
from config.database import engine,SessionLocal,Base

app=FastAPI(
    title="Cricket Player Statistics API",
    version="1.0.0"
)

Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {
        "message":"Welcome to Cricket Player Statistics API"
    }

@app.post("/players",response_model=CricketPlayerResponse,status_code=201)
def create_player(player:CricketPlayerCreate):
    db=SessionLocal()

    try:
        new_player=service.create_player(db,player)
        logger.info(f"Player created {new_player.player_id}")
        return new_player
    
    except IntegrityError:
        db.rollback()
        logger.warning("Duplicate player id")
        raise HTTPException(status_code=409,detail="Player Id already exists")

    except Exception:
        logger.exception("Unexpected Create Error")
        raise HTTPException(status_code=500,detail="Internal Server Error")

    finally:
        db.close()

@app.get("/players",response_model=list[CricketPlayerResponse])
def get_players(skip:int=0,limit:int=10):
    db=SessionLocal()

    return service.get_all_players(db,skip,limit)

@app.get("/players/{player_id}",response_model=CricketPlayerResponse)
def get_player(player_id:int):
    db=SessionLocal()

    player=service.get_player_by_id(db,player_id)

    if not player:
        logger.warning("Player {player_id} not found")
        raise HTTPException(status_code=404,detail="Player not found")

    return player

@app.put("/players/{player_id}",response_model=CricketPlayerResponse)
def update_player(player_id:int,data:CricketPlayerUpdate):
    db=SessionLocal()

    try:
        player=service.update_player(db,player_id,data)

        if not player:
            logger.warning("Player {player_id} not found")
            raise HTTPException(status_code=404,detail="Player not found")

        logger.info(f"Player Updated {player_id}")
        return player

    except HTTPException:
        raise

    except IntegrityError:
        db.rollback()
        raise

    except Exception:
        logger.exception("Update Error")
        raise HTTPException(status_code=500,detail="Internal Server Error")

    finally:
        db.close()

@app.delete("/players/{player_id}")
def delete_player(player_id:int):
    db=SessionLocal()

    player=service.delete_player(db,player_id)

    if not player:
        logger.warning("Player {player_id} not found")
        raise HTTPException(status_code=404,detail="Player not found")

    logger.info(f"Player deleted {player_id}")
    return {
        "message":"Player deleted successfully"
    }

@app.get("/team/{team_name}")
def team_players(team_name:str):
    db=SessionLocal()

    return service.filter_team(db,team_name)

@app.get("/all-rounders")
def get_all_rounders():
    db=SessionLocal()

    return service.all_rounders(db)

@app.get("/top-scorers")
def get_top_scorers():
    db=SessionLocal()

    return service.top_run_scorers(db)

@app.get("/strike-rates")
def get_strike_rates():
    db=SessionLocal()

    return service.strike_rates(db)

@app.get("/team-statistics")
def team_stats():
    db=SessionLocal()

    data=service.team_statistics(db)

    return [
        {
            "team_name": team,
            "total_runs": runs,
            "total_wickets": wickets
        }
        for team, runs, wickets in data
    ]





    
