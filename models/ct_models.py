""" it contains classes for the project:
    class Tournaments
    class Players
    class Rounds, with classify and game methods """

class Tournaments:
    """ each tournament contains
        a number of rounds, 4 by default
        a list with rounds
        a list of players's index
        a time-controller's type, 
        1 for blitz 2 for bullet and 3 for speed
        and a description
    :param: name is a string
            place is a string
            date is a float, with 8 digits """
    def __init__(self,name,place,date):
        self.name = name
        self.place = place
        self.date = date
        self.total_of_rounds = 4
        self.rounds = []
        self.participants = []
        self.time_controller = 1
        self.description = ""

class Players:
    """ each player have an attribute ranking, 0 by default
        :param: last_name and first_name are strings
                birth_date is a float with 8 digits
                genre is a float, 1 for male and 2 for female """
    def __init__ (self, name1, name2, date, genre):
        self.last_name = name1
        self.first_name = name2
        self.birth_date = date
        self.genre = genre
        self.rating = 0
        self.event_points = 0
    def informations(self):
        info_list = [self.last_name, self.first_name,self.birth_date,
                     self.genre, self.rating, self.event_points]
        return info_list

class Rounds:
    """ rounds of a tournament
        finishing_time is a list with one date and one time
        round_type is a boolean, 
        true for the first round and false for others rounds
        :param: a_list is the players's list for the tournament
                a_number is a float, the round's number
                time1 is a list of tuples with date and hour keys """
    def __init__(self,a_list,a_number,time1):
        self.participants = a_list
        self.round_number = a_number
        self.starting_time = time1
        self.finishing_time = {'day':[],'hour':[]}

    def classify(a_list):
        """ create players's ranking
            to create each match in the round
            :param: a_list of players
            :return: a list of players, in order to create matchs """
        #ici on va classer les joueurs
        #attention, il y a un classement pour le round 1
        #et un autre type de classement pour les autres rounds
        classify_list = a_list
        return classify_list

    def game(a_list):
        """ create a liste of matchs for a round
            :param: a list of players
            :return:a list Games of tuples, with keys
            opponents and score """
        match = {'opponents':[A,B],'score':[0,0]}
        games =[]
        return games

