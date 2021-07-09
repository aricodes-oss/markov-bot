from .db import db
from .message import Message

db.create_tables([Message])
