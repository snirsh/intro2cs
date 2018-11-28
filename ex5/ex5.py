import xml.etree.ElementTree as ET


def get_attribute(store_db, ItemCode, tag):
    '''
    Returns the attribute (tag)
    of an Item with code: Itemcode in the given store
    '''
    return store_db[ItemCode].get(tag)


def string_item(item):
    '''
    Textual representation of an item in a store.
    Returns a string in the format of '[ItemCode] (ItemName)'
    '''
    return str('[' + item["ItemCode"] + ']' + '\t' + '{' + item["ItemName"]
               + '}')


def string_store_items(store_db):
    '''
    Textual representation of a store.
    Returns a string in the format of:
    string representation of item1
    string representation of item2
    '''
    # representation will be the string that will contain the textual
    # representation of all the items in the store
    representation = ''
    # running a loop on each item in the store_db
    for item in store_db.items():
        # adding to representation each of the items as a string and a new line
        representation += str(string_item(item[1]) + '\n')
    # returns representation
    return representation


def read_prices_file(filename):
    '''
    Read a file of item prices into a dictionary.  The file is assumed to
    be in the standard XML format of "misrad hacalcala".
    Returns a tuple: store_id and a store_db,
    where the first variable is the store name
    and the second is a dictionary describing the store.
    The keys in this db will be ItemCodes of the different items and the
    values smaller  dictionaries mapping attribute names to their values.
    Important attributes include 'ItemCode', 'ItemName', and 'ItemPrice'
    '''
    # parsing the given XML file into tree
    tree = ET.parse(filename)
    root = tree.getroot()
    # store_db will be the store's database
    store_db = {}
    # an empty dictionary that will store every item as a dictionary and will
    # be uses later
    newdic = {}
    # run a loop on all the items in store
    for element in root[5]:
        # a loop that runs for every individual item
        for item in element:
            # creating a dictionary for every item
            newdic[item.tag] = item.text
            # saving the item's code as the dictionary key
            if item.tag == "ItemCode":
                ItemCode = item.text
        # creating the wanted dictionary with Item Code: item
        store_db[ItemCode] = dict(newdic)
    # returning store_db with the wanted list
    return root[2].text, store_db


def filter_store(store_db, filter_txt):
    '''
    Create a new dictionary that includes only the items
    that were filtered by user.
    I.e. items that text given by the user is part of their ItemName.
    Args:
    store_db: a dictionary of dictionaries as created in read_prices_file.
    filter_txt: the filter text as given by the user.
    '''
    # newdb will be the dictionary of the items
    newdb = dict()
    # a loop that will run for every key in store db
    for i in store_db:
        # checking if the value of an item is a key, because there is one
        # which is the store ID and which will not be in use. also, checking if
        # the given text is in "ItemName" so we can put it into our new list
        if type(store_db[i]) is dict and filter_txt in store_db[i]["ItemName"]:
            # appending the "i" key (itemID) its value from the dictionary of
            # the item
            newdb[i] = dict(store_db[i])
    # returning the newdb
    return newdb


def create_basket_from_txt(basket_txt):
    '''
    Receives text representation of few items (and maybe some garbage
      at the edges)
    Returns a basket- list of ItemCodes that were included in basket_txt
    '''
    # the list that will contain the item codes
    basket = []
    # running in the range of the basket_txt length
    for i in range(len(basket_txt)):
        # checking if the letter in index i is [
        if basket_txt[i] is '[':
            # setting a boolean that will remain True from the point the letter
            # we have is '[' and until it's ']'
            isbracket = True
            # starting an index called start that will save the
            # position of '[' in our string and raise the counter to move
            # forward and check the text
            start = i + 1
            i += 1
            # running a loop as long as the value of the index  is '[' and as
            # far as the basket_txt length
            while isbracket and i < len(basket_txt):
                # checking if there's a ']' in basket_txt to tell the
                # loop when to finish index
                if basket_txt[i] is ']':
                    finish = i
                    # appending the text between the brackets and when
                    # finishing appending changing the boolean to false
                    basket.append(basket_txt[start:finish])
                    isbracket = False
                # when finishing move the counter by one
                i += 1
    # return the filtered item
    return basket


def get_basket_prices(store_db, basket):
    '''
    Arguments: a store - dictionary of dictionaries and a basket -
       a list of ItemCodes
    Go over all the items in the basket and create a new list
      that describes the prices of store items
    In case one of the items is not part of the store,
      its price will be None.
    '''
    # defining an empty list that will be later filled with the items' prices
    newbasket = []
    # running for every item code in the basket
    for ItemCode in basket:
        # checking if the item code is available in the store database
        if ItemCode in store_db.keys():
            # add the new list the price fot a specific item code in the basket
            newbasket.append(float(store_db[ItemCode].get("ItemPrice")))
        # if the item isn't in the store, assign price as None
        else:
            newbasket.append(None)
    # returning basket prices
    return newbasket


def sum_basket(price_list):
    '''
    Receives a list of prices
    Returns a tuple - the sum of the list (when ignoring Nones)
    and the number of missing items (Number of Nones)
    '''
    # count the number of missing items in a store
    missing = price_list.count(None)
    # summing the price of all items in basket without counting the Nones
    price = sum(filter(None, price_list))
    # returning a tuple containing the summed price and the number of
    # missing items
    return price, missing


def basket_item_name(stores_db_list, ItemCode):
    '''
    stores_db_list is a list of stores (list of dictionaries of
      dictionaries)
    Find the first store in the list that contains the item and return its
    string representation (as in string_item())
    If the item is not available in any of the stores return only [ItemCode]
    '''
    # checking if Item Code is not one of the keys in the store's database, and
    # if it doesnt the function will return [ItemCode]
    if ItemCode not in stores_db_list[1]:
        return '[' + ItemCode + ']'
    # if it is in the dictionary we'll return ItemCode as a string_item
    else:
        return string_item(stores_db_list[1][ItemCode])


def save_basket(basket, filename):
    '''
    Save the basket into a file
    The basket representation in the file will be in the following format:
    [ItemCode1]
    [ItemCode2]
    ...
    [ItemCodeN]
    '''
    newstring = ''
    # opening a file in "appending" mode so user can add items to the basket
    file = open(filename, 'a')
    # writing all items to the file, each item in a separate line)
    for i in range(len(basket)):
        newstring += '['+basket[i]+']'+'\n'
    file.write(newstring)


def load_basket(filename):
    '''
    Create basket (list of ItemCodes) from the given file.
    The file is assumed to be in the format of:
    [ItemCode1]
    [ItemCode2]
    ...
    [ItemCodeN]
    '''
    # opening the text file with the given name and join it's string without
    # line spaces into basket
    with open(filename, "r") as myfile:
        basket = myfile.read().replace('\n', '')
    # converting basket string into a list of ItemCodes using the function
    # create_basket_from_text
    return create_basket_from_txt(basket)


def best_basket(list_of_price_list):
    '''
    Arg: list of lists, where each inner list is list of prices as created
    by get_basket_prices.
    Returns the cheapest store (index of the cheapest list) given that a
    missing item has a price of its maximal price in the other stores *1.25
    '''
    # defining default values for key variables for the function that
    # will later be used
    best_store = 0
    lowest_sum = 0
    item_price = 0
    # run a loop which is as long as the number of baskets needed to be
    # compared
    for cur_lst in list_of_price_list:
        # resetting a temporary basket price for the current sum price not
        # including the None "penalties". "missing" will not be used in the
        # function and exist only to separate the sum price from the sum tuple.
        sum_price, missing = sum_basket(cur_lst)
        # running a loop through all items in a list in order to find all
        # "None" items in a list and giving them a "price"
        for item in range(len(cur_lst)):
            # check if the current item the program is looking at is a missing
            # item
            if cur_lst[item] is None:
                # running a loop that will compare the missing item price in
                # all other price lists.
                # the loop runs as many times as stores compared in case we
                # will want to add an option for comparing more then 3 stores.
                for i in range(len(list_of_price_list)):
                    # finding the highest price of the item in an equivalent
                    # store
                    if (list_of_price_list[i][item] is not None) and (
                                list_of_price_list[i][item] > item_price):
                        item_price = (list_of_price_list[i][item])
                # adding 25% to the already highest price for not having the
                # item in store.
                item_price *= 1.25
                # add the price of the item to the basket's sum.
                sum_price += item_price
        # comparing the current prices sum to the lowest basket price the
        # program already knows
        if sum_price < lowest_sum:
            # if current sum is lower than the lowest so far, assign as the
            # new lowest
            lowest_sum = sum_price
            # assign the best_store the index of the lowest known basket
            best_store = list_of_price_list.index(cur_lst)
        # when in the first iteration of the loop, assign the first sum as
        # the lowest sum and the best basket as the first one
        elif lowest_sum == 0:
            lowest_sum = sum_price
            best_store = list_of_price_list.index(cur_lst)
    # return the best basket
    return best_store