""" it contains classes for the project:
    class Tournaments
    class Players
    class Rounds """


class Players:
    """ each player have an attribute ranking, 0 by default
    :param: last_name and first_name are strings
    birth_date is a float with 8 digits
    genre is a float, 1 for male and 2 for female
    """

    players_list = []
    identification = 1

    def __init__(self, name1, name2, date, gendar):
        self.first_name = name1
        self.last_name = name2
        self.birth_date = date
        self.gendar = gendar
        self.rating = 0.0
        self.event_points = 0.0
        self.identification = Players.identification
        self.opponents_list = []
        self.in_game = False
        Players.identification += 1
        return Players.players_list.append(self)

    def display(self):
        """ print informations for a player """
        print("Nom: ", self.last_name,
              " Prénom: ", self.first_name,
              "Date de naissance: ", self.birth_date,
              " Genre: ", self.gendar,
              "\nClassement: ", self.rating, " points\n",
              "Points au tournoi en cours: ", self.event_points)
        return print("")

    def players_alphabetical_order():
        """ range in alphabetical order a list
        :return: the list, classify
        """
        print("Liste de tous les joueurs enregistrés, par ordre alphabétique:")
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
                             "in game": self.in_game}
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
                    self.display
                    return rating
                else:
                    print("Le classement est obligatoirement un nombre positif.")
            except ValueError:
                print("Il faut entrer un nombre entier ou décimal")


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
        print("Nom du tournoi: ", self.name,
              " Lieu du tournoi: ", self.place,
              "Date du tournoi: ", self.date,
              "\nHeure de début: ", self.beginning_hour,
              " Controle du temps: ", self.time_controller,
              " Nombre de rondes ", self.total_of_rounds,
              " Nombre de participants: ", self.number_of_participants,
              "\n Description: ", self.description)
        print("Liste des participants:")
        for player in self.participants:
            player.display()
        if self.in_game is True:
            print("Statut du tournoi: En cours")
        else:
            print("Statut du tournoi: Terminé")
        return print("")

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

    def first_round_matchs_creation(self):
        """ create a liste of matchs for a round
            :return: a list Games of tuples, with keys
            opponents and score """
        # match = {'opponents':[A,B],'score':[0,0]}
        for participant in self.participants:
            print(participant.first_name, participant.last_name)
        players_in_round = self.participants
        n = len(players_in_round) // 2
        print(n)
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
                except IndexError as e:
                    # If there is an exception in the swiss system,
                    # two players can meet again each other
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
        return self.games

    def display(self):
        """ print all matchs for a round """
        print("Voici les matchs pour ce round:\n")
        print("date de début:", self.starting_time['date'], "heure:", self.starting_time['hour'])
        if not self.in_game:
            print("date de fin:", self.finishing_time['date'], "heure:", self.finishing_time['hour'])
        for game in self.games:
            player1 = game['opponents'][0]
            player2 = game['opponents'][1]
            print(player1.first_name, player1.last_name, "( joueur",
                  player1.identification, ")", "score", game["score"][0])
            print("contre")
            print(player2.first_name, player2.last_name, "( joueur",
                  player2.identification, ")",
                  "score", game["score"][1], "\n")
        return print("")

    def new_results(self):
        """ launch the loop, to enter match's results """
        print("Entrez les résultats pour le match,\n",
              "sous la forme 0 puis 1 ou 1 puis 0 en cas de vainqueur, \n",
              "ou bien 0.5 pour chaque joueur en cas de nul. \n",
              "Vous pouvez marquer 0 à chacun pour passer au match suivant,\n",
              "sans entrer de résultat.")
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
