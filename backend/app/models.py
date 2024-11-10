from sqlalchemy import Column, Integer, String, DateTime, Float
from .database import Base

class GymVisit(Base):
    __tablename__ = "gym_visits"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, index=True)
    gym_id = Column(String, index=True)
    checkin_time = Column(DateTime)
    checkout_time = Column(DateTime)
    workout_type = Column(String)
    calories_burned = Column(Float)

class GymUser(Base):
    __tablename__ = "gym_users"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, index=True)
    first_name = Column(String)
    last_name = Column(String)
    age = Column(Integer)
    gender = Column(String)
    birthdate = Column(DateTime)
    sign_up_date = Column(DateTime)
    user_location = Column(String)
    subscription_plan = Column(String)