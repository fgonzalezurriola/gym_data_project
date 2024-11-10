\COPY gym_users(user_id, first_name, last_name, age, gender, birthdate, sign_up_date, user_location, subscription_plan) FROM 'C:/Users/fgonz/Escritorio/gym_data_project/backend/data/users_data.csv' DELIMITER ',' CSV HEADER;

\COPY gym_visits(user_id, gym_id, checkin_time, checkout_time, workout_type, calories_burned) FROM 'C:/Users/fgonz/Escritorio/gym_data_project/backend/data/checkin_checkout_history_updated.csv' DELIMITER ',' CSV HEADER;
