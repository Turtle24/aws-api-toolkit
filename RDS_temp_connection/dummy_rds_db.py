from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from settings import USERNAME, DATABASE_PASSWORD, CONNECTION, DATABASE
from fastapi import HTTPException, status
import asyncio
import aiomysql

SQLALCHEMY_DATABASE_URL = f'mysql+pymysql://{USERNAME}:{DATABASE_PASSWORD}@{CONNECTION}/{DATABASE}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()

async def get_db():
    """Database connection used for db: Sessions. Creates a cursor to execute
    queries, cursors are added to the event pool,
    yielded to use for execution and then the queries are commited to the database. 

    Raises:
        HTTPException: If the connection to the database fails then the exception is raised.

    Yields:
        DictCursor: That allows the connection to be queried.
    """
    # loop = asyncio.get_event_loop()
    async with aiomysql.connect(host=f'{CONNECTION}', port=3306,
                                user=f'{USERNAME}', password=f'{DATABASE_PASSWORD}',
                                db=f"{DATABASE}", autocommit=False) as conn:
        cursor = await conn.cursor(aiomysql.DictCursor) 
        if not cursor:
            raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=f"Could not connect to the database")
        yield cursor
        await conn.commit()
