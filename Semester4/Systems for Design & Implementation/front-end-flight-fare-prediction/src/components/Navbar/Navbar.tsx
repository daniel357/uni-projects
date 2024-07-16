import Link from 'next/link';
import { useRouter } from 'next/router';
import styles from './Navbar.module.scss';
import React from 'react';
import { GiCommercialAirplane } from 'react-icons/gi';
import { RiHome4Line } from 'react-icons/ri';
import {  QueryStats } from '@mui/icons-material';
import { LuCalendarSearch } from "react-icons/lu";

const Navbar: React.FC = () => {
  const router = useRouter();

  return (
    <nav className={styles.navbar}>
      <div className={styles.logo}>
        <Link href="/" legacyBehavior>
          <a className={styles.navLink}>
            <GiCommercialAirplane className={styles.icon} />
            <span>Flight Fare Predictions</span>
          </a>
        </Link>
      </div>
      <div className={styles.links}>
        <Link href="/" legacyBehavior>
          <a className={router.pathname === '/' ? `${styles.navLink} ${styles.active}` : styles.navLink}>
            <RiHome4Line className={styles.icon} />
            <span>Home</span>
          </a>
        </Link>
        {router.pathname !== '/prediction' && (
          <Link href="/prediction" legacyBehavior>
            <a className={router.pathname === '/prediction' ? `${styles.navLink} ${styles.active}` : styles.navLink}>
              <LuCalendarSearch className={styles.icon} />
              <span>Predictions</span>
            </a>
          </Link>
        )}
        {router.pathname !== '/statistics' && (
          <Link href='/statistics' legacyBehavior>
            <a className={router.pathname === '/statistics' ? `${styles.navLink} ${styles.active}` : styles.navLink}>
              <QueryStats className={styles.icon} />
              <span>Statistics</span>
            </a>
          </Link>
        )}
      </div>
    </nav>
  );
};

export default Navbar;
