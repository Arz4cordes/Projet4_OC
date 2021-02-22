""" it contains classes for the project:
    class Tournaments
    class Players
    class Rounds """


from tinydb import Query


class Players:
    """ each player have an attribute ranking, 0 by default
    :param: last_name and first_name are strings
    birth_date is a float with 8 digits
    genre is a float, 1 for male and 2 for female
    """

    players_list = []
    identification = 1

    def __init__(self, name1, name2, date, gendar, rating):
        self.first_name = name1
        self.last_name = name2
        self.birth_date = date
        self.gendar = gendar
        self.rating = rating
        self.event_points = 0.0
        self.identification = Players.identification
        self.opponents_list = []
        self.in_game = False
        Players.identification += 1
        return Players.players_list.append(self)

    def display(self):
        """ print informations for a player """
        text = "Nom: " + self.last_name + \
               " Prénom: " + self.first_name + \
               " Date de naissance: " + str(self.birth_date) + \
               " Genre: " + self.gendar + \
               "\nClassement: " + str(self.rating) + " points " + \
               " Points au tournoi en cours: " + str(self.event_points)
        return text

    def players_alphabetical_order():
        """ range in alphabetical order a list
        :return: the list, classify
        """
        the_list = sorted(Players.players_list, key=lambda player: player.last_name)
        return the_list

    def serialize(self):
        """ create a dictionay with player's attributes
        :return: serialized_player, type: dict
        """
        serialized_player = {"first name": self.first_name,
                             "last name": self.last_name,
                             "birth date": self.birth_date,
                             "gendar": self.gendar,
                             "rating": self.rating,
                             "event's points": self.event_points,
                             "identification": self.identification,
                             "in game": self.in_game,
                             "list of opponents": self.opponents_list}
        return serialized_player

    def players_by_rating(players_list):
        """ range by ranking
        :return: the list, classify
        """
        the_list = sorted(players_list, key=lambda player: player.rating, reverse=True)
        return the_list

    def players_classify_in_tournament(players_list):
        """ range by event's points
        :return: the list, classify
        """
        the_list = sorted(players_list, key=lambda player: player.event_points, reverse=True)
        return the_list

    def new_rating(self):
        """ input a new rating for a player and change it """
        self.display()
        condition = False
        while not condition:
            print("Entrer un nouveau classement pour le joueur,",
                  "à la place de", self.rating, "points:")
            rating = input()
            try:
                rating = float(rating)
                if rating >= 0:
                    condition = True
                    self.rating = rating
                    print("Le classement a bien été mis à jour:")
                    self.display()
                else:
                    print("Le classement est obligatoirement",
                          "un nombre positif.")
            except ValueError:
                print("Il faut entrer un nombre entier ou décimal")

    def db_update(self, players_db, key_entry):
        players_datas = Query()
        serialized_player = Players.serialize(self)
        try:
            for key in serialized_player.keys():
                if key == key_entry:
                    dico = {key: serialized_player[key]}
            return players_db.update(dico, players_datas.identification == self.identification)
        except AttributeError:
            return print("Erreur: l'attribut n'existe pas")


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
            date is a string, format dd/mm/aaaa
    """
    tournaments_list = []
    identification = 1

    def __init__(self, name, place, date, beginning_hour, time_controller):
        self.name = name
        self.place = place
        self.date = date
        self.beginning_hour = beginning_hour
        self.time_controller = time_controller
        self.total_of_rounds = 4
        self.number_of_participants = 8
        self.rounds = []
        self.participants = []
        self.description = ""
        self.identification = Tournaments.identification
        self.in_game = False
        Tournaments.identification += 1
        return Tournaments.tournaments_list.append(self)

    def display(self):
        """ print informations for a tournament """
        text = "\nNom du tournoi: " + self.name + \
               " Lieu du tournoi: " + self.place + \
               " Date du tournoi: " + str(self.date) + \
               "\nHeure de début: " + str(self.beginning_hour) + \
               " Controle du temps: " + str(self.time_controller) + \
               " Nombre de rondes " + str(self.total_of_rounds) + \
               " Nombre de participants: " + str(self.number_of_participants) + \
               "\nDescription: " + self.description
        if self.in_game:
            text += "\nStatut du tournoi: En cours"
        else:
            text += "\nStatut du tournoi: Terminé"
        return text

    def serialize(self):
        """ create a dictionay with the tournament's attributes
        :return: serialized_tournament, type: dict
        """
        identifications_list = []
        for player in self.participants:
            identifications_list.append(player.identification)
        serialized_tournament = {"name": self.name,
                                 "place": self.place,
                                 "date": self.date,
                                 "beginning hour": self.beginning_hour,
                                 "time controller": self.time_controller,
                                 "total of rounds": self.total_of_rounds,
                                 "number of participants": self.number_of_participants,
                                 "description": self.description,
                                 "in game boolean": self.in_game,
                                 "identification": self.identification,
                                 "players's identification": identifications_list}
        return serialized_tournament

    def db_update(self, tournaments_db, key_entry):
        tournaments_datas = Query()
        serialized_tournament = Tournaments.serialize(self)
        try:
            for key in serialized_tournament.keys():
                if key == key_entry:
                    dico = {key: serialized_tournament[key]}
            return tournaments_db.update(dico, tournaments_datas.identification == self.identification)
        except AttributeError:
            return print("Erreur: l'attribut n'existe pas")


class Rounds:
    """ rounds of a tournament
        finishing_time is a list with one date and one time
        in_game is a boolean,
        true for the first round and false for others rounds
        :param: a_list is the players's list for the tournament
                time1 is a list of tuples with date and hour keys
    """

    identification = 1

    def __init__(self, players_list, time1):
        self.participants = players_list
        self.starting_time = time1
        self.finishing_time = {'date': [], 'hour': []}
        self.in_game = False
        self.games = []
        self.tournament_affiliation = 0
        self.identification = Rounds.identification
        Rounds.identification += 1

    def display(self):
        """ print all matchs for a round """
        text = "Voici les matchs pour ce round:\n" + \
               "date de début: " + str(self.starting_time['date']) + \
               "   heure: " + str(self.starting_time['hour']) + "\n"
        if not self.in_game:
            text += "date de fin: " + str(self.finishing_time['date']) + \
                    "   heure: " + str(self.finishing_time['hour']) + "\n"
        for game in self.games:
            player1 = game['opponents'][0]
            player2 = game['opponents'][1]
            text += "\n" + player1.first_name + " " + player1.last_name + \
                    " (joueur " + str(player1.identification) + ")" + \
                    "   score: " + str(game["score"][0]) + "\ncontre\n" + \
                    player2.first_name + " " + player2.last_name + \
                    " (joueur " + str(player2.identification) + ")" + \
                    "   score: " + str(game["score"][1]) + "\n"
        return text

    def first_round_matchs_creation(self):
        """ create a liste of matchs for a round
            :return: a list Games of tuples, with keys
            opponents and score """
        # match = {'opponents':[A,B],'score':[0,0]}
        players_in_round = self.participants
        n = len(players_in_round) // 2
        for i in range(n):
            opponent1 = players_in_round[i]
            opponent2 = players_in_round[n + i]
            opponent1.opponents_list.append(opponent2.identification)
            opponent1.in_game = True
            opponent2.opponents_list.append(opponent1.identification)
            opponent2.in_game = True
            match = {'opponents': [opponent1, opponent2], 'score': [0, 0]}
            self.games.append(match)
        return self.games

    def matchs_creation(self):
        """ create a liste of matchs for a round
            :return: a list Games of tuples, with keys
            opponents and score
        """
        players_in_round = self.participants
        n = len(players_in_round)
        for i in range(n-1):
            opponent1 = players_in_round[i]
            if not opponent1.in_game:
                try:
                    j = i + 1
                    condition = False
                    while not condition:
                        condition1 = players_in_round[j].identification not in opponent1.opponents_list
                        condition2 = not players_in_round[j].in_game
                        if condition1 and condition2:
                            opponent2 = players_in_round[j]
                            opponent1.opponents_list.append(opponent2.identification)
                            opponent2.opponents_list.append(opponent1.identification)
                            opponent1.in_game = True
                            opponent2.in_game = True
                            match = {'opponents': [opponent1, opponent2], 'score': [0, 0]}
                            self.games.append(match)
                            condition = True
                        else:
                            j += 1
                except IndexError:
                    # If there is an exception in the swiss system,
                    # two players can meet again each other
                    try:
                        j = i + 1
                        condition = False
                        while not condition:
                            condition2 = not players_in_round[j].in_game
                            if condition2:
                                opponent2 = players_in_round[j]
                                opponent1.opponents_list.append(opponent2.identification)
                                opponent2.opponents_list.append(opponent1.identification)
                                opponent1.in_game = True
                                opponent2.in_game = True
                                match = {'opponents': [opponent1, opponent2], 'score': [0, 0]}
                                self.games.append(match)
                                condition = True
                            else:
                                j += 1
                    except IndexError:
                        print("Joueur sans match:")
                        print(opponent1.display())
        return self.games

    def new_results(self):
        """ launch the loop, to enter match's results """
        for game in self.games:
            game = self.match_results(game)
        self.in_game = False
        return self.games

    def match_results(self, a_game):
        """ input matchs's results
        :param: games_list is a list of tuples
                with keys 'opponents' and 'score'
        :return: the games_list, update
        """
        player1 = a_game['opponents'][0]
        player2 = a_game['opponents'][1]
        print(player1.first_name, player1.last_name, "(",
              player1.identification, ")", "contre",
              player2.first_name, player2.last_name, "(",
              player2.identification, ")",)
        verification = False
        while not verification:
            print("score pour ", player1.identification, player1.first_name, player1.last_name, ": \n")
            score1 = input()
            print("score pour ", player2.identification, player2.first_name, player2.last_name, ": \n")
            score2 = input()
            if score1 == "0" and score2 == "0":
                verification = True
                score1 = float(score1)
                score2 = float(score2)
            elif (score1 not in ["0", "0.5", "1"]) or (score2 not in ["0", "0.5", "1"]):
                print("Les scores entrés doivent être 0 ou 0.5 ou 1...")
            else:
                score1 = float(score1)
                score2 = float(score2)
                if score1 + score2 != 1:
                    print("Les résultats possibles sont 1 - 0, 0 - 1 ou 0.5 - 0.5...")
                else:
                    a_game['score'] = [score1, score2]
                    verification = True
        player1.event_points += score1
        player1.in_game = False
        player2.event_points += score2
        player2.in_game = False
        print("le score a bien été entré\n")
        return a_game

    def serialize(self):
        """ create a dictionay with the round's attributes
        :return: serialized_, type: ditoundct
        """
        games_for_db = []
        for game in self.games:
            player1 = game['opponents'][0]
            player2 = game['opponents'][1]
            score1 = game['score'][0]
            score2 = game['score'][1]
            games_for_db.append([player1.identification, player2.identification, score1, score2])
        serialized_round = {"starting time": self.starting_time,
                            "finishing time": self.finishing_time,
                            "in game": self.in_game,
                            "tournament's affiliation": self.tournament_affiliation,
                            "games in the round": games_for_db,
                            "identification": self.identification}
        return serialized_round

    def db_games_update(self, rounds_db):
        games_for_db = []
        for game in self.games:
            player1 = game['opponents'][0]
            player2 = game['opponents'][1]
            score1 = game['score'][0]
            score2 = game['score'][1]
            games_for_db.append([player1.identification, player2.identification, score1, score2])
        rounds_datas = Query()
        dict_update = {"games in the round": games_for_db}
        return rounds_db.update(dict_update, rounds_datas.identification == self.identification)

    def db_update(self, rounds_db, key_entry):
        rounds_datas = Query()
        serialized_round = Rounds.serialize(self)
        try:
            for key in serialized_round.keys():
                if key == key_entry:
                    dico = {key: serialized_round[key]}
            return rounds_db.update(dico, rounds_datas.identification == self.identification)
        except AttributeError:
            return print("Erreur: l'attribut n'existe pas")
