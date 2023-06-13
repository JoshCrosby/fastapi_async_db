from db import db, metadata, sqlalchemy

users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("first_name", sqlalchemy.String),
    sqlalchemy.Column("last_name", sqlalchemy.String),
    sqlalchemy.Column("age", sqlalchemy.Integer),
)


class User:
    @classmethod
    async def get(cls, id):
        query = users.select().where(users.c.id == id)
        return await db.fetch_one(query)

    @classmethod
    async def create(cls, **user):
        query = users.insert().values(**user)
        return await db.execute(query)
