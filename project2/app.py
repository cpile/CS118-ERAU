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
    keys = None
    stocks = []
    with open(file_name) as f:
        for line in f:
            if not keys:
                keys = line.replace("\n", "").split(',')
            else:
                d = {}
                lst = line.replace("\n", "").split(",")  # e.g. 'John,Doe' => ['John','Doe']
                for i in range(len(keys)):  # 0,1 => keys[0] ='First Name', key[1]= 'Last Name'
                    d[keys[i]] = lst[i]
                stocks.append(d)
    return stocks


def get_num_of_shares(stock, investment):
    """
    Returns the number of shares one could buy of the the given stock with the given amount
    :param stock: dict
    :param investment: int of float
    :return: stock['Price']//investment (int)
    """
    return 0  # instead of 0, your code here ....


def find_cheapest_stock(stock_list):
    """
    Cheap means lowest price earning ratio, but the company needs to have earning.
    I.e. PE Ratio needs to be greater than 0
    :param stock_list: list dicts, every dict describes a stock
    :return: dict, the cheapest stock
    """
    cheap = [(i['Name'], i['PE Ratio']) for i in stock_list]
    cheap.sort(key=lambda i: float(i[1]))
    print(cheap)
    while True:
        for i in cheap:
            if float(i[1]) > 0:
                print(i[0])
                return i
        break


def find_bargain_stock(stock_list):
    """
    Bargain here means that a stock price is low, considering its 52 week trading range.
    I.e.: r = stock["52 Week Range"].split(':')
          bargain lowest stock["Price"] - tr[0] / tr[1] - tr[0]
    :param stock_list: list dicts, every dict describes a stock
    :return: dict, the cheapest stock
    """
    pass  # instead of pass, your code here ....


def show(list_of_dicts, key):
    """
    Print the Company Name followed by the named value (e.g. 'PE Ratio') for every company dict in the list
    :param list_of_dicts: list dicts, every dict describes a stock
    :param key: value of this key will be printed for each item in the list
    :return: None
    """
    print("\nHere are the stocks I have considered for you:")
    for i in list_of_dicts:
        pass  # instead of pass, your code here ....


DATA_FILE = "stocks.csv"


# Capture a valid input
while True:
    x = input("How much do you want to invest? ")
    if x.isnumeric():
        break

# un comment this section line by line and make the program work

list_of_stocks = get_data_from_file(DATA_FILE)
cheapest = find_cheapest_stock(list_of_stocks)
# bargain = find_bargain_stock(list_of_stocks)
#
# show(list_of_stocks, "Market Cap")
# print(f"\nCurrently, the cheapest stock is {cheapest['Name']}")
# print(f"You could buy {get_num_of_shares(cheapest, float(x))} shares.")
# print(f"\n{bargain['Name']} is trading relatively low, considering its 52 week trading range.")
# print(f"At ${bargain['Price']} per share, you could buy {get_num_of_shares(bargain, float(x))}")
#
# assert (len(list_of_stocks) == open(DATA_FILE).read().count('\n'))
# assert (0 < float(cheapest['PE Ratio']))
# assert (0 == get_num_of_shares(cheapest, 0))
# assert (1 == get_num_of_shares(cheapest, float(cheapest['Price'])))
