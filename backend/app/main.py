from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import analytics
from .database import engine
from . import models
import pandas as pd
from .database import SessionLocal
from .models import GymVisit, GymUser 
from .config import CORS_ORIGINS
import uvicorn
import os

app = FastAPI(title="Analíticas de Gimnasios")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ORIGINS,
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
    #print("Cargando datos de visitas...")
    df_visits = pd.read_csv("data/checkin_checkout_history_updated.csv")
    print(f"Total de filas en df_visits: {len(df_visits)}")
    db = SessionLocal()
    
    for i, row in df_visits.iterrows():
        #print(f"Insertando visita {i + 1}/{len(df_visits)}: usuario {row['user_id']}")
        visit = GymVisit(
            user_id=row['user_id'],
            gym_id=row['gym_id'],
            checkin_time=pd.to_datetime(row['checkin_time']),
            checkout_time=pd.to_datetime(row['checkout_time']),
            workout_type=row['workout_type'],
            calories_burned=row['calories_burned']
        )
        db.add(visit)

    #print("Cargando datos de usuarios...")
    df_users = pd.read_csv("data/users_data.csv")
    print(f"Total de filas en df_users: {len(df_users)}")
    for i, row in df_users.iterrows():
        #print(f"Insertando usuario {i + 1}/{len(df_users)}: {row['user_id']}")
        user = GymUser(
            user_id=row['user_id'], 
            first_name=row['first_name'],
            last_name=row['last_name'],
            age=row['age'],
            gender=row['gender'],
            birthdate=pd.to_datetime(row['birthdate']),
            sign_up_date=pd.to_datetime(row['sign_up_date']),
            user_location=row['user_location'],
            subscription_plan=row['subscription_plan']
        )
        db.add(user)

    db.commit()
    db.close()
    #print("Carga de datos completada.")

# Populate DB
print("Ejecutando el poblamiento de la base de datos...")
load_initial_data()

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)