from peewee import CharField
from .base import BaseModel


class Message(BaseModel):
    sender = CharField()
    contents = CharField(max_length=512)
