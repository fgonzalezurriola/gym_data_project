from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import analytics
from .database import engine
from . import models
import pandas as pd
from .database import SessionLocal
from .models import GymVisit, UserData 

app = FastAPI(title="Analíticas de Gimnasios")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create database tables
models.Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(analytics.router, prefix="/api/analytics", tags=["analytics"])

# Load data function
def load_initial_data():
    # Load gym visit data
    df_visits = pd.read_csv("data/checkin_checkout_history_updated.csv")
    db = SessionLocal()
    
    for _, row in df_visits.iterrows():
        visit = GymVisit(
            user_id=row['user_id'],
            gym_id=row['gym_id'],
            checkin_time=pd.to_datetime(row['checkin_time']),
            checkout_time=pd.to_datetime(row['checkout_time']),
            workout_type=row['workout_type'],
            calories_burned=row['calories_burned']
        )
        db.add(visit)

    # Load user data
    df_users = pd.read_csv("data/user_data.csv")
    for _, row in df_users.iterrows():
        user = UserData(
            user_id=row['id'], 
            first_name=row['name'],
            last_name=row['last_name'],
            age=row['age'],
            gender=row['gender'],
            birthdate=pd.to_datetime(row['birthdate']),
            sign_up_date=pd.to_datetime(row['sign_up_date']),
            user_location=row['location'],
            subscription_plan=row['subscription_plan']
        )
        db.add(user)

    db.commit()
    db.close()

if __name__ == "__main__":
    load_initial_data()