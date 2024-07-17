from .connect import connect
from mongoengine import Document, StringField, DateTimeField, BooleanField, IntField
from datetime import datetime

class User(Document):
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)
    language = StringField(max_length=2)
    chat_id = IntField()
    created_at = DateTimeField(default=datetime.now)
    is_active = BooleanField(default=True)