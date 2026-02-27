from forex_python.converter import CurrencyRates
c = CurrencyRates()

base = input("Enter base currency (e.g. USD): ").upper
target = input("Enter target currency (e.g. GBP): ").upper()
amount = float(input("Enter amount (number only): "))

rate = c.get_rate(base , target)
Converted = amount * rate

print(f"{amount} {base} = {converted:.2f} {target}")
