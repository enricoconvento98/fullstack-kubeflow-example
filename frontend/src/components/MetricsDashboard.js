import React, { useEffect, useState } from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend } from 'recharts';

const MetricsDashboard = ({ runId }) => {
  const [metrics, setMetrics] = useState([]);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    const fetchMetrics = async () => {
      try {
        const response = await fetch(`http://localhost:8000/metrics/${runId}`);
        const data = await response.json();
        setMetrics(data);
      } catch (error) {
        console.error("Error fetching metrics:", error);
      } finally {
        setIsLoading(false);
      }
    };

    fetchMetrics();
  }, [runId]);

  if (isLoading) return <div>Loading...</div>;

  // Transform data for Recharts
  const chartData = metrics.reduce((acc, metric) => {
    const existingPoint = acc.find(point => 
      new Date(point.timestamp).getTime() === new Date(metric.timestamp).getTime()
    );
    
    if (existingPoint) {
      existingPoint[metric.metric_name] = metric.metric_value;
    } else {
      acc.push({
        timestamp: metric.timestamp,
        [metric.metric_name]: metric.metric_value
      });
    }
    
    return acc;
  }, []);

  return (
    <div>
      <h2>Metrics for Run: {runId}</h2>
      <LineChart width={800} height={400} data={chartData}>
        <CartesianGrid strokeDasharray="3 3" />
        <XAxis dataKey="timestamp" />
        <YAxis />
        <Tooltip />
        <Legend />
        <Line type="monotone" dataKey="accuracy" stroke="#8884d8" />
        <Line type="monotone" dataKey="precision" stroke="#82ca9d" />
        <Line type="monotone" dataKey="recall" stroke="#ffc658" />
        <Line type="monotone" dataKey="f1" stroke="#ff7300" />
      </LineChart>
    </div>
  );
};

export default MetricsDashboard;