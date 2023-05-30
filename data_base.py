from peewee import *

db = SqliteDatabase("database.sqlite")


class BaseModel(Model):
    class Meta:
        database = db


class Employees(BaseModel):
    id = AutoField(primary_key=True, unique=True)
    name = CharField()
    position = CharField()
    department = CharField()

    def __str__(self):
        return f"{self.name} ({self.department[:20]})"


class Destinations(BaseModel):
    id = AutoField(primary_key=True, unique=True)
    destination = CharField()
    employee_position = CharField()
    employee = CharField()


def create_db():
    db.create_tables([Employees, Destinations])

