######################################################################
# FILE : ex10.py                                                     #
# WRITER : Snir Sharristh , snirsh , 305500001                       #
# EXERCISE : intro2cs ex10 2015-2016                                 #
# DESCRIPTION: creating a network of articles with special functions #
######################################################################

######################################################################
#                   Frequently Used Numbers                          #
######################################################################
default_d = 0.9
first_iter = 1
starting_money = 1
minimum_d = 1 - default_d
no_neighbors = 0
nothing = 0
pos0 = 0
pos1 = 1
one_occurance = 1
counter_inc = 1
counter_dec = 1

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
        and self.neighbor_names is a list of the names of the neighbors
        where every name is type string.
        """
        self.neighbors = []
        self.neighbor_names = []
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
        if neighbor.get_name() not in self.neighbor_names \
                and type(neighbor) is Article:
            self.neighbors.append(neighbor)
            self.neighbor_names.append(neighbor.get_name())

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
        output_repr = (self.name, self.neighbor_names)
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
        if type(article) is Article:
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
        friends and path are used in the last functions(recursive functions)
        """
        self.network = {}
        self.path = []
        self.create_articles(link_list)
        self.friends = []

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
            if article_name not in self.network.keys():
                self.network[article_name] = Article(article_name)
            neighbor = Article(article_neighbor)
            self.network[article_name].add_neighbor(neighbor)
        # here we check if there's a neighbor with no neighbors and create it
        neighbor_to_append = []
        for val in self.network.values():
            for neighbor in val.neighbor_names:
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
        """
        this method will create a ranking for all the articles based on the
        amount of times that other articles link to them.
        the function will run iter times and each time will do the base
        algorithm of page_rank
        """
        # a function that initializes the dict to have 1 money on all the
        # articles
        values_dict = self.get_money()
        articles = self.get_articles()
        contributions = {}
        if d == nothing:  # nothing == 0
            """
                            HOW SORT WORKS
            here we sort first by pos1 == 1 (value of dict) and we do it
            by descending order therefor it's -x and then we sort by
            keys(pos0 == 0) ascending order therefor x is positive
            """
            sorted_dict = \
                [v[pos0] for v in sorted(values_dict.items(),
                                         key=lambda x: (-x[pos1], x[pos0]))]
            return sorted_dict
        # running iter times (how many iterations) and each time we
        # calculate how much we need to contribute and contribute it to the
        # other articles.
        for i in range(iters):
            for article in articles:
                if article.__len__():
                    # how much contribution is (d*curr article money)
                    # divided by how many neighbors he has
                    contribution = \
                        (d * values_dict[
                            article.get_name()]) / article.__len__()
                    values_dict[article.get_name()] = minimum_d  # == 0.1
                else:  # if the current article has no neighbors
                    contribution = nothing  # == 0
                contributions[article] = contribution
            # here we contribute the money to all the neighbors
            for article in articles:
                for neighbor in article.neighbor_names:
                    values_dict[neighbor] += contributions[article]
        # same as the first time in this function
        sorted_dict = \
            [v[pos0] for v in
             sorted(values_dict.items(), key=lambda x: (-x[pos1], x[pos0]))]
        return sorted_dict

    def get_money(self):
        """
        this method will initiate a dictionary to be used in Page_rank.
        the keys are all the article names and their starting money is 1
        """
        values_dict = {}
        for value in self.network.values():
            values_dict[value.get_name()] = starting_money  # =1
        return values_dict

    def jaccard_index(self, article_name):
        """
        this method will create an index based on how many neighbors the
        given article has that is similar to the other articles.
        the main equation for it will be where a is first group and b is the
        second: A&B/A|B (where & is intersection and | is union)
        the function will create a list of all the article names in our
        network where each one has a jaccard ranking and the list is
        descending from the biggest jaccard ranking (the given article) to
        the one with the lowest ranking.
        """
        jaccard_dict = dict()
        # checking if article_name exists in our system
        if self.__contains__(article_name) is False:
            return None
        checked_list = self.network[article_name]
        article_len = checked_list.__len__()
        if article_len == no_neighbors:
            return None
        for val in self.network.values():
            # creating an intersection and union of curr article neighbors
            # and our given article neighbors
            inter = len(set(checked_list.neighbor_names) & set(
                val.neighbor_names))
            union = len(set(checked_list.neighbor_names) | set(
                val.neighbor_names))
            if union == nothing:  # == 0
                jaccard_dict[val.get_name()] = nothing  # == 0
            else:
                jaccard_dict[val.get_name()] = inter / union
        # see page rank to understand how sort works
        sorted_dict = \
            [v[pos0] for v in
             sorted(jaccard_dict.items(), key=lambda x: (-x[pos1], x[pos0]))]
        return sorted_dict

    def travel_path_iterator(self, article_name):
        """
        this function will travel from given point through the best ranked
        neighbor (where the best ranked neighbor is either the one with most
        neighbors or if all the neighbors have the same amount of neighbors the
        one with the lowest alphabetical name.) and continue to travel
        recursively.
        each time we travel we add the article name into a list until we get
        a big list with our path and when we finished traveling we return
        the path.
        """
        neighbor_rank = {}
        highest_ranks = []
        highest_val = nothing  # == 0
        # checks if the article exists
        if self.__contains__(article_name) is False:
            return iter([])  # returning an empty iterable list if not
        # adds the current article to the path
        self.path.extend(article_name)
        if self.path.count(article_name) > one_occurance:  # ==1
            return iter(self.path)
        if self.network[article_name].neighbor_names:
            neighbors = self.network[article_name].neighbor_names
            for neighbor in neighbors:  # running on the curr article neighbors
                neighbor_rank[neighbor] = self.rank_article(neighbor)
                # here we check if the current neighbor's rank is higher
                # then the last highest rank value. if so we change the
                # value of it
                if neighbor_rank[neighbor] > highest_val:
                    highest_val = neighbor_rank[neighbor]
            # appending all the highest neighbors to a list
            for neighbor in neighbors:
                if neighbor_rank[neighbor] == highest_val:
                    highest_ranks.append(neighbor)
            # getting the best highest rank (therefor we use min cause it
            # will be the minimal alphabetical value or itself where only
            # one is the highest)
            highest = min(highest_ranks[pos0])
            # continue recursively with the highest ranked neighbor we got
            self.travel_path_iterator(highest)
        return iter(self.path)

    def rank_article(self, article_name):
        """
        this method will rank a current article by increasing its rank by
        one for each article he has in his neighbors.
        the function will return the article's rank.
        """
        rank = nothing
        articles = self.get_articles()
        for article in articles:
            if article_name in article.neighbor_names:
                rank += counter_inc  # == 1
        return rank

    def friends_by_depth(self, article_name, depth):
        """
        this function will add the friends of the current article by depth.
        meaning we add the neighbors of the first article and the neighbor's
        neighbors we do this depth amount of times recursively.
        """
        if self.__contains__(article_name) is False:
            return None
        if depth > nothing:  # == 0
            # checking if the article name wasn't already appended and
            # appending it if needed
            if article_name not in self.friends:
                self.friends.extend(article_name)
            neighbors = self.network[article_name].neighbor_names
            if neighbors:
                for neighbor in neighbors:
                    # running recursively on every neighbor
                    self.friends_by_depth(neighbor, depth - counter_dec)  # =1
        else:
            # we get here when depth == 0 if so we just append the current
            # article's name if it's not already in our list
            if article_name not in self.friends:
                self.friends.extend(article_name)
        return self.friends

