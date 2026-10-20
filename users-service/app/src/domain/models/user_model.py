import datetime
import uuid
from sqlmodel import Field, SQLModel

class User(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    name: str = Field(index=True)
    identification_type: str
    identification_number: str
    birthday_rate: datetime.date

    __tablename__= "usr_users"
