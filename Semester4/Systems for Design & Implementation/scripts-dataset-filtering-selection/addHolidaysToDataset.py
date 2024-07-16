import pandas as pd
from datetime import timedelta

from getPublicHolidays import get_public_holidays


def mark_holidays_in_dataset(df, year, country_code):
    """
    Enhances the DataFrame by marking flight dates that are national holidays
    and those within +/- 5 days of a national holiday.

    Parameters:
    - df: The DataFrame with flight data, including a 'flightDate' column.
    - year (int): The year for which to fetch public holidays.
    - country_code (str): The country code for the holidays.

    Returns:
    - The enhanced DataFrame with two new columns: 'isHoliday' and 'nearHoliday'.
    """
    holidays = get_public_holidays(year, country_code)
    holiday_dates = [pd.to_datetime(holiday['date']) for holiday in holidays]

    def is_holiday(date):
        return date in holiday_dates

    def is_near_holiday(date):
        return any(
            pd.to_datetime(holiday_date) - timedelta(days=5) <= date <= pd.to_datetime(holiday_date) + timedelta(days=5)
            for holiday_date in holiday_dates)

    df['flightDate'] = pd.to_datetime(df['flightDate'])
    df['isHoliday'] = df['flightDate'].apply(is_holiday)
    df['nearHoliday'] = df['flightDate'].apply(is_near_holiday)

    return df

