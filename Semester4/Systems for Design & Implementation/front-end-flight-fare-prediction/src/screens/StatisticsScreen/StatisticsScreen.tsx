import React, { useEffect, useState } from 'react';
import { Line } from 'react-chartjs-2';
import 'chart.js/auto';
import Navbar from '../../components/Navbar/Navbar';
import { useHttp } from '../../hooks/useHttp';
import FlightApi from '../../services/api/flightFarePredictions/flightFarePredictions.api';
import styles from './StatisticsScreen.module.scss';

const StatisticsScreen: React.FC = () => {
  const { http } = useHttp({ withLoading: true });

  const [chartData, setChartData] = useState<any>(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const data = await http(() => FlightApi.getStatisticalDataAboutFlightPrices());
        console.log(data);

        const labels = data.map(item => item.flightDate);
        const baseFares = data.map(item => item.baseFare);
        const holidayData = data
          .filter(item => item.isHoliday)
          .map(item => ({ x: item.flightDate, y: item.baseFare }));

        setChartData({
          labels,
          datasets: [
            {
              label: 'Average Flight Fare',
              data: baseFares,
              borderColor: 'white',
              backgroundColor: 'rgba(255, 255, 255, 0.35)',
              fill: true,
              tension: 0.1
            },
            {
              label: 'Holidays',
              data: holidayData,
              backgroundColor: 'blue',
              pointRadius: 8,
              pointBackgroundColor: 'blue',
              type: 'scatter',
              showLine: false
            }
          ]
        });
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
  }, []);

  const chartOptions = {
    scales: {
      x: {
        ticks: {
          color: 'white'
        }
      },
      y: {
        ticks: {
          color: 'white'
        }
      }
    },
    plugins: {
      legend: {
        labels: {
          color: 'white'
        }
      }
    }
  };

  return (
    <div className={styles.pageContainer}>
      <Navbar />
      <div className={styles.container}>
        <h2 className={styles.title}>Average Ticket Prices </h2>
        <p className={styles.description}>
          Visual representation of daily average flight prices and the impact of holidays on fare trends.
        </p>
        {chartData && <Line data={chartData} options={chartOptions} />}
      </div>
    </div>
  );
};

export default StatisticsScreen;
