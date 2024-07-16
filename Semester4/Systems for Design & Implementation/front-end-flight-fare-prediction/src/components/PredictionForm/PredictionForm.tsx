import React, { useEffect, useState } from 'react';
import CustomSingleDatePicker from '../SingleDatePicker/SingleDatePicker';
import moment, { Moment } from 'moment';
import { TextField } from '@mui/material';
import { LocalizationProvider, TimePicker } from '@mui/x-date-pickers';
import { AdapterMoment } from '@mui/x-date-pickers/AdapterMoment';
import { renderTimeViewClock } from '@mui/x-date-pickers/timeViewRenderers';
import styles from './PredictionForm.module.scss';
import { useHttp } from 'src/hooks/useHttp';
import { EmailDto, FlightDto } from '../../types/flight.types';
import ResultsModal from '../ResultsModal/ResultsModal';
import FlightFarePredictionsApi from '../../services/api/flightFarePredictions/flightFarePredictions.api'; // Import the new ResultsModal component

const PredictionForm: React.FC = () => {
  const { http } = useHttp({ withLoading: true });
  const [departureDate, setDepartureDate] = useState<Moment | null>(null);
  const [searchDate, setSearchDate] = useState<Moment | null>(null);
  const [departureTime, setDepartureTime] = useState<Moment | null>(null);
  const [arrivalTime, setArrivalTime] = useState<Moment | null>(null);
  const [isFormValid, setIsFormValid] = useState(false);
  const [predictedNumberOfDays, setPredictedNumberOfDays] = useState<number | null>(null);
  const [open, setOpen] = useState(false);

  useEffect(() => {
    setIsFormValid(
      searchDate !== null &&
      departureDate !== null &&
      departureTime !== null &&
      arrivalTime !== null
    );
  }, [searchDate, departureDate, departureTime, arrivalTime]);

  const handleSubmitFormData = async (event: React.FormEvent) => {
    event.preventDefault();
    const flightData: FlightDto = {
      searchDate: searchDate ? searchDate.format('YYYY-MM-DD') : null,
      flightDate: departureDate ? departureDate.format('YYYY-MM-DD') : null,
      departureHour: departureTime ? departureTime.hour() : null,
      departureMinute: departureTime ? departureTime.minute() : null,
      arrivalHour: arrivalTime ? arrivalTime.hour() : null,
      arrivalMinute: arrivalTime ? arrivalTime.minute() : null
    };

    try {
      const response = await http(() => FlightFarePredictionsApi.submitFlightDataForPrediction(flightData));
      // const response = { prediction: 4 };
      const roundedPrediction = Math.round(response.prediction);
      setPredictedNumberOfDays(roundedPrediction);
      setOpen(true);
      console.log(response);
    } catch (error) {
      console.error('Error submitting flight data', error);
    }
  };

  const handleSubmitEmail = async (email: string) => {
    if (!departureTime || !predictedNumberOfDays || !departureDate) {
      return;
    }
    const mailDate: EmailDto = {
      flightDate: departureDate.format('YYYY-MM-DD'),
      departureHour: departureTime.hour(),
      departureMinute: departureTime.minute(),
      toEmail: email,
      predictedDays: predictedNumberOfDays
    };

    try {
      await http(() => FlightFarePredictionsApi.sendMailToUser(mailDate));
    } catch (error) {
      console.error('Error submitting flight data', error);
    }
  };

  const resetForm = () => {
    setDepartureDate(null);
    setSearchDate(null);
    setDepartureTime(null);
    setArrivalTime(null);
    setPredictedNumberOfDays(null);
  };

  const handleClose = () => {
    resetForm();
    setOpen(false);
  };

  const isSearchDateOutsideRange = (day: Moment): boolean => {
    const firstSearchDate = moment('2022-04-17');
    const lastSearchDate = moment('2022-10-05');
    return !day.isBetween(firstSearchDate, lastSearchDate, 'day', '[]') ||
      (departureDate !== null && day.isAfter(departureDate, 'day'));
  };

  const isDepartureDateOutsideRange = (day: Moment): boolean => {
    const firstFlightDate = moment('2022-05-01');
    const lastFlightDate = moment('2022-11-09');
    return !day.isBetween(firstFlightDate, lastFlightDate, 'day', '[]') ||
      (searchDate !== null && day.isBefore(searchDate, 'day'));
  };

  const handleSearchDateChange = (date: Moment | null) => {
    setSearchDate(date);
    if (departureDate && date && date.isAfter(departureDate, 'day')) {
      setDepartureDate(null);
    }
  };

  const handleDepartureDateChange = (date: Moment | null) => {
    setDepartureDate(date);
    if (searchDate && date && date.isBefore(searchDate, 'day')) {
      setSearchDate(null);
    }
  };

  const getInitialSearchDateVisibleMonth = () => {
    if (departureDate) {
      return departureDate;
    }
    return moment('2022-04', 'YYYY-MM');
  };

  const getInitialDepartureDateVisibleMonth = () => {
    if (searchDate) {
      return searchDate;
    }
    return moment('2022-05', 'YYYY-MM');
  };

  return (
    <>
      <form className={styles.form} onSubmit={handleSubmitFormData}>
        <div className={styles.row}>
          <div className={styles.field}>
            <label htmlFor='searchDate'>Search Date</label>
            <CustomSingleDatePicker
              date={searchDate}
              onDateChange={handleSearchDateChange}
              initialVisibleMonth={getInitialSearchDateVisibleMonth}
              isOutsideRange={isSearchDateOutsideRange}
            />
          </div>
          <div className={styles.field}>
            <label htmlFor='departureDate'>Departure Date</label>
            <CustomSingleDatePicker
              date={departureDate}
              onDateChange={handleDepartureDateChange}
              initialVisibleMonth={getInitialDepartureDateVisibleMonth}
              isOutsideRange={isDepartureDateOutsideRange}
            />
          </div>
        </div>
        <div className={styles.row}>
          <LocalizationProvider dateAdapter={AdapterMoment}>
            <div className={styles.field}>
              <label htmlFor='departureTime'>Departure Time</label>
              <TimePicker
                value={departureTime}
                onChange={(newValue) => setDepartureTime(newValue)}
                renderInput={(params: any) => <TextField {...params} />}
                viewRenderers={{
                  hours: renderTimeViewClock,
                  minutes: renderTimeViewClock,
                  seconds: renderTimeViewClock
                }}
                sx={{ backgroundColor: 'white' }}
              />
            </div>
            <div className={styles.field}>
              <label htmlFor='arrivalTime'>Arrival Time</label>
              <TimePicker
                value={arrivalTime}
                onChange={(newValue) => setArrivalTime(newValue)}
                viewRenderers={{
                  hours: renderTimeViewClock,
                  minutes: renderTimeViewClock,
                  seconds: renderTimeViewClock
                }}
                renderInput={(params: any) => <TextField {...params} />}
                sx={{ backgroundColor: 'white' }}
              />
            </div>
          </LocalizationProvider>
        </div>
        <button type='submit' className={styles.button} disabled={!isFormValid}>Check Now</button>
      </form>
      <ResultsModal
        open={open}
        onClose={handleClose}
        departureDate={departureDate}
        departureTime={departureTime}
        predictedNumberOfDays={predictedNumberOfDays}
        sendEmail={handleSubmitEmail}
      />
    </>
  );
};

export default PredictionForm;
