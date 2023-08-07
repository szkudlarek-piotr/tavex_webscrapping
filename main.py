import requests
import pandas as pd
from bs4 import BeautifulSoup
codes = []
tavex_buys_for_arr = []
tavex_sells_for_arr = []
capitalism_ratios = []
req_tavex = requests.get("https://tavex.pl/kantor-warszawa-centrum/")
tavex_center_txt = req_tavex.text

soup = BeautifulSoup(tavex_center_txt, features="html.parser")
currencies = soup.findAll("tr", {"class", "list-table__row js-filter-search-row"})

for currency in currencies:
    print(currency)
    print("\n")
    rates = currency.findAll("td", {"class", "list-table__col list-table__col--value"})
    print(rates)
    code = currency.find("abbr").get_text()
    print(code)
    codes.append(code)

    try:
        tavex_buys_for = float(rates[0].get_text())
    except:
        tavex_buys_for = "NaN"
        print("Tavex nie skupuje {}".format(code))
    tavex_buys_for_arr.append(tavex_buys_for)

    try:
        tavex_sells_for = float(rates[1].get_text())
    except:
        tavex_sells_for = "NaN"
        print("Tavex nie skupuje {}".format(code))
    tavex_sells_for_arr.append(tavex_sells_for)

    try:
        capitalism_ratio = round(tavex_buys_for / tavex_sells_for,4)
    except:
        capitalism_ratio = "NaN"
    capitalism_ratios.append(capitalism_ratio)
currencies_table = pd.DataFrame.from_dict({"ABBR": codes, "SELL": tavex_buys_for_arr, "BUY": tavex_sells_for_arr,
"CPR": capitalism_ratios})
print(currencies_table)
