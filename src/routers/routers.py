from fastapi import APIRouter, HTTPException

from schemas import schemas
from services import database

participants_router = APIRouter(prefix="/participants", tags=["PARTICIPANTS"])

@participants_router.get("", status_code=200, response_model=list[schemas.ParticipantResponse])
def get_all_participants():
    return database.get_all_participants()
    
@participants_router.get("/{id}", status_code=200, response_model=schemas.ParticipantResponse)
def get_participant_id(id: int): 
    db_participant = database.get_participant_id(id)
    if not db_participant:
        raise HTTPException(status_code=404, detail="Participant not found")
    return db_participant

@participants_router.post("/post", status_code=201, response_model=schemas.ParticipantResponse)
def post_participant(participant: schemas.CreateParticipant):
    return database.post_participant(participant)
