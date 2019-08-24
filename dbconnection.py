from sqlalchemy import create_engine

def getEngine():
    return create_engine("sqlite:///sample.db")