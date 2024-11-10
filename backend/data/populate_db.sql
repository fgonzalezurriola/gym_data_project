\COPY gym_users(user_id, first_name, last_name, age, gender, birthdate, sign_up_date, user_location, subscription_plan) FROM 'C:/Users/fgonz/Escritorio/gym_data_project/backend/data/users_data.csv' DELIMITER ',' CSV HEADER;

\COPY gym_visits(user_id, gym_id, checkin_time, checkout_time, workout_type, calories_burned) FROM 'C:/Users/fgonz/Escritorio/gym_data_project/backend/data/checkin_checkout_history_updated.csv' DELIMITER ',' CSV HEADER;

-- ### Comando para Popular la Base de Datos

-- Para cargar los datos en la base de datos de PostgreSQL, se utilizó el siguiente comando:

-- ```bash
-- psql -h <host> -U <usuario> -d <nombre_de_base_de_datos> -f <ruta_del_archivo_sql>