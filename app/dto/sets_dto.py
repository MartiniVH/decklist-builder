from pydantic import BaseModel


class SetDTO(BaseModel):
    id: int
    name: str
    name_shorthand: str
    release_date: str
