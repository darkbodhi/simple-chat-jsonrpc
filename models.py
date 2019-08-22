import mongoengine


class Dialogue(Document):
    type = StringField(max_length=50)
    last_message = StringField()
    last_message_date = ()


class UserDialogue(Document):
    dialogue_id = StringField()
    user_id = StringField()
    type = StringField(max_length=50)
    last_message = StringField()
    last_message_date = ()


class Message(Document):
    dialogue_id = StringField()
    user_id = StringField()
    message = ()
    date = ()
