import requests


def get_public_holidays(year, country_code):
    """
    Fetches public holidays for a given year and country code from the API.

    Parameters:
    - year (str or int): The year for which to fetch public holidays.
    - country_code (str): The country code for which to fetch public holidays.

    Returns:
    - A list of dictionaries containing public holiday information, or an error message.
    """
    base_url = "https://date.nager.at/api/v3/publicholidays"
    endpoint = f"{base_url}/{year}/{country_code}"

    try:
        response = requests.get(endpoint)
        response.raise_for_status()
        holidays = response.json()

        return holidays
    except requests.exceptions.HTTPError as err:
        return f"HTTP Error: {err}"
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"


