import views.ct_views as view
import models.ct_models as modl


import re
from tinydb import TinyDB


def players_loading():
    """ load players saving in a json file,
        and create an object of the class Players
        for each player saved
        :return: players_db, json file open with tinydb
    """
    players_db = TinyDB('chess_players.json')
    for item in players_db:
        first_name = item["first name"]
        last_name = item["last name"]
        birth_date = item["birth date"]
        gendar = item["gendar"]
        rating = item["rating"]
        identification = item["identification"]
        event_points = item["event's points"]
        in_game = item["in game"]
        opponents_list = item["list of opponents"]
        player = modl.Players(first_name, last_name, birth_date, gendar, rating)
        player.event_points = event_points
        player.in_game = in_game
        player.identification = identification
        player.opponents_list = opponents_list
    return players_db


def tournaments_loading():
    """ load tournaments saving in a json file,
        and create an object of the class Tournaments
        for each tournament
        participants for each tournament are loaded
        by a list of players's identification
        :return: tournaments_db, json file open with tinydb
    """
    tournaments_db = TinyDB('chess_tournaments.json')
    for item in tournaments_db:
        name = item["name"]
        place = item["place"]
        date = item["date"]
        beginning_hour = item["beginning hour"]
        time_controller = item["time controller"]
        total_of_rounds = item["total of rounds"]
        number_of_participants = item["number of participants"]
        description = item["description"]
        in_game = item["in game boolean"]
        identification = item["identification"]
        identifications_list = item["players's identification"]
        tournament = modl.Tournaments(name, place, date, beginning_hour, time_controller)
        tournament.total_of_rounds = total_of_rounds
        tournament.number_of_participants = number_of_participants
        tournament.description = description
        tournament.identification = identification
        tournament.in_game = in_game
        for identification in identifications_list:
            for player in modl.Players.players_list:
                if player.identification == identification:
                    tournament.participants.append(player)
    return tournaments_db


def rounds_loading():
    """ load rounds saving in a json file,
        and create an object of the class Rounds
        for each tournament
        games for each round are loaded
        by a list of dictionnaries with players's identification
        and scores of each player
        :return: tournaments_db, json file open with tinydb
    """
    rounds_db = TinyDB('chess_rounds.json')
    for item in rounds_db:
        starting_time = item["starting time"]
        finishing_time = item["finishing time"]
        in_game = item["in game"]
        tournament_affiliation = item["tournament's affiliation"]
        games_for_db = item["games in the round"]
        identification = item["identification"]
        for tournament in modl.Tournaments.tournaments_list:
            if tournament.identification == tournament_affiliation:
                the_tournament = tournament
        the_round = modl.Rounds(the_tournament.participants, starting_time)
        the_round.finishing_time = finishing_time
        the_round.in_game = in_game
        the_round.tournament_affiliation = tournament_affiliation
        the_round.identification = identification
        for game in games_for_db:
            for player in the_round.participants:
                if player.identification == game[0]:
                    player1 = player
                    score1 = game[2]
                elif player.identification == game[1]:
                    player2 = player
                    score2 = game[3]
            dico = {'opponents': [player1, player2], 'score': [score1, score2]}
            the_round.games.append(dico)
        the_tournament.rounds.append(the_round)
    return rounds_db


# MENUS
def page_1(players_db, tournaments_db, rounds_db):
    """ display the main menu,
    input a choice and launch a function
    page 1 is the main page
    page 2 is the tournament's page
    page 3 is the statistiques's page
    :return: the_page and choice (types: int)
    """
    choice = "choix ?"
    choice_list = [1, 2, 3, 4, 5, 0]
    while choice not in choice_list:
        choice = view.home_page()
        if choice.isdigit():
            choice = int(choice)
        else:
            choice = "choix ?"
    if choice == 1:
        the_page = tournament_creation(tournaments_db, players_db)
    elif choice == 2:
        the_page = tournament_menu()
    elif choice == 3:
        player = player_creation(players_db)
        text = f"Le joueur au nom de {player.last_name} a bien été crée"
        view.information_message(text)
        the_page = 1
    elif choice == 4:
        rating_update(players_db)
        the_page = 1
    elif choice == 5:
        the_page = 3
    elif choice == 0:
        the_page = 1
    return the_page, choice


def page_2(players_db, tournaments_db, rounds_db):
    """ affiche le menu du tournoi,
    demande à l'utilisateur de choisir une option,
    et exécute une instruction en fonction de l'option choisie
    :return: the_page (type: int)
    page 1 is the main page
    page 2 is the tournament's page
    page 3 is the statistiques"s page
    :return: the_page and choice type int
    """
    choice = "choix ?"
    choice_list = [1, 2, 3, 4, 5, 6, 0]
    while choice not in choice_list:
        choice = view.tournament_page()
        if choice.isdigit():
            choice = int(choice)
        else:
            choice = 0
    if choice == 1:
        tournament = modl.Tournaments.tournaments_list[-1]
        if tournament.rounds == []:
            first_round(tournament.participants, tournament, players_db, tournaments_db, rounds_db)
            the_page = 2
        else:
            new_round(tournament.participants, tournament, players_db, rounds_db)
            the_page = 2
    elif choice == 2:
        tournament = modl.Tournaments.tournaments_list[-1]
        matchs_informations(tournament)
        the_page = 2
    elif choice == 3:
        tournament = modl.Tournaments.tournaments_list[-1]
        enter_results(tournament, players_db, tournaments_db, rounds_db)
        the_page = 2
    elif choice == 4:
        tournament = modl.Tournaments.tournaments_list[-1]
        tournament_rankings(tournament)
        the_page = 2
    elif choice == 5:
        the_page = 3
    elif choice == 6:
        the_page = 1
    elif choice == 0:
        the_page = 1
    return the_page, choice


def page_3(players_db, tournaments_db, rounds_db):
    """affiche le menu statistiques,
        demande à l'utilisateur de choisir une option,
        et exécute une instruction en fonction de l'option choisie
        :return: the_page (type: int)
        page 1 is the main page
        page 2 is the tournament's page
        page 3 is the statistiques's page
        :return: the_page and choice type int
        """
    choice = "choix ?"
    choice_list = [1, 2, 3, 4, 0]
    while choice not in choice_list:
        choice = view.stat_page()
        if choice.isdigit():
            choice = int(choice)
        else:
            choice = 0
    if choice == 1:
        players_view_informations()
        the_page = 3
    elif choice == 2:
        tournaments_view_informations()
        the_page = 3
    elif choice == 3:
        the_page = tournament_menu()
    elif choice == 4:
        the_page = 1
    elif choice == 0:
        the_page = 1
    return the_page, choice


# JOUEURS
def player_creation(players_db):
    """ input attributes for a new player
    add a player, object of the class Players
    save the player in the data file
    :return: the_page for the menu, type int
    """
    first_name, last_name, birth_date, gendar, rating = new_player()
    player = modl.Players(first_name, last_name, birth_date, gendar, rating)
    players_db.insert(player.serialize())
    return player


def players_view_informations():
    """ input choice for viewing informations
    run a function which sort the player's list
    display the player's list in the order
    :return: the_page, for menu, type: int
    """
    choice = view.players_menu()
    if choice == 1:

        the_list = modl.Players.players_alphabetical_order()
        view.players_view(the_list, choice)
    elif choice == 2:
        the_list = modl.Players.players_by_rating(modl.Players.players_list)
        view.players_view(the_list, choice)


def new_player():
    """ create a new player, input differents informations about him
    :return: first_name,last_name,birth_date,gendar,rating for the new player
    """
    view.text_area_display("Création d'un nouveau joueur:")
    first_name = "0"
    while not first_name.isalpha():
        view.text_area_display("Entrez le prénom du joueur:\n")
        first_name = input()
    last_name = "0"
    while not last_name.isalpha():
        view.text_area_display("Entrez le nom du joueur:\n")
        last_name = input()
    verification = False
    while not verification:
        text = "Entrez la date de naissance du joueur, " + \
               "au format jj/mm/aaaa, par exemple 03/10/1983 \n"
        view.text_area_display(text)
        birth_date = input()
        verification = date_check(birth_date)
    gendar = "0"
    while gendar.lower() not in ["f", "h"]:
        view.text_area_display("Entrez H pour homme et F pour femme:\n")
        gendar = input()
    rating = player_rating()
    return first_name, last_name, birth_date, gendar, rating


def player_rating():
    """ input rating for a player
    :return: the_rating, type: float
    """
    view.text_area_display("Entrez le classement du joueur (nombre positif)")
    verification = False
    while not verification:
        the_rating = input()
        try:
            the_rating = int(the_rating)
            if the_rating >= 0:
                verification = True
        except ValueError:
            text = "Merci d'entrer un nombre positif pour le classement.\n"
            view.information_message(text)
    return the_rating


def rating_update(players_db):
    """ update a players's rating """
    players_list = modl.Players.players_list
    if players_list == []:
        text = "Il n'y a aucun joueur enregistré pour le moment."
        view.information_message(text)
    else:
        text = "Tapez le nom d'un joueur " + \
               "ou bien tapez 0 pour voir la liste des joueurs"
        view.text_area_display(text)
        the_name = input()
        indice = compare_players_name(players_list, the_name)
        if type(indice) == int:
            player = players_list[indice]
            player.new_rating()
            player.db_update(players_db, "rating")
        else:
            view.players_view(players_list, 3)
            text = "Entrez le numéro devant le joueur " + \
                   "pour modifier son classement ou sinon appuyez sur Entrée"
            view.text_area_display(text)
            player_choosen = input()
            try:
                player_choosen = int(player_choosen)
                if 0 <= player_choosen < len(players_list):
                    player = players_list[player_choosen]
                    player.new_rating()
                    player.db_update(players_db, "rating")
                else:
                    text = "Cet identifiant ne correspond à aucun joueur."
                    view.information_message(text)
                    view.information_message("Retour au menu principal.\n")
            except ValueError:
                view.information_message("Retour au menu principal.\n")


def compare_players_name(players_list, a_name):
    """look at players_list to find a name,
    display all names found,
    input which player is available
    :return: indice, type int or 'nothing' if none
    """
    indices_list = []
    players_suggestion = []
    i = 0
    for player in players_list:
        if player.last_name == a_name:
            text = "Numéro " + str(i) + "\n" + player.display()
            view.text_area_display(text)
            players_suggestion.append(player)
            indices_list.append(i)
        i += 1
    if len(indices_list) > 0:
        indice = select_player(players_suggestion)
        if indice not in indices_list:
            indice = "nothing"
        else:
            return indice
    else:
        text = "Aucun joueur avec ce nom n'est enregistré pour le moment:"
        view.information_message(text)
        text = "Il faut entrer les données du nouveau joueur:"
        view.information_message(text)
        indice = "nothing"
    return indice


def select_player(players_list):
    text = "Voici la liste des joueurs enregistrés:\n" + \
           "entrez le numéro devant le joueur pour l'ajouter au tournoi,\n" + \
           "ou sinon appuyez sur Entrée pour créer un nouveau joueur"
    view.text_area_display(text)
    player_choosen = input()
    try:
        indice = int(player_choosen)
        return indice
    except ValueError:
        indice = "nothing"
        return indice


# TOURNOIS
def tournament_creation(tournaments_db, players_db):
    """ to create a new tournament,
    run the function new_tournament(),
    which input informations about a new tournament
    input player's name for the new tournament,
    add a new tournament, object of the class Tournaments
    :return: the_page, for the menu, type: int
    """
    if modl.Tournaments.tournaments_list != []:
        length = len(modl.Tournaments.tournaments_list) - 1
        actual_tournament = modl.Tournaments.tournaments_list[length]
        condition = actual_tournament.in_game
    else:
        condition = False
    if not condition:
        name, place, date, begin_hour, \
            total_participants, total_rounds, time_control, \
            description = new_tournament()
        tournament = modl.Tournaments(name, place, date, begin_hour, time_control)
        tournament.total_of_rounds = total_rounds
        tournament.number_of_participants = total_participants
        tournament.description = description
        tournament_players = players_in_tournament(modl.Players.players_list, players_db, total_participants)
        tournament.participants = modl.Players.players_by_rating(tournament_players)
        tournaments_db.insert(tournament.serialize())
        for player in tournament_players:
            player.opponents_list = []
            player.event_points = 0.0
            player.db_update(players_db, "event's points")
            player.db_update(players_db, "list of opponents")
        the_page = 2
        return the_page
    else:
        text = "Il faut clore le tournoi en cours " + \
                "avant de lancer un nouveau tournoi !"
        view.information_message(text)
        the_page = 1
        return the_page


def new_tournament():
    """ run functions which input informations about a new tournament
    :return: the_name, the_place, the_date,
                total_of_rounds, time_controller, tournament_players,
                description
    """
    view.text_area_display("Création d'un nouveau tournoi:")
    name = tournament_name()
    place = tournament_place()
    date = tournament_date()
    begin_hour = tournament_hour()
    number_of_participants = tournament_participants_number()
    total_rounds = tournament_rounds_number(number_of_participants)
    time_controller = tournament_time_type()
    description = tournament_description_update()
    return name, place, date, begin_hour, \
        number_of_participants, total_rounds, time_controller, description


def tournament_name():
    """ input the name of a tournament,
       :return: the_name, type string with letters and some special characters
    """
    verification = False
    while not verification:
        the_name = input("Entrez le nom du tournoi:\n")
        result = re.match(r"^[\w\sçéèùê]+$", the_name)
        if (result) and (len(the_name) <= 100):
            verification = True
    return the_name


def tournament_place():
    """input the place of a tournament
       :return: the_place, type string with letters and some special characters
    """
    verification = False
    while not verification:
        the_place = input("Entrez le lieu du tournoi:\n")
        result = re.match(r"^[\w\sçéèùê]+$", the_place)
        if result and len(the_place) <= 100:
            verification = True
    return the_place


def tournament_date():
    """input the date for a tournament
       :return: the_date, a string in dd/mm/yyyy format
    """
    verification = False
    while not verification:
        text = "Entrez la date de début du tournoi, au format " + \
               "jj/mm/aaaa, par exemple 03/10/2013\n"
        view.text_area_display(text)
        the_date = input()
        verification = date_check(the_date)
    return the_date


def tournament_hour():
    """input hour and minutes for a tournament
       :return: the_hour, a string in hh:mm format"""
    verification = False
    while not verification:
        text = "Entrez l'horaire de début du tournoi, " + \
               "au format hh:mm ou hhmm, par exemple 09:35 " + \
               "pour 9 heures 35 minutes " + \
               "ou 18:02 pour 6 heures 2 minutes l'après midi"
        view.text_area_display(text)
        the_hour = input()
        verification = time_check(the_hour)
    return the_hour


def tournament_participants_number():
    """ input the number of participants for the tournament
        :return: total_of_participants, type int
    """
    verification = False
    while not verification:
        text = "Indiquez le nombre de participants pour ce tournoi, " + \
               "ou tapez directement sur Entrée pour laisser 8 par défaut"
        view.text_area_display(text)
        total_of_participants = input()
        if total_of_participants.isdigit():
            if int(total_of_participants) < 2:
                text = "Il faut au moins 2 joueurs pour faire un tournoi"
                view.information_message(text)
            elif int(total_of_participants) % 2 != 0:
                text = "Merci d'entrer un nombre pair de joueurs " + \
                       "pour créer le tournoi"
                view.information_message(text)
            else:
                verification = True
        else:
            total_of_participants = 8
            verification = True
    total_of_participants = int(total_of_participants)
    return total_of_participants


def tournament_rounds_number(total_of_participants):
    """ input the round's number for a tournament
       :return: total_of_rounds, type int"""
    verification = False
    while not verification:
        text = "Indiquez le nombre de rounds pour ce tournoi, " + \
               "ou tapez directement sur Entrée pour laisser 4 par défaut:\n"
        view.text_area_display(text)
        total_of_rounds = input()
        if total_of_rounds.isdigit():
            if 0 < int(total_of_rounds) < total_of_participants:
                verification = True
            else:
                text = "Le nombre de rounds doit être strictement positif " + \
                       "et strictement inférieur au nombre de participants"
                view.information_message(text)
        elif total_of_rounds == "":
            verification = True
            total_of_rounds = 4
    total_of_rounds = int(total_of_rounds)
    return total_of_rounds


def tournament_time_type():
    """ input the time controller for a tournament
       :return: the string 'Blitz', 'Bullet' or 'Speed' """
    verification = False
    while not verification:
        text = "Indiquez le type de contrôle du temps:\n" + \
               "1 pour Blitz\n2 pour Bullet\n3 pour Speed\n"
        view.text_area_display(text)
        time_controller = input()
        if time_controller == "1":
            time_controller = "Blitz"
            verification = True
        elif time_controller == "2":
            time_controller = "Bullet"
            verification = True
        elif time_controller == "3":
            time_controller = "Speed"
            verification = True
    return time_controller


def players_in_tournament(players_list, players_db, number_of_participants=8):
    """ enter names and informations of players in the tournament,
    players_list is from the class Players
    :return: tournament_players, a list of players from the class Players
    """
    tournament_players = []
    for n in range(number_of_participants):
        text = "Entrez le nom de famille du joueur " + str(n+1)
        view.text_area_display(text)
        the_name = input()
        if players_list is not None:
            indice = compare_players_name(players_list, the_name)
            if type(indice) == int:
                tournament_players.append(players_list[indice])
                the_name = players_list[indice].last_name
                text = f"Le joueur au nom de {the_name} a bien été ajouté"
                view.information_message(text)
            else:
                view.players_view(players_list, 3)
                indice = select_player(players_list)
                if type(indice) == int:
                    tournament_players.append(players_list[indice])
                    the_name = players_list[indice].last_name
                    text = f"Le joueur au nom de {the_name} a bien été ajouté"
                    view.information_message(text)
                else:
                    player = player_creation(players_db)
                    tournament_players.append(player)
        else:
            player = player_creation(players_db)
            tournament_players.append(player)
    return tournament_players


def tournament_description_update():
    view.text_area_display("Vous pouvez ajouter une description au tournoi,")
    view.text_area_display("ou sinon tapez sur Entrée:")
    description = input()
    return description


def tournament_menu():
    """ display the tournament's menu, if possible
    :return: the_page, type: int
    """
    if len(modl.Tournaments.tournaments_list) > 0:
        the_page = 2
        return the_page
    else:
        text = "Il n'y a aucun tournoi de crée pour le moment...\n"
        view.information_message(text)
        the_page = 1
        return the_page


def tournaments_view_informations():
    """ input which tournament must be showing
    and display information about a tournament
    :return: the_page, for the menu, type: int
    """
    tournaments_list = modl.Tournaments.tournaments_list
    if tournaments_list == []:
        text = "Il n'y a aucun tournoi à afficher pour le moment."
        view.information_message(text)
    else:
        i = 0
        for tournament in tournaments_list:
            view.information_message("numéro " + str(i) + ":")
            view.information_message(tournament.display() + "\n")
            i += 1
        list_length = len(tournaments_list)
        indice = tournament_choose(list_length)
        if type(indice) == int:
            tournament = tournaments_list[indice]
            tournament_rankings(tournament)
            rounds_information(tournament)


def tournament_choose(list_length):
    """input a tournament's number,
    for showing the rounds
    :return: indice, type int or the string "nothing"
    """
    text = "Entrez le numéro du tournoi pour afficher la liste des joueurs" + \
           " et la liste des rondes" + \
           "avec les matchs du tournoi,\n" + \
           "ou bien appuyez sur la touche Entrée pour revenir au menu"
    view.text_area_display(text)
    tournament_choosen = input()
    try:
        tournament_choosen = int(tournament_choosen)
        if 0 <= tournament_choosen < list_length:
            indice = tournament_choosen
            return indice
        else:
            indice = "nothing"
            return indice
    except ValueError:
        indice = "nothing"
        return indice


def rounds_information(a_tournament):
    """ show all rounds in a tournament
    """
    i = 1
    for a_round in a_tournament.rounds:
        view.information_message("Ronde numéro " + str(i))
        view.information_message(a_round.display())
        i += 1


def tournament_ending(a_tournament):
    """ input a date and an hour for the end of the last round,
    and display the final players's ranking in teh tournament
    :return: the_page, type: int
    """
    a_tournament.in_game = False
    view.information_message("Le tournoi est maintenant terminé.")
    view.information_message("Voici les résultats:\n")
    tournament_rankings(a_tournament)


def tournament_rankings(a_tournament):
    """ display players's ranking for an actual tournament
    :return the_page, type: int
    """
    players_list = a_tournament.participants
    players_list = modl.Players.players_classify_in_tournament(players_list)
    view.players_view(players_list, 2)


# ROUNDS
def first_round(players_list, a_tournament, players_db, tournaments_db, rounds_db,):
    """ input date and time for the first round,
        order players by rating,
        and create matchs for the round
        :return: the_page, type: int
    """
    view.text_area_display("Entrer la date du nouveau round:")
    round_date = input("? ")
    view.text_area_display("Entrer l'horaire de début du nouveau round")
    round_starting_time = input("? ")
    time1 = {'date': round_date, 'hour': round_starting_time}
    players_in_round = modl.Players.players_by_rating(players_list)
    first_round = modl.Rounds(players_in_round, time1)
    a_tournament.rounds.append(first_round)
    a_tournament.in_game = True
    first_round.games = first_round.first_round_matchs_creation()
    first_round.in_game = True
    first_round.tournament_affiliation = a_tournament.identification
    rounds_db.insert(first_round.serialize())
    a_tournament.db_update(tournaments_db, "in game boolean")
    for player in first_round.participants:
        player.db_update(players_db, "list of opponents")
        player.db_update(players_db, "in game")
    view.information_message(first_round.display())


def new_round(players_list, a_tournament, players_db, rounds_db):
    """ input date and time for a round,
        order players by ranking in the tournament,
        and create matchs for the round
        :return: the_page, type: int
    """
    previous_round = a_tournament.rounds[-1]
    if len(a_tournament.rounds) >= a_tournament.total_of_rounds:
        text = "Le tournoi est terminé, tous les rounds ont déjà été joués"
        view.information_message(text)
    elif previous_round.in_game:
        text = "Le round en cours n'est pas encore terminé, " + \
                "il faut entrer tous les scores d'abord"
        view.information_message(text)
    else:
        view.text_area_display("Creation d'un nouveau round: \n")
        view.text_area_display("Entrer la date du nouveau round:")
        round_date = input("? ")
        view.text_area_display("Entrer l'horaire de début du nouveau round")
        round_starting_time = input("? ")
        time1 = {'date': round_date, 'hour': round_starting_time}
        players_in_round = modl.Players.players_classify_in_tournament(players_list)
        new_round = modl.Rounds(players_in_round, time1)
        a_tournament.rounds.append(new_round)
        new_round.games = new_round.matchs_creation()
        new_round.in_game = True
        new_round.tournament_affiliation = a_tournament.identification
        rounds_db.insert(new_round.serialize())
        for player in new_round.participants:
            player.db_update(players_db, "list of opponents")
            player.db_update(players_db, "in game")
        view.information_message(new_round.display())


def matchs_informations(a_tournament):
    """ show actual matchs and say if they are done or not
        :return: the_page, type: int
    """
    if a_tournament.rounds == []:
        view.information_message("Le premier round n'a pas encore été crée")
    else:
        actual_round = a_tournament.rounds[-1]
        round_number = len(a_tournament.rounds) + 1
        view.information_message("Round numéro " + str(round_number))
        view.information_message(actual_round.display())
        if actual_round.in_game:
            text = "Les matchs de ce round sont en cours, " + \
                   "scores non enregistrés"
            view.text_area_display(text)
        else:
            text = "Ce round est fini, les scores ont été enregistrés"
            view.text_area_display(text)


def enter_results(a_tournament, players_db, tournaments_db, rounds_db):
    if a_tournament.rounds == []:
        view.information_message("Le premier round n'a pas encore été crée...")
    elif not a_tournament.rounds[-1].in_game:
        view.information_message("Les résultats ont déjà été entrés.")
    else:
        actual_round = a_tournament.rounds[-1]
        text = "Entrez les résultats pour le match,\n" + \
               "sous la forme 0 puis 1 ou 1 puis 0 en cas de vainqueur, \n" + \
               "ou bien 0.5 pour chaque joueur en cas de nul. \n" + \
               "Vous pouvez marquer 0 à chacun " + \
               "pour passer au match suivant,\n" + \
               "sans entrer de résultat."
        view.text_area_display(text)
        actual_round.new_results()
        actual_round.in_game = False
        verification = False
        while not verification:
            text = "Entrez la date de fin du round, au format jj/mm/aaaa, " + \
                   "par exemple 03/10/2013 \n"
            view.text_area_display(text)
            the_date = input()
            verification = date_check(the_date)
        actual_round.finishing_time['date'] = the_date
        verification = False
        while not verification:
            text = "Entrez l'horaire de fin du round, " + \
                    "au format hh:mm ou hhmm, " + \
                    "par exemple 09:35 pour 9 heures 35 minutes, " + \
                    "ou 18:02 pour 6 heures 2 minutes l'après midi:"
            view.text_area_display(text)
            the_hour = input()
            verification = time_check(the_hour)
        actual_round.finishing_time['hour'] = the_hour
        actual_round.db_games_update(rounds_db)
        actual_round.db_update(rounds_db, "in game")
        actual_round.db_update(rounds_db, "finishing time")
        for player in actual_round.participants:
            player.db_update(players_db, "event's points")
            player.db_update(players_db, "in game")
        text = "Voulez pouvez laisser ici un commentaire pour ce round ?" + \
               "\nou sinon tapez sur la touche Entrée pour continuer" + \
               " sans compléter la description"
        view.text_area_display(text)
        new_description = input()
        if new_description != "":
            a_tournament.description = a_tournament.description + "\n" + new_description
            a_tournament.db_update(tournaments_db, "description")
        if len(a_tournament.rounds) == a_tournament.total_of_rounds:
            tournament_ending(a_tournament)
            a_tournament.db_update(tournaments_db, "in game boolean")


# Verifications
def date_check(a_date):
    """ check the format of a date
    :return: date_test, a boolean
    """
    date_test = False
    result = re.match(r"^[0123]{1}\d{1}/[01]{1}\d{1}/\d{4}$", a_date)
    if result:
        date_test = True
        decomposition = a_date.split("/")
        day = int(decomposition[0])
        month = int(decomposition[1])
        year = int(decomposition[2])
        cond1 = day < 1 or day > 31
        cond2 = month < 1 or month > 12
        short_months = [2, 4, 6, 9, 11]
        cond3 = (day == 31) and (month in short_months)
        cond4 = (day == 30) and (month == 2)
        cond5 = year < 1900
        if cond1 or cond2 or cond3 or cond4:
            date_test = False
        elif cond5:
            view.information_message("It seems to be very old, no ?")
            date_test = False
        elif day == 29 and month == 2:
            date_test = bisextile_checking(year)
    return date_test


def bisextile_checking(a_year):
    """check if a year is a bisextile year
    :return: verification, a boolean
    """
    verification = False
    if (a_year % 400 == 0) or (a_year % 4 == 0 and a_year % 100 != 0):
        verification = True
    else:
        view.information_message("Ce n'est pas une année bixectile...")
    return verification


def time_check(a_string):
    """ check the time's format hh:mm
    :return: verification, a boolean
    """
    verification = False
    the_time = a_string.replace(":", "")
    if len(the_time) == 4 and the_time.isdigit():
        hours = int(the_time[0] + the_time[1])
        minutes = int(the_time[2] + the_time[3])
        if 0 <= hours <= 24 and 0 <= minutes <= 60:
            verification = True
    return verification


def main():
    """ fonction principale: gère le passage d'une page à l'autre
    avec une boucle qui stop si the_page = 1 et choice = 6
    :return: message indiquant la fermeture du programme, le cas échéant
    """
    players_db = players_loading()
    tournaments_db = tournaments_loading()
    rounds_db = rounds_loading()
    page = 1
    app_stop = "quit ?"
    while app_stop != 0:
        if page == 1:
            page, app_stop = page_1(players_db, tournaments_db, rounds_db)
        elif page == 2:
            page, app_stop = page_2(players_db, tournaments_db, rounds_db)
        elif page == 3:
            page, app_stop = page_3(players_db, tournaments_db, rounds_db)
    text = "\n Le programme est désormais fermé. Bonne journée à vous."
    return view.information_message(text)


if __name__ == "__main__":
    main()
