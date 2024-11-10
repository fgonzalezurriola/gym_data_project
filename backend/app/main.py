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
    try:
        print("Verificando si la base de datos ya tiene datos...")
        db = SessionLocal()
        # Verificar si ya hay datos
        existing_users = db.query(GymUser).first()
        if existing_users:
            print("La base de datos ya contiene datos. Saltando la población inicial.")
            db.close()
            return

        print("Comenzando la carga de datos...")
        print(f"Directorio actual: {os.getcwd()}")
        
        try:
            df_visits = pd.read_csv("data/checkin_checkout_history_updated.csv")
            print(f"Archivo de visitas cargado. Total de filas: {len(df_visits)}")
        except Exception as e:
            print(f"Error al cargar archivo de visitas: {e}")
            return
        
        for i, row in df_visits.iterrows():
            try:
                visit = GymVisit(
                    user_id=row['user_id'],
                    gym_id=row['gym_id'],
                    checkin_time=pd.to_datetime(row['checkin_time']),
                    checkout_time=pd.to_datetime(row['checkout_time']),
                    workout_type=row['workout_type'],
                    calories_burned=row['calories_burned']
                )
                db.add(visit)
                if i % 100 == 0:  # Log cada 100 registros
                    print(f"Procesados {i} registros de visitas")
            except Exception as e:
                print(f"Error al procesar visita {i}: {e}")
                continue

        try:
            df_users = pd.read_csv("data/users_data.csv")
            print(f"Archivo de usuarios cargado. Total de filas: {len(df_users)}")
        except Exception as e:
            print(f"Error al cargar archivo de usuarios: {e}")
            return

        for i, row in df_users.iterrows():
            try:
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
                if i % 100 == 0:  # Log cada 100 registros
                    print(f"Procesados {i} registros de usuarios")
            except Exception as e:
                print(f"Error al procesar usuario {i}: {e}")
                continue

        db.commit()
        print("Carga de datos completada exitosamente.")
    except Exception as e:
        print(f"Error general durante la carga de datos: {e}")
    finally:
        db.close()

@app.on_event("startup")
async def startup_event():
    print("Forzando población de la base de datos...")
    load_initial_data()

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)