from pydantic import BaseModel, Field
from bson import ObjectId
from typing import Optional


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")


class ChildInfo(BaseModel):
	name: Optional[str] = None
	address: str
	contact_email: str
	contact_mobile: str

class ChildModel(BaseModel):
	id: PyObjectId = Field(default_factory=PyObjectId, alias='_id')
	info: ChildInfo = Field(...)
	type: str = Field(...)

	class Config:
		allow_population_by_field_name = True
		arbitrary_types_allowed = True
		json_encoders = {ObjectId: str}
