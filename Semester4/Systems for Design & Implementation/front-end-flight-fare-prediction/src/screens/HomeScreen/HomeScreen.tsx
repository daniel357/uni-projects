import type { NextPage } from 'next';
import styles from './HomeScreen.module.scss';
import Link from 'next/link';
import { LuCalendarSearch } from 'react-icons/lu';
import { QueryStats } from '@mui/icons-material';
import React from 'react';

const Home: NextPage = () => {
  return (
    <div className={styles.container}>
      <h1>Welcome to Flight Fare Predictions</h1>
      <p>Discover the optimal time to purchase flight tickets at the best prices.</p>
      <div className={styles.buttons}>
        <Link href="/prediction" legacyBehavior>
          <a>
            <LuCalendarSearch className={styles.icon} />
            <span>Find Best Deals</span>
          </a>
        </Link>
        <Link href="/statistics" legacyBehavior>
          <a>
            <QueryStats className={styles.icon} />
            <span>View Price Trends</span>
          </a>
        </Link>
      </div>
    </div>
  );
};

export default Home;
