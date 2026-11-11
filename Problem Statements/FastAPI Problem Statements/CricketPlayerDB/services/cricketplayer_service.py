from sqlalchemy.orm import Session
from sqlalchemy import select,func
from models.cricketplayer_model import CricketPlayer

def create_player(db:Session,data):
    player=CricketPlayer(**data.model_dump())

    db.add(player)
    db.commit()
    db.refresh(player)
    return player

def get_all_players(db:Session,skip:int,limit:int):
    query=select(CricketPlayer).offset(skip).limit(limit)
    result=db.scalars(query)
    return result.all()

def get_player_by_id(db:Session,player_id:int):
    return db.get(CricketPlayer,player_id)

def update_player(db:Session,player_id:int,data):
    player=db.get(CricketPlayer,player_id)

    if player is None:
        return None

    for key,value in data.model_dump().items():
        setattr(player,key,value)

    db.commit()
    db.refresh(player)
    return player

def delete_player(db:Session,player_id:int):
    player=db.get(CricketPlayer,player_id)

    if player is None:
        return None

    db.delete(player)
    db.commit()
    return True

def filter_team(db:Session,team_name:str):
    query=select(CricketPlayer).where(CricketPlayer.team_name==team_name)
    result=db.scalars(query)
    return result.all()

def all_rounders(db:Session):
    query=(select(CricketPlayer).where(CricketPlayer.role=="All-Rounder").where(CricketPlayer.wickets_taken>=10))
    result=db.scalars(query)
    return result.all()

def top_run_scorers(db:Session):
    query=(select(CricketPlayer).order_by(CricketPlayer.total_runs.desc()).limit(5))
    result=db.scalars(query)
    return result.all()

def strike_rates(db:Session):
    query=select(CricketPlayer)
    result=db.scalars(query)
    players=result.all()

    players_result=[]

    for player in players:
        if player.balls_faced==0:
            strike_rate=0
        else:
            strike_rate=round(
                (player.total_runs/player.balls_faced)*100,2
            )

        players_result.append(
            {
                "player_id":player.player_id,
                "player_name":player.player_name,
                "strike_rate":strike_rate
            }
        )

    return players_result

def team_statistics(db:Session):
    query=(select(CricketPlayer.team_name,func.sum(CricketPlayer.total_runs).label("total_runs"),func.sum(CricketPlayer.wickets_taken).label("total_wickets")).group_by(CricketPlayer.team_name))
    result=db.execute(query)
    return result.all()





