from fastapi import FastAPI, Depends
from db import engine, Base, get_db
from contextlib import asynccontextmanager
from models import User
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    await engine.dispose()


app = FastAPI(lifespan=lifespan)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/users")
async def list_users(db: AsyncSession = Depends(get_db)):
    stmt = select(User)
    result = await db.execute(stmt)
    return result.scalars().all()
