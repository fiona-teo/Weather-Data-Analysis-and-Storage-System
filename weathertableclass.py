import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#create the engine
db_url = 'sqlite:///weathertable.db'
engine = create_engine(db_url)

#create the session
Session = sessionmaker(bind=engine)
session = Session()

#define the base class
Base = sqlalchemy.orm.declarative_base()

#C4. Created another class that generates a table in SQLite by using SQLAlchemy ORM module
class WeatherTable(Base):
    __tablename__ = 'Weather_Information'
    primary_key = Column(Integer, primary_key=True)
    latitude = Column(Float)
    longitude = Column(Float)
    year = Column(Integer)
    month = Column(Integer)
    day = Column(Integer)
    five_yr_avg_temp = Column(Float)
    five_yr_min_temp = Column(Float)
    five_yr_max_temp = Column(Float)
    five_yr_avg_wind_speed = Column(Float)
    five_yr_min_wind_speed = Column(Float)
    five_yr_max_wind_speed = Column(Float)
    five_yr_sum_precipitation = Column(Float)
    five_yr_min_precipitation = Column(Float)
    five_yr_max_precipitation = Column(Float)

#creating the table after I declared it
Base.metadata.create_all(engine)



