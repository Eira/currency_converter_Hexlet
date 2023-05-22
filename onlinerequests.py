import requests

API_KEY = 'XoBEUPQfmGMrchtmk7VULD5dVnmzRrx8Oz9tC8Cj'
ENDPOINT = 'https://api.freecurrencyapi.com/v1/latest'


def get_rate(user_currency: str, converted_currency: str) -> float:
    """Get fresh rates from https://app.freecurrencyapi.com ."""
    response = requests.get(
        url=ENDPOINT,
        params={
            'apikey': API_KEY,
            'currencies': converted_currency,
            'base_currency': user_currency,
           }
    )

    return response.json()['data'].get(converted_currency)
