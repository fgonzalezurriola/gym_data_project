import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { LineChart, Line, BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend } from 'recharts';

function App() {
  const [weeklyData, setWeeklyData] = useState([]);
  const [workoutData, setWorkoutData] = useState([]);
  const [metrics, setMetrics] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const [weeklyResponse, workoutResponse, metricsResponse] = await Promise.all([
          axios.get('http://localhost:8000/api/analytics/weekly-visits'),
          axios.get('http://localhost:8000/api/analytics/workout-distribution'),
          axios.get('http://localhost:8000/api/analytics/daily-metrics')
        ]);

        setWeeklyData(weeklyResponse.data);
        setWorkoutData(workoutResponse.data);
        setMetrics(metricsResponse.data);
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
        <div className="text-xl">Loading...</div>
      </div>
    );
  }

  return (
    <div className="p-6 max-w-7xl mx-auto">
      <h1 className="text-3xl font-bold mb-8">Gym Analytics Dashboard</h1>
      
      {/* Metrics Cards */}
      <div className="grid grid-cols-1 md:grid-cols-4 gap-4 mb-8">
        <div className="bg-white p-4 rounded-lg shadow">
          <h3 className="text-gray-500 text-sm">Avg. Daily Visits</h3>
          <p className="text-2xl font-bold">{metrics?.avg_daily_visits}</p>
        </div>
        <div className="bg-white p-4 rounded-lg shadow">
          <h3 className="text-gray-500 text-sm">Avg. Calories/Session</h3>
          <p className="text-2xl font-bold">{metrics?.avg_calories_per_session}</p>
        </div>
        <div className="bg-white p-4 rounded-lg shadow">
          <h3 className="text-gray-500 text-sm">Popular Hour</h3>
          <p className="text-2xl font-bold">{metrics?.most_popular_hour}</p>
        </div>
        <div className="bg-white p-4 rounded-lg shadow">
          <h3 className="text-gray-500 text-sm">Active Users</h3>
          <p className="text-2xl font-bold">{metrics?.active_users}</p>
        </div>
      </div>

      {/* Charts */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
        <div className="bg-white p-6 rounded-lg shadow">
          <h2 className="text-xl font-semibold mb-4">Weekly Visits Trend</h2>
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

        <div className="bg-white p-6 rounded-lg shadow">
          <h2 className="text-xl font-semibold mb-4">Workout Distribution</h2>
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
    </div>
  );
}

export default App;