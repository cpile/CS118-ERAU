"""
    your docstring goes here ...
"""


def get_data_from_file(file_name):
    """
    Reads a file and interprets the 1st line as the name of the Keys
    Every following line will be used to create as Values.
    Keys and Values will be used to create dictionaries. I.e. every line (but the 1st) will create a dict
    Every such dict will be appended to a list, which will eventually be returned.
    Look here for ideas how to read a file line by line:
    https://www.w3schools.com/python/python_file_open.asp
    Also consider zip():
    https://www.w3schools.com/python/ref_func_zip.asp

    :param file_name: file path (str)
    :return: list of dicts
    """
    stocks = []
    with open(file_name) as fh:
        keys = line2words(fh.readline())
        for line in fh:
            stocks.append(dict(zip(keys, line2words(line))))
    return stocks


def get_num_of_shares(stock, investment):
    """
    Returns the number of shares one could buy of the the given stock with the given amount
    :param stock: dict
    :param investment: int of float
    :return: stock['Price']//investment (int)
    """
    return int(investment // float(stock['Price']))


def find_cheapest_stock(stock_list):
    """
    Cheap means lowest price earning ratio, but the company needs to have earning.
    I.e. PE Ratio needs to be greater than 0
    :param stock_list: list dicts, every dict describes a stock
    :return: dict, the cheapest stock
    """

    cheap = [(i['Name'], i['PE Ratio']) for i in stock_list]  # makes a list of tuples [(Stock Name, PE Ratio)]
    cheap.sort(key=lambda i: float(i[1]))  # uses lamba to sort list of tuples by PE Ratio
    for i in cheap:  # finds the cheapest stock that has a PE Ratio > 0
        if float(i[1]) > 0:
            low = i[0]
            for k in stock_list:
                if k['Name'] == low:
                    return k


def find_bargain_stock(stock_list):
    """
    Bargain here means that a stock price is low, considering its 52 week trading range.
    I.e.: r = stock["52 Week Range"].split(':')
          bargain lowest stock["Price"] - tr[0] / tr[1] - tr[0]
    :param stock_list: list dicts, every dict describes a stock
    :return: dict, the cheapest stock
    """

    bargain_stocks = [(i['Name'], i['Price'], i['52 Week Range'].split(':')) for i in stock_list]
    lowest = [(k[0], (float(k[1]) - float(k[2][0])) / (float(k[2][1]) - float(k[2][0]))) for k in bargain_stocks]
    bargain_stock = min(lowest, key=lambda f: f[1])
    for i in stock_list:
        if i['Name'] == bargain_stock[0]:
            return i


def show(list_of_dicts, key):
    """
    Print the Company Name followed by the named value (e.g. 'PE Ratio') for every company dict in the list
    :param list_of_dicts: list dicts, every dict describes a stock
    :param key: value of this key will be printed for each item in the list
    :return: None
    """
    print("\nHere are the stocks I have considered for you:")
    for i in list_of_dicts:  # iterates through list_of_dicts and prints Name and Market Cap
        print(f" - {i['Name']} - Market Cap is {i['Market Cap']} ")


def line2words(line):
    return line.replace("\n", "").split(',')


DATA_FILE = "stocks.csv"


# Capture a valid input
while True:
    x = input("How much do you want to invest? ")
    if x.isnumeric():
        break

# un comment this section line by line and make the program work

list_of_stocks = get_data_from_file(DATA_FILE)
cheapest = find_cheapest_stock(list_of_stocks)
bargain = find_bargain_stock(list_of_stocks)
#
show(list_of_stocks, "Market Cap")
print(f"\nCurrently, the cheapest stock is {cheapest['Name']}")
print(f"You could buy {get_num_of_shares(cheapest, float(x))} shares.")
print(f"\n{bargain['Name']} is trading relatively low, considering its 52 week trading range.")
print(f"At ${bargain['Price']} per share, you could buy {get_num_of_shares(bargain, float(x))}")
#
assert (len(list_of_stocks) == open(DATA_FILE).read().count('\n'))
assert (0 < float(cheapest['PE Ratio']))
assert (0 == get_num_of_shares(cheapest, 0))
assert (1 == get_num_of_shares(cheapest, float(cheapest['Price'])))
