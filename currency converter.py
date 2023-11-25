

import requests

class CurrencyConverter:
    def __init__(self):
        self.base_url = "https://api.exchangeratesapi.io/latest"

    def get_exchange_rates(self):
        response = requests.get(self.base_url)
        data = response.json()
        return data["rates"]

    def convert(self, amount, from_currency, to_currency):
        rates = self.get_exchange_rates()

        if from_currency == to_currency:
            return amount

        if from_currency != "EUR":
            amount = amount / rates[from_currency]

        converted_amount = amount * rates[to_currency]
        return converted_amount

if __name__ == "__main__":
    converter = CurrencyConverter()

    print("Welcome to the Currency Converter!")

    while True:
        try:
            amount = float(input("Enter the amount: "))
            from_currency = input("From currency (3-letter code): ").upper()
            to_currency = input("To currency (3-letter code): ").upper()

            result = converter.convert(amount, from_currency, to_currency)

            print(f"{amount} {from_currency} is equal to {result} {to_currency}")
        except ValueError:
            print("Please enter a valid number.")
        except KeyError:
            print("Invalid currency code. Please check your input.")
        finally:
            choice = input("Do you want to convert another currency? (yes/no): ")
            if choice.lower() != "yes":
                break
