from .database import engine, Base
from .models import GymVisit

Base.metadata.create_all(bind=engine)
print("Tablas creadas manualmente.")
