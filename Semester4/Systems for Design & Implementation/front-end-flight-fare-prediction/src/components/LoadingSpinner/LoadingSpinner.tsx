import { CircularProgress, Typography } from '@mui/material';
import { useSelector } from 'react-redux';
import { RootState } from '@redux/reducers';

import styles from './LoadingSpinner.module.scss';

const LoadingSpinner = () => {
  const { isLoading } = useSelector((state: RootState) => state.ui);

  return (
    <>
      {isLoading && (
        <div className={styles.container}>
          <CircularProgress
            size={50}
            sx={{ color: 'white', m: 'auto', position: 'absolute', top: 0, left: 0, bottom: 0, right: 0 }}
          />
          <Typography color="white" sx={{ mt: '100px', ml: '10px' }}>
            Loading...
          </Typography>
        </div>
      )}
    </>
  );
};

export default LoadingSpinner;
