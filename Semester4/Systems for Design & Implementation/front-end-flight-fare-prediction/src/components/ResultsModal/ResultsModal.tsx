import React, { useState } from 'react';
import Modal from '@mui/material/Modal';
import CloseIcon from '@mui/icons-material/Close';
import { Moment } from 'moment';
import { Button, TextField, Snackbar, Alert } from '@mui/material';
import styles from '../PredictionForm/PredictionForm.module.scss';

interface ResultsModalProps {
  open: boolean;
  onClose: () => void;
  departureDate: Moment | null;
  departureTime: Moment | null;
  predictedNumberOfDays: number | null;
  sendEmail: (email: string) => void;
}

const ResultsModal: React.FC<ResultsModalProps> = ({
                                                     open,
                                                     onClose,
                                                     departureDate,
                                                     departureTime,
                                                     predictedNumberOfDays,
                                                     sendEmail
                                                   }) => {
  const [email, setEmail] = useState('');
  const [isEmailValid, setIsEmailValid] = useState(true);
  const [showSuccessMessage, setShowSuccessMessage] = useState(false);

  const handleEmailChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setEmail(event.target.value);
    setIsEmailValid(true);
  };

  const validateEmail = (email: string) => {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
  };

  const handleSendEmail = () => {
    if (validateEmail(email)) {
      sendEmail(email);
      setEmail('');
      setShowSuccessMessage(true);
      setTimeout(() => {
        setShowSuccessMessage(false);
      }, 3000);
    } else {
      setIsEmailValid(false);
    }
  };

  return (
    <Modal
      open={open}
      onClose={onClose}
      aria-labelledby='prediction-result-title'
      aria-describedby='prediction-result-description'
      className={styles.modal}
    >
      <div className={styles.modalContent}>
        <CloseIcon className={styles.closeIcon} onClick={onClose} />
        <h2 id='prediction-result-title'>Optimal Purchase Time</h2>
        <p id='prediction-result-description'>
          For the flight on <strong>{departureDate?.format('MMMM Do, YYYY')}</strong> departing
          at <strong>{departureTime?.format('hh:mm A')}</strong>, it is recommended to purchase your
          ticket <strong>{predictedNumberOfDays} days</strong> before departure for the best fare.
        </p>
        <div className={styles.emailSection}>
          <p>Would you like to receive this information by email?</p>
          <TextField
            label='Email Address'
            variant='outlined'
            value={email}
            onChange={handleEmailChange}
            error={!isEmailValid}
            helperText={!isEmailValid ? 'Please enter a valid email address' : ''}
            fullWidth
            className={styles.emailInput}
          />
          <Button
            variant='contained'
            color='primary'
            onClick={handleSendEmail}
            className={styles.sendButton}
          >
            Send Email
          </Button>
        </div>
        <Snackbar
          open={showSuccessMessage}
          autoHideDuration={3000}
          onClose={() => setShowSuccessMessage(false)}
        >
          <Alert onClose={() => setShowSuccessMessage(false)} severity="success">
            Email sent successfully!
          </Alert>
        </Snackbar>
      </div>
    </Modal>
  );
};

export default ResultsModal;
