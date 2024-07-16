import type { NextPage } from 'next';
import styles from './PredictionScreen.module.scss';
import Navbar from '../../components/Navbar/Navbar';
import PredictionForm from '../../components/PredictionForm/PredictionForm';

const Predictions: NextPage = () => {
  return (
    <div className={styles.pageContainer}>
      <Navbar />
      <div className={styles.container}>
        <div className={`${styles.airportLabel} ${styles.startingAirport}`}>
          CHICAGO
        </div>
        <div className={styles.curvedLine}></div>
        <div className={`${styles.airportLabel} ${styles.destinationAirport}`}>
          LOS ANGELES
        </div>
        <div className={styles.predictionFormContainer}>
          <h1>Discover The Best Flight Deals</h1>
        <PredictionForm />
        </div>
      </div>
    </div>
  );
};

export default Predictions;
