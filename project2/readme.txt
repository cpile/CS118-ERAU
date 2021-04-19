Write a program that reads a given text file and interprets the 1st line as the name of the Keys and every following line as Values.
Keys and Values will be used to create dictionaries. I.e. every line (but the 1st) will create a dict.

Here for instance are the keys: Name,Ticker,Market Cap,Price,PE Ratio,EPS,52 Week Range
This is one line of values: Microsoft Corp,MSFT,1930B,255.85,6.71,38.15,162.30:255.99

Every such dict will be appended to a list, which will become your list of stocks
Look here for ideas how to read a file line by line:
https://www.w3schools.com/python/python_file_open.asp
Also consider zip() function:
https://www.w3schools.com/python/ref_func_zip.asp

Your program will ask the user for an amount they want to invest.
Your program will show all the stocks it considered (i.e., those provided in the text file)
Your program will show the cheapest stock (lowest PE ration that is still greater than 0)
Your program will show the bargin stock (lowest in 52 week range)
Your program will show how many shares users could buy with the amount they want to invest.

Here is the output of a sample run:

How much do you want to invest? 1000

Here are the stocks I have considered for you:
 - Microsoft Corp - Market Cap is 1930B
 - Workday Inc - Market Cap is 62.573B
 - Service Now Inc - Market Cap is 103.933B
 - Amazon Inc - Market Cap is 1698B
 - Zoom Inc - Market Cap is 94.767B
 - Cisco Systems Inc - Market Cap is 219.913B

Currently, the cheapest stock is Microsoft Corp
You could buy 3 shares.

Zoom Inc is trading relatively low, considering its 52 week trading range.
At $322.65 per share, you could buy 3

2.)

Your program needs to implement these functions

def get_data_from_file(file_name):
    """
    Reads a file and interprets the 1st line as the name of the Keys
    Every following line will be used to create as Values.
    Keys and Values will be used to create dictionaries. I.e. every line (but the 1st) will create a dict
    Every such dict will be appended to a list, which will eventually be returned.
    :param file_name: file path (str)
    :return: list of dicts
    """

def get_num_of_shares(stock, investment):
    """
    Returns the number of shares one could buy of the the given stock with the given amount
    :param stock: dict
    :param investment: int of float
    :return: stock['Price']//investment (int)
    """

def find_cheapest_stock(stock_list):
    """
    Cheap means lowest price earning ratio, but the company needs to have earning.
    I.e. PE Ratio needs to be greater than 0
    :param stock_list: list dicts, every dict describes a stock
    :return: dict, the cheapest stock
    """

def find_bargain_stock(stock_list):
    """
    Bargain here means that a stock price is low, considering its 52 week trading range.
    I.e.: r = stock["52 Week Range"].split(':')
          bargain lowest stock["Price"] - tr[0] / tr[1] - tr[0]
    :param stock_list: list dicts, every dict describes a stock
    :return: dict, the cheapest stock
    """

def show(list_of_dicts, key):
    """
    Print the Company Name followed by the named value (e.g. 'PE Ratio') for every company dict in the list
    :param list_of_dicts: list dicts, every dict describes a stock
    :param key: value of this key will be printed for each item in the list
    :return: None
    """

Look at the provided "Starter Code" in the project2.zip archive	