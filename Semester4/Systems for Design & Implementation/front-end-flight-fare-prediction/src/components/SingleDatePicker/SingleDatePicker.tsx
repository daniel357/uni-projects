import 'react-dates/lib/css/_datepicker.css';
import React, { useState } from 'react';
import { SingleDatePicker } from 'react-dates';
import { Moment } from 'moment';

require('react-dates/initialize');

interface DatePickerProps {
  date: Moment | null;
  onDateChange: (date: Moment | null) => void;
  initialVisibleMonth: () => Moment;
  isOutsideRange: (day: Moment) => boolean;
}

const CustomSingleDatePicker: React.FC<DatePickerProps> = ({
                                                             date,
                                                             onDateChange,
                                                             initialVisibleMonth,
                                                             isOutsideRange,
                                                           }) => {
  const [focused, setFocused] = useState<boolean>(false);

  return (
    <SingleDatePicker
      date={date}
      onDateChange={onDateChange}
      focused={focused}
      onFocusChange={({ focused }) => setFocused(focused)}
      id="single_date_picker"
      numberOfMonths={1}
      initialVisibleMonth={initialVisibleMonth}
      isOutsideRange={isOutsideRange}
      displayFormat="YYYY-MM-DD"
    />
  );
};

export default CustomSingleDatePicker;
