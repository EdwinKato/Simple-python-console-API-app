"""
    This console application prints out the exchange rates for certain currencies as documented on http://fixer.io/
"""

import http.client
import json
from prettytable import PrettyTable


def main():
    try:
        connection = http.client.HTTPConnection('api.fixer.io')
        connection.request('GET', '/latest')
        response = json.loads(connection.getresponse().read().decode())
        rates = response["rates"]
        print("Latest Currency rates with base currency as Euro ")
        table = PrettyTable(['Currency', 'Rate'])
        for currency in rates:
            table.add_row([currency, rates[currency]])

        print(table)
    except Exception as e:
        print(type(e))
        print(e)


if __name__ == '__main__':
    main()