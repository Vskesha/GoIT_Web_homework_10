from mongoengine import connect, Document, StringField, ListField, ReferenceField, CASCADE

connect(
    db="vs_hw10",
    host="mongodb://localhost:27017"
)


class Author(Document):
    fullname = StringField(required=True, unique=True)
    born_date = StringField(max_length=50)
    born_location = StringField(max_length=150)
    description = StringField()
    meta = {'collection': 'authors'}


class Quote(Document):
    author = ReferenceField(Author, required=True, reverse_delete_rule=CASCADE)
    tags = ListField(StringField(max_length=100))
    quote = StringField(unique=True)
    meta = {'collection': 'quotes'}
