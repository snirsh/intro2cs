######################################################################
# FILE : ex10.py                                                     #
# WRITER : Snir Sharristh , snirsh , 305500001                       #
# EXERCISE : intro2cs ex10 2015-2016                                 #
# DESCRIPTION:                                                       #
######################################################################
######################################################################
#                           IMPORTS                                  #
######################################################################
import operator
######################################################################
#                   Frequently Used Numbers                          #
######################################################################
default_d = 0.9
first_iter = 1
starting_money = 1
minimum_d = 1 - default_d
no_neighbors = 0


def read_article_links(file_name):
    """
    this function gets a file_name which is .txt file.
    the method will read the file_name.txt file into string and create a
    list of tuples where each tuple contains the words in each line.
    for example file:
    'a' 'b'
    'c' 'd'
    output:
    [('a','b'),('c','d')]

    :INPUT:
     file_name as a string of the required file name
    :return:
     output will be a list of tuples where every tuple will be a tuple of 2
     words
    """
    list_articles = []  # our output list
    # here we open the file as a read only file into file object and turn it
    # into a string called data
    with open(file_name, 'r') as file:
        data = file.read()
    # running on every line and splitting it into a tuple with 2 values that
    #  will be appended to the output list
    for line in data.splitlines():
        article_tuple = tuple(line.split('\t'))
        list_articles.append(article_tuple)
    return list_articles


class Article:
    def __init__(self, name):
        """
        our Article initializer. the init gets the name of the article
        :param name: and creates an Article object with this name
        self.neighbors will be a list of all the neighbors of article object
        """
        self.neighbors = []
        self.name = name

    def get_name(self):
        """
        this function returns the name of our article thus it will return
        self.name as the init saved name as a private value
        """
        return self.name

    def add_neighbor(self, neighbor):
        """
        this function adds a new neighbor into the Article's neighbor list
        input:
        :param neighbor
        output:
        None, updates the neighbor private list
        """
        if type(neighbor) is type:
            if neighbor not in self.neighbors:
                self.neighbors.append(neighbor)

    def get_neighbors(self):
        """
        this function returns all the neighbors for the current Article
        """
        return self.neighbors

    def __repr__(self):
        """
        representing the article as a tuple repr that contains
        (name (string), neighbors(a list of names))
        example for output:
        ('a' , [ 'b' , 'c' ])
        :return
        (name, neighbors)
        """
        output_repr = (self.name, self.get_neighbor_names())
        return str(output_repr)

    def __len__(self):
        """
        returning how many neighbors those the Article have, thus returning
        the length of the neighbors list that contains all the neighbors of
        the current Article
        :return:
        length(neighbors list)
        """
        return len(self.neighbors)

    def __contains__(self, article):
        """
        this function receives an article object as an input and returns
        True if the article is a neighbor of the current Article else it
        will return False.
        the boolean will be checked with the function get_name()
        :param article: a given Article to check
        :return:
        True or False
        """
        if type(article) is type:
            return article in self.neighbors
        return False

class WikiNetwork:
    def __init__(self, link_list=[]):
        """
        this is our initializer for a network in WikiNetwork.
        the function will create a dictionary of all the articles that we
        have from the file we got from read_article_list which here is
        link_list.
        to create the dictionary from Article objects we use a small helper
        function called create_articles. documentary for this function is below
        """
        self.network = dict()
        self.create_articles(link_list)

    def create_articles(self, link_list):
        """
        this function creates our dictionary or updates it if the dictionary
        already contains a certain key.
        with link_list (a list like the list we got from read_article_list)
        as an input it will create a dictionary with articles where the
        first item of the tuple is the article's name and the second item of
        the tuple is a neighbor.
        for example:
        if list is:
        'a' 'b'
        'a' 'c'
        'a' 'd'
        'b' 'c'
        the dictionary will be:
        {'a':['a',['b','c','d']], 'b':['b',['c']}
        """
        for article_name, article_neighbor in link_list:
            if article_name in self.network.keys():
                self.network[article_name].add_neighbor(article_neighbor)
            else:
                self.network[article_name] = Article(article_name)
                self.network[article_name].add_neighbor(article_neighbor)
        neighbor_to_append = []
        for val in self.network.values():
            for neighbor in val.get_neighbors():
                if neighbor not in self.network.keys():
                    neighbor_to_append.append(neighbor)
        for neighbor in neighbor_to_append:
            self.network[neighbor] = Article(neighbor)

    def update_network(self, link_list):
        """
        this function updates our network dictionary. it will update it
        using the function create_articles with the given link_list
        """
        self.create_articles(link_list)

    def get_articles(self):
        """
        this function will return all the articles we have in the network.
        thus we run on all the values in our network dictionary and return
        them.
        we'll set articles to be our output list and append to this list
        every value from our network (Article objects)
        :returns
        articles
        """
        articles = list()
        for article in self.network.values():
            articles.append(article)
        return articles

    def get_titles(self):
        """
        this function will return all the article titles we have in our
        network. therefor we'll set titles as our output list and append
        into it all the keys from our network dictionary and return it to
        the user
        :returns
        titles
        """
        titles = list()
        for title in self.network.keys():
            titles.append(title)
        return titles

    def __contains__(self, article_name):
        """
        checks if an articles name is in our network. therefor we'll create
        a list of all the titles (using get_titles method) and check if
        titles contain the given article name
        :returns
        True - if the article_name is in the keys of our network
        False  - if we don't have an article with this name
        """
        titles = self.get_titles()
        if article_name in titles:
            return True
        return False

    def __len__(self):
        """
        this function returns how many articles we have in our network
        therefor we use len and return the len of our network (meaning
        we return how many keys are in the dictionary)
        :return:
        length of our dictionary
        """
        return len(self.network)

    def __repr__(self):
        """
        a representation of the current dictionary as a string
        for example the string:
        {'a':['a',['b','c','d']], 'b':['b',['c','d'], 'c':['c',['d']]}
        :return:
        string(network dictionary)
        """
        return str(self.network)

    def __getitem__(self, article_name):
        """
        checks if our network has the article name in its values.
        if it doesnt we'll return an error that the article name is not a
        key in our network dictionary. we'll use __contains__ method to
        check if the given name is in our network if so we'll return it's
        article object. else raising the error
        :returns
        Article (if it's in our network)
        error (if we don't have an article with this name in our network)
        """
        if self.network.__contains__(article_name):
            return self.network[article_name]
        raise KeyError(article_name)

    def page_rank(self, iters, d=default_d):
        values_dict = self.get_money()
        articles = self.get_articles()
        for i in range(iters):
            for article in articles:
                contribution = article.__len__() / d
                for neighbor in article.get_neighbors():
                    values_dict[neighbor] += contribution
                values_dict[article.get_name()] = minimum_d
        sorted_dict = \
            sorted(values_dict, key=lambda k: values_dict[k], reverse=True)
        return sorted_dict

    def get_money(self):
        values_dict = dict()
        for value in self.network.values():
            values_dict[value.get_name()] = starting_money  # =1
        return values_dict

    def jacaard_index(self, article_name):
        jacaard_dict = dict()
        checked_list = self.network[article_name]
        article_len = checked_list.__len__()
        if article_len == no_neighbors:
            return None
        for val in self.network:
            inter = len(set(checked_list.get_neighbor_names()) & set(
                val.get_neighbor_names()))
            union = len(set(checked_list.get_neighbor_names()) | set(
                val.get_neighbor_names()))
            if union == 0:
                jacaard_dict[val.get_name] = 0
            else:
                jacaard_dict[val.get_name] = inter/union
        jacaard_list = sorted(jacaard_dict, key=lambda k: jacaard_dict[k])
        return jacaard_list

    def friends_by_depth(self):
        pass

