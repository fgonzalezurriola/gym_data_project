import React, { useState, useEffect, Component } from 'react';
import axios from 'axios';
import { LineChart, Line, BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend } from 'recharts';
import Footer from './components/Footer';

function App() {
  const [weeklyData, setWeeklyData] = useState([]);
  const [workoutData, setWorkoutData] = useState([]);
  const [metrics, setMetrics] = useState(null);
  const [userData, setUserData] = useState({});
  const [loading, setLoading] = useState(true);

  // console.log('Weekly Data:', weeklyData);
  // console.log('Workout Data:', workoutData);
  // console.log('Metrics:', metrics);
  console.log('User Data:', userData);

  // useEffect(() => {
  //   const fetchData = async () => {
  //     try {
  //       const [weeklyResponse, workoutResponse, metricsResponse, userResponse] = await Promise.all([
  //         axios.get('http://localhost:8000/api/analytics/weekly-visits'),
  //         axios.get('http://localhost:8000/api/analytics/workout-distribution'),
  //         axios.get('http://localhost:8000/api/analytics/daily-metrics'),
  //         axios.get('http://localhost:8000/api/analytics/users-metrics'),
  //       ]);

  //       setWeeklyData(weeklyResponse.data);
  //       setWorkoutData(workoutResponse.data);
  //       setMetrics(metricsResponse.data);
  //       setUserData(userResponse.data);
  //     } catch (error) {
  //       console.error('Error fetching data:', error);
  //     } finally {
  //       setLoading(false);
  //     }
  //   };

  useEffect(() => {
    const fetchData = async () => {
      try {
        const baseURL = process.env.REACT_APP_API_BASE_URL || 'http://localhost:8000';
        
        const [weeklyResponse, workoutResponse, metricsResponse, userResponse] = await Promise.all([
          axios.get(`${baseURL}/api/analytics/weekly-visits`),
          axios.get(`${baseURL}/api/analytics/workout-distribution`),
          axios.get(`${baseURL}/api/analytics/daily-metrics`),
          axios.get(`${baseURL}/api/analytics/users-metrics`),
        ]);
  
        setWeeklyData(weeklyResponse.data);
        setWorkoutData(workoutResponse.data);
        setMetrics(metricsResponse.data);
        setUserData(userResponse.data);
      } catch (error) {
        console.error('Error fetching data:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  if (loading) {
    return (
      <div className="flex items-center justify-center min-h-screen">
        <div className="text-3xl">Loading...</div>
      </div>
    );
  }

  return (
    <div className="p-6 max-w-7xl mx-auto">
      <h1 className="text-4xl font-bold mb-8 mt-4 ml-2"> Analíticas de Gimnasios Dashboard</h1>
      
      {/* Metrics Cards */}
      <div className="grid grid-cols-1 md:grid-cols-4 gap-4 mb-8">
        <div className="bg-white p-4 rounded-lg shadow">
          <h3 className="text-gray-500 text-sm">Promedio de visitas diarias</h3>
          <p className="text-2xl font-bold">{metrics?.avg_daily_visits}</p>
        </div>
        <div className="bg-white p-4 rounded-lg shadow">
          <h3 className="text-gray-500 text-sm">Promedio de calorías por sesión</h3>
          <p className="text-2xl font-bold">{metrics?.avg_calories_per_session}</p>
        </div>
        <div className="bg-white p-4 rounded-lg shadow">
          <h3 className="text-gray-500 text-sm">Hora más Popular</h3>
          <p className="text-2xl font-bold">{metrics?.most_popular_hour}</p>
        </div>
        <div className="bg-white p-4 rounded-lg shadow">
          <h3 className="text-gray-500 text-sm">Usuarios Activos</h3>
          <p className="text-2xl font-bold">{metrics?.active_users}</p>
        </div>
      </div>

      {/* Charts */}
      <div className="flex flex-wrap w-full mx-auto items-center">
        <div className="bg-white h-[350px] p-2 rounded md:rounded-l-lg  shadow">
          <h2 className="text-xl font-semibold ml-2.5 mb-4">Visitas semanales</h2>
          <LineChart width={600} height={300} data={weeklyData}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="week" />
            <YAxis />
            <Tooltip />
            <Legend />
            <Line type="monotone" dataKey="visits" stroke="#8884d8" />
            <Line type="monotone" dataKey="avg_calories" stroke="#82ca9d" />
          </LineChart>
        </div>

        <div className="bg-white h-[350px] p-2 rounded md:rounded-r-lg shadow">
          <h2 className="text-xl font-semibold ml-2 mb-4">Categoría de ejercicio y cantidad de calorías quemadas</h2>
          <BarChart width={600} height={300} data={workoutData}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="type" />
            <YAxis />
            <Tooltip />
            <Legend />
            <Bar dataKey="count" fill="#8884d8" />
            <Bar dataKey="avg_calories" fill="#82ca9d" />
          </BarChart>
        </div>
      </div>

      {/* User Metrics */}
      <div className="p-4 rounded-lg shadow bg-white mb-8 mt-8">
        <h2 className="text-xl font-semibold mb-4">Conteo de Usuarios por Género</h2>
        <p>Hombre: <strong>{userData.gender_counts?.['Male'] || 0}</strong></p>
        <p>Mujer: <strong>{userData.gender_counts?.['Female'] || 0}</strong></p>
        <p>No-Binario: <strong>{userData.gender_counts?.['Non-binary'] || 0}</strong></p>
      </div>
      <Footer />

    </div>

  );
}

export default App;