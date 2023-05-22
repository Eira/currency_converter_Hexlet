from onlinerequests import get_rate

CURRENCIES = {'USD', 'RUB', 'GBP', 'EUR'}


def main() -> None:
    """Currency converter."""
    _show_greatings_and_info(CURRENCIES)

    user_currency = _get_user_currency(CURRENCIES)
    current_amount = _get_current_amount()
    conversion_currency = _get_conversion_currency(CURRENCIES)

    converted_amount = _process_converted_amount(
        user_currency,
        conversion_currency,
        current_amount,
    )

    print(f"Итого: {round(converted_amount, 2)} {conversion_currency}")


def _show_greatings_and_info(currencies: set[str]) -> None:
    """Print a greeting message and message about what this program do."""
    print('Добро пожалвать в конвертер валют!\n')
    print("""Наша программа поможет вам конвертировать валюты.
    1. Введение имеющийся валюты.
    2. Количетво валюты.
    3. Выбор валюты для конвертации.
    """)

    print("Вам предложены следующие валюты:")

    key_counter = 1
    for name in currencies:
        print(f'    {key_counter}. {name}')
        key_counter += 1


def _get_user_currency(currency: set[str]) -> str:
    """Get user currency and check if it's correct."""
    user_currency = input('Введите имеющуюся валюту: ').upper()

    while user_currency not in currency:
        user_currency = input('Некорректная валюта.\n Попробуйте еще раз:')

    return user_currency


def _get_current_amount() -> float:
    """Get amount of money to convert."""
    while True:
        try:
            current_amount = float(
                input('Введите имеющуюся сумму: '),
            )
        except ValueError:
            current_amount = 0.0

        if current_amount > 0:
            return current_amount

        print('Сумма не коректна. Попробуте еще раз!')


def _get_conversion_currency(currency: set[str]) -> str:
    """Get conversion currency."""
    conversion_currency = input('Выберете валюту для конвертации:').upper()

    while conversion_currency not in currency:
        conversion_currency = input(
            'Некорректная валюта.\n Попробуйте еще раз:',
        )

    return conversion_currency


def _process_converted_amount(
    user_currency: str,
    conversion_currency: str,
    current_amount: float,
) -> float:
    """Calculate converted amount of money and return it."""
    return current_amount * get_rate(user_currency, conversion_currency)


if __name__ == '__main__':
    main()
