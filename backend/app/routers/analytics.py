from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Dict
from datetime import datetime, timedelta
import pandas as pd
from .. import models
from ..database import SessionLocal
from sqlalchemy import text


router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/weekly-visits")
def get_weekly_visits(db: Session = Depends(get_db)):
    query = text("""
    SELECT date_trunc('week', checkin_time) as week,
           COUNT(*) as visits,
           AVG(calories_burned) as avg_calories
    FROM gym_visits
    GROUP BY week
    ORDER BY week DESC
    LIMIT 52
    """)
    result = db.execute(query)

    data = []
    for row in result:
        row_week = row.week.strftime("%m-%d")
        data.append({
            "week": row_week,
            "visits": row.visits,
            "avg_calories": row.avg_calories
        })
    # print("Weekly Visits Data:", data)  
    return data


@router.get("/workout-distribution")
def get_workout_distribution(db: Session = Depends(get_db)):
    """Get distribution of workout types and their average calories"""
    query = text("""
    SELECT workout_type,
           COUNT(*) as count,
           AVG(calories_burned) as avg_calories
    FROM gym_visits
    GROUP BY workout_type
    ORDER BY count DESC
    """)
    result = db.execute(query)
    # for row in result:
    #     print(row) 
    return [{"type": row.workout_type, "count": row.count, "avg_calories": row.avg_calories}
            for row in result]

@router.get("/daily-metrics")
def get_daily_metrics(db: Session = Depends(get_db)):
    """Get key metrics for the dashboard"""
    # Average daily visits
    avg_daily_visits = db.execute(text("""
        SELECT AVG(daily_count)
        FROM (
            SELECT DATE(checkin_time) as visit_date, COUNT(*) as daily_count
            FROM gym_visits
            GROUP BY DATE(checkin_time)
        ) as daily_stats
    """)).scalar()

    # Average calories per session
    avg_calories = db.execute(text("""
        SELECT AVG(calories_burned)
        FROM gym_visits
    """)).scalar()

    # Most popular hour
    popular_hour = db.execute(text("""
        SELECT EXTRACT(HOUR FROM checkin_time) as hour,
               COUNT(*) as visit_count
        FROM gym_visits
        GROUP BY hour
        ORDER BY visit_count DESC
        LIMIT 1
    """)).first()

    # Active users (users with visits in last 30 days)
    active_users = db.execute(text("""
        SELECT COUNT(distinct user_id)
        FROM gym_visits
    """)).scalar()



    return {
        "avg_daily_visits": round(avg_daily_visits) if avg_daily_visits is not None else "N/A",
        "avg_calories_per_session": round(avg_calories) if avg_calories is not None else "N/A",
        "most_popular_hour": f"{popular_hour.hour}:00" if popular_hour is not None else "N/A",
        "active_users": active_users if active_users is not None else "N/A",
    }

@router.get("/user-metrics")
def get_daily_metrics(db: Session = Depends(get_db)):
    """Get user metrics for the second dashboard"""

    categories_count = db.execute(text("""
        SELECT COUNT(distinct user_id)
        FROM gym_visits
    """)).scalar()
                                       

    return {
        "gender": categories_count if categories_count is not None else "N/A",
    }