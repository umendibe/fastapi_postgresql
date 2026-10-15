from pydantic import BaseModel, Field


class CreateParticipant(BaseModel):
    name: str = Field(min_length=2, max_length=80)
    surname: str = Field(min_length=2, max_length=120)
    age: int = Field(gt=0, lt=120)

class ParticipantResponse(BaseModel):
    id: int
    name: str
    surname: str
    age: int
    
class UpdateParticipant(BaseModel):
    name: str = Field(None, min_length=2, max_length=80)
    surname: str = Field(None, min_length=2, max_length=120)
    age: int = Field(None, gt=0, lt=120)
    
