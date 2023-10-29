import pydantic
from errors import ApiException


class CreateAdvertisementSchema(pydantic.BaseModel):
    title: str
    description: str
    owner: str
    created_at: str


def validate(data: dict, schema_class):
    try:
        return schema_class(**data).dict()
    except pydantic.ValidationError as er:
        raise ApiException(400, er.errors())