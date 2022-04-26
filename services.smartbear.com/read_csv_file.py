import csv
import re


def read_csv():
    expected_prices = { }
    with open('smart_prices.csv') as f:
        rows = csv.DictReader(f)
        for row in rows:
            expected_prices[row['product']] = float(row['price'])
    return expected_prices

def get_actual_price(price):
    temp = re.findall(r'[\d\.]', price)
    price = float(''.join(temp))
    return price

reference = read_csv()

# for name, expected_price in reference.items():
