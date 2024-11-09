from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import analytics
from .database import engine
from . import models
import uvicorn

app = FastAPI(title="Gym Analytics API")

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

# Script para cargar datos iniciales
def load_initial_data():
    import pandas as pd
    from .database import SessionLocal
    from .models import GymVisit
    
    df = pd.read_csv("data/checkin_checkout_history_updated.csv")
    db = SessionLocal()
    
    for _, row in df.iterrows():
        visit = GymVisit(
            user_id=row['user_id'],
            gym_id=row['gym_id'],
            checkin_time=pd.to_datetime(row['checkin_time']),
            checkout_time=pd.to_datetime(row['checkout_time']),
            workout_type=row['workout_type'],
            calories_burned=row['calories_burned']
        )
        db.add(visit)
    
    db.commit()
    db.close()

if __name__ == "__main__":
    load_initial_data()