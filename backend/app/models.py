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