import views.ct_views as view
import models.ct_models as modl


import re
from tinydb import TinyDB, Query


def players_loading():
    """ load players saving in a json file,
        and create an object of the class Players
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
        player = modl.Players(first_name, last_name, birth_date, gendar)
        player.event_points = event_points
        player.rating = rating
        player.in_game = in_game
        player.identification = identification
    return players_db


def tournaments_loading():
    """ load tournaments saving in a json file,
        and create an object of the class Tournaments
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
            the_round.games.append({'opponents': [player1, player2], 'score': [score1, score2]})
        the_tournament.rounds.append(the_round)
    return rounds_db


# MENUS
def page_1(players_db, tournaments_db, rounds_db):
    """ affiche le menu principal,
    demande à l'utilisateur de choisir une option,
    et exécute une instruction en fonction de l'option choisie
    :return: the_page et choice (types: int)
    page 1 is the main page
    page 2 is the tournament's page
    page 3 is the statistiques"s page
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
        the_page = player_creation_menu(players_db)
    elif choice == 4:
        the_page = rating_update(players_db)
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
            the_page = first_round(tournament.participants, tournament, rounds_db)
        else:
            the_page = new_round(tournament.participants, tournament, rounds_db)
    elif choice == 2:
        tournament = modl.Tournaments.tournaments_list[-1]
        the_page = matchs_informations(tournament)
    elif choice == 3:
        tournament = modl.Tournaments.tournaments_list[-1]
        if tournament.rounds == []:
            print("Le premier round n'a pas encore été crée...")
            the_page = 2
        elif not tournament.rounds[-1].in_game:
            print("Les résultats ont déjà été entrés.")
            the_page = 2
        else:
            actual_round = tournament.rounds[-1]
            actual_round.new_results()
            print("Entrer la date de fin du round:")
            round_date = input("? ")
            actual_round.finishing_time['date'] = round_date
            print("Entrer l'horaire de fin de ce round")
            round_hour = input("? ")
            actual_round.finishing_time['hour'] = round_hour
            if len(tournament.rounds) == tournament.total_of_rounds:
                tournament_ending(actual_round, tournament)
            the_page = 2
    elif choice == 4:
        tournament = modl.Tournaments.tournaments_list[-1]
        the_page = tournament_rankings(tournament)
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
        the_page = players_view_informations()
    elif choice == 2:
        the_page = tournaments_view_informations()
    elif choice == 3:
        the_page = tournament_menu()
    elif choice == 4:
        the_page = 1
    elif choice == 0:
        the_page = 1
    return the_page, choice


# JOUEURS
def player_creation_menu(players_db):
    """ input attributes for a new player
    add a player, object of the class Players
    save the player in the data file
    :return: the_page for the menu, type int
    """
    first_name, last_name, birth_date, gendar, rating = player_creation()
    player = modl.Players(first_name, last_name, birth_date, gendar)
    player.rating = rating
    players_db.insert(player.serialize())
    the_page = 1
    return the_page


def players_db_rating_update(a_player, players_db, new_rating):
    """ modify informations saving in the database
    :return: ...
    """
    players_datas = Query()
    return players_db.update({"rating": new_rating},
                             players_datas.identification == a_player.identification)


def players_view_informations():
    """ input choice for viewing informations
    run a function which sort the player's list
    display the player's list in the order
    :return: the_page, for menu, type: int
    """
    choice = view.players_menu()
    if choice == 1:
        the_list = modl.Players.players_alphabetical_order()
        if the_list == []:
            print("Il n'y a aucun joueur à afficher pour le moment.")
        else:
            for player in the_list:
                player.display()
    elif choice == 2:
        print("Liste de tous les joueurs enregistrés dans l'ordre de leur classement:")
        the_list = modl.Players.players_by_rating(modl.Players.players_list)
        if the_list == []:
            print("Il n'y a aucun joueur à afficher pour le moment.")
        else:
            for player in the_list:
                player.display()
    the_page = 3
    return the_page


def player_creation():
    """ create a new player, input differents informations about him
    :return: first_name,last_name,birth_date,gendar,rating for the new player
    """
    print("Création d'un nouveau joueur:")
    first_name = "0"
    while not first_name.isalpha():
        first_name = input("Entrez le prénom du joueur:\n")
    last_name = "0"
    while not last_name.isalpha():
        last_name = input("Entrez le nom du joueur:\n")
    verification = False
    while not verification:
        print("Entrez la date de naissance du joueur,",
              "au format jj/mm/aaaa, par exemple 03/10/1983 \n")
        birth_date = input()
        verification = date_check(birth_date)
    gendar = "0"
    while gendar.lower() not in ["f", "h"]:
        gendar = input("Entrez H pour homme et F pour femme:\n")
    rating = player_rating()
    return first_name, last_name, birth_date, gendar, rating


def player_rating():
    """ input rating for a player
    :return: the_rating, type: float
    """
    print("Entrez le classement du joueur (nombre positif)")
    verification = False
    while not verification:
        the_rating = input()
        try:
            the_rating = int(the_rating)
            if the_rating >= 0:
                verification = True
        except ValueError:
            print("Merci d'entrer un nombre positif pour le classement.\n")
    return the_rating


def rating_update(players_db):
    """ update a players's rating
    :return: the_page, for menu, type: int
    """
    players_list = modl.Players.players_list
    if players_list == []:
        print("Il n'y a aucun joueur enregistré pour le moment.")
    else:
        print("Tapez le nom d'un joueur ou bien tapez 0 pour voir la liste des joueurs")
        the_name = input()
        indice = compare_players_name(players_list, the_name)
        if type(indice) == int:
            player = players_list[indice]
            player.new_rating()
            players_db.insert(player.serialize())
        else:
            i = 0
            for player in players_list:
                print("Numéro", i)
                player.display()
                i += 1
            print("Entrez le numéro devant le joueur pour modifier son classement",
                  "et sinon appuyez sur Entrée")
            player_choosen = input()
            try:
                player_choosen = int(player_choosen)
                if 0 <= player_choosen < len(players_list):
                    player = players_list[player_choosen]
                    new_rating = player.new_rating()
                    players_db_rating_update(player, players_db, new_rating)
                else:
                    print("Cet identifiant ne correspond à aucun joueur.")
                    print("Retour au menu principal.\n")
            except ValueError:
                print("Retour au menu principal.\n")
    the_page = 1
    return the_page


def compare_players_name(players_list, a_name):
    indices_list = []
    i = 0
    for player in players_list:
        if player.last_name == a_name:
            print("\nNuméro", i)
            player.display()
            indices_list.append(i)
        i += 1
    if len(indices_list) > 0:
        print("Si le joueur est dans la liste ci-dessus, ",
              "entrez le numéro devant le joueur pour l'ajouter au tournoi,\n",
              "et sinon appuyez sur Entrée")
        player_choosen = input()
        try:
            player_choosen = int(player_choosen)
            if player_choosen in indices_list:
                return player_choosen
            else:
                indice = "nothing"
                return indice
        except ValueError:
            indice = "nothing"
            return indice
    else:
        print("Aucun joueur avec ce nom n'est enregistré pour le moment:")
        print("Il faut entrer les données du nouveau joueur:")
        indice = "nothing"
        return indice


def select_player(players_list):
    i = 0
    for player in players_list:
        print("\nNuméro", i)
        player.display()
        i += 1
    print("Voici la liste des joueurs enregistrés:",
          "entrez le numéro devant le joueur pour l'ajouter au tournoi,\n",
          "et sinon appuyez sur Entrée pour créer un nouveau joueur")
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
    run the function new_tournament() which input informations about a new tournament
    input player's name for the new tournament,
    add a new tournament, object of the class Tournaments
    :return: the_page, for the menu, type: int
    """
    if modl.Tournaments.tournaments_list != []:
        list_length = len(modl.Tournaments.tournaments_list)
        actual_tournament = modl.Tournaments.tournaments_list[list_length - 1]
        condition = actual_tournament.in_game
    else:
        condition = False
    if not condition:
        name, place, date, begin_hour, total_participants, total_rounds, time_control, description = new_tournament()
        tournament = modl.Tournaments(name, place, date, begin_hour, time_control)
        tournament.total_of_rounds = total_rounds
        tournament.number_of_participants = total_participants
        tournament.description = description
        tournament_players = players_in_tournament(modl.Players.players_list,
        players_db, tournament.number_of_participants)
        tournament.participants = modl.Players.players_by_rating(tournament_players)
        tournaments_db.insert(tournament.serialize())
        the_page = 2
        return the_page
    else:
        print("Il faut clore le tournoi en cours",
              " avant de lancer un nouveau tournoi !")
        the_page = 1
        return the_page


def new_tournament():
    """ run functions which input informations about a new tournament
    :return: the_name, the_place, the_date,
                total_of_rounds, time_controller, tournament_players,
                description
    """
    print("Création d'un nouveau tournoi:")
    name = tournament_name()
    place = tournament_place()
    date = tournament_date()
    begin_hour = tournament_hour()
    number_of_participants = tournament_participants_number()
    total_rounds = tournament_rounds_number(number_of_participants)
    time_controller = tournament_time_type()
    description = ""
    return name, place, date, begin_hour, number_of_participants, total_rounds, time_controller, description


def tournament_name():
    """ input the name of a tournament,
       :return: the_name, type string with letters and some special characters"""
    verification = False
    while not verification:
        the_name = input("Entrez le nom du tournoi:\n")
        result = re.match(r"^[\w\sçéèùê]+$", the_name)
        if (result) and (len(the_name) <= 100):
            verification = True
    return the_name


def tournament_place():
    """input the place of a tournament
       :return: the_place, type string with letters and some special characters"""
    verification = False
    while not verification:
        the_place = input("Entrez le lieu du tournoi:\n")
        result = re.match(r"^[\w\sçéèùê]+$", the_place)
        if result and len(the_place) <= 100:
            verification = True
    return the_place


def tournament_date():
    """input the date for a tournament
       :return: the_date, a string in dd/mm/yyyy format"""
    verification = False
    while not verification:
        print("Entrez la date de début du tournoi,",
              "au format jj/mm/aaaa, par exemple 03/10/2013 \n")
        the_date = input()
        verification = date_check(the_date)
    return the_date


def tournament_hour():
    """input hour and minutes for a tournament
       :return: the_hour, a string in hh:mm format"""
    verification = False
    while not verification:
        print("Entrez l'horaire de début du tournoi,",
              "au format hh:mm ou hhmm, par exemple 09:35 pour 9 heures 35 minutes,",
              "ou 18:02 pour 6 heures 2 minutes l'après midi:")
        the_hour = input()
        verification = time_check(the_hour)
    return the_hour


def tournament_participants_number():
    """ input the number of participants for the tournament
        :return: total_of_participants, type int
    """
    verification = False
    while not verification:
        print("Indiquez le nombre de participants pour ce tournoi,",
              "ou tapez directement sur Entrée pour laisser 8 par défaut")
        total_of_participants = input()
        if total_of_participants.isdigit():
            if int(total_of_participants) < 2:
                print("Il faut au moins 2 joueurs pour faire un tournoi")
            elif int(total_of_participants) % 2 != 0:
                print("Merci d'entrer un nombre pair de joueurs pour créer le tournoi")
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
        print("Indiquez le nombre de rounds pour ce tournoi, ou tapez",
              " directement sur Entrée pour laisser 4 par défaut:\n")
        total_of_rounds = input()
        if total_of_rounds.isdigit():
            if int(total_of_rounds) < total_of_participants:
                verification = True
            else:
                print("Le nombre de matchs doit être",
                      "strictement inférieur au nombre de participants")
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
        print("Indiquez le type de contrôle du temps:\n",
              "1 pour Blitz\n 2 pour Bullet\n 3 pour Speed\n")
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


def tournament_menu():
    """ display the tournament's menu, if possible
    :return: the_page, type: int
    """
    if len(modl.Tournaments.tournaments_list) > 0:
        the_page = 2
        return the_page
    else:
        print("Il n'y a aucun tournoi de crée",
              " pour le moment...\n")
        the_page = 1
        return the_page


def players_in_tournament(players_list, players_db, number_of_participants=8):
    """ enter names and informations of players in the tournament,
    players_list is from the class Players
    :return: tournament_players, a list of players from the class Players
    """
    tournament_players = []
    for n in range(number_of_participants):
        print("Entrez le nom de famille du joueur ", n+1)
        the_name = input()
        if players_list is not None:
            indice = compare_players_name(players_list, the_name)
            if type(indice) == int:
                tournament_players.append(players_list[indice])
                the_name = players_list[indice].last_name
                print(f"Le joueur au nom de {the_name} a bien été ajouté")
            else:
                indice = select_player(players_list)
                if type(indice) == int:
                    tournament_players.append(players_list[indice])
                    the_name = players_list[indice].last_name
                    print(f"Le joueur au nom de {the_name} a bien été ajouté")
                else:
                    first_name, last_name, birth_date, gendar, rating = player_creation()
                    player = modl.Players(first_name, last_name, birth_date, gendar)
                    player.rating = rating
                    players_db.insert(player.serialize())
                    tournament_players.append(player)
        else:
            first_name, last_name, birth_date, gendar, rating = player_creation()
            player = modl.Players(first_name, last_name, birth_date, gendar)
            player.rating = rating
            players_db.insert(player.serialize())
            tournament_players.append(player)
    return tournament_players


def players_tournament_saving(a_player, players_tournament_db):
    """ create a dictionay with player's attributes
    :return: the new player is add to the data file
    """
    serialized_player = {"first name": a_player.first_name,
                         "last name": a_player.last_name,
                         "birth date": a_player.birth_date,
                         "gendar": a_player.gendar,
                         "rating": a_player.rating,
                         "event's points": a_player.event_points
                         }
    return players_tournament_db.insert(serialized_player)


def tournaments_view_informations():
    """ input which tournament must be showing
    and display information about a tournament
    :return: the_page, for the menu, type: int
    """
    tournaments_list = modl.Tournaments.tournaments_list
    if tournaments_list == []:
        print("Il n'y a aucun tournoi à afficher pour le moment.")
    else:
        i = 0
        for tournament in tournaments_list:
            print("numéro " + str(i) + ":")
            tournament.display()
        list_length = len(tournaments_list)
        indice = tournament_choose(list_length)
        if type(indice) == int:
            tournament = tournaments_list[indice]
            rounds_information(tournament)
    the_page = 3
    return the_page


def tournament_choose(list_length):
    """input a tournament's number,
    for showing the rounds
    :return: indice, type int or the string "nothing"
    """
    print("Entrez le numéro du tournoi pour afficher les rondes",
          "et les matchs du tournoi,\n",
          "ou bien appuyez sur la touche Entrée pour revenir au menu")
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
    for a_round in a_tournament.rounds:
        a_round.display()


def tournament_ending(a_round, a_tournament):
    """ input a date and an hour for the end of the last round,
    and display the final players's ranking in teh tournament
    :return: the_page, type: int
    """
    a_tournament.in_game = False
    print("Entrer la date de fin de ce dernier round:")
    round_finish_date = input("? ")
    print("Entrer l'horaire de fin de ce dernier round")
    round_finish_time = input("? ")
    a_round. finishing_time = {'date': round_finish_date, 'hour': round_finish_time}
    print("Le tournoi est maintenant terminé.")
    print("Voici les résultats:\n")
    the_page = tournament_rankings(a_tournament)
    return the_page


def tournament_rankings(a_tournament):
    """ display players's ranking for an actual tournament
    :return the_page, type: int
    """
    players_list = a_tournament.participants
    players_list = modl.Players.players_classify_in_tournament(players_list)
    i = 0
    for player in players_list:
        print(str(i) + ")")
        player.display()
        i += 1
    the_page = 2
    return the_page


# ROUNDS
def first_round(players_list, a_tournament, rounds_db):
    """ input date and time for the first round,
        order players by rating,
        and create matchs for the round
        :return: the_page, type: int
    """
    print("Entrer la date du nouveau round:")
    round_date = input("? ")
    print("Entrer l'horaire de début du nouveau round")
    round_starting_time = input("? ")
    time1 = {'date': round_date, 'hour': round_starting_time}
    players_in_round = modl.Players.players_by_rating(players_list)
    first_round = modl.Rounds(players_in_round, time1)
    a_tournament.rounds.append(first_round)
    a_tournament.in_game = True
    first_round.games = first_round.first_round_matchs_creation()
    first_round.in_game = True
    first_round.tournament_affiliation = a_tournament.identification
    round_saving(first_round, rounds_db)
    a_tournament.in_game = True
    first_round.display()
    the_page = 2
    return the_page


def new_round(players_list, a_tournament, rounds_db):
    """ input date and time for a round,
        order players by ranking in the tournament,
        and create matchs for the round
        :return: the_page, type: int
    """
    if len(a_tournament.rounds) < a_tournament.total_of_rounds:
        print("Creation d'un nouveau round.")
    else:
        print("Le tournoi est terminé, tous les rounds ont déjà été joués")
        the_page = 2
        return the_page
    previous_round = a_tournament.rounds[-1]
    if not previous_round.in_game:
        print("Entrer la date du nouveau round:")
        round_date = input("? ")
        print("Entrer l'horaire de début du nouveau round")
        round_starting_time = input("? ")
        time1 = {'date': round_date, 'hour': round_starting_time}
        players_in_round = modl.Players.players_classify_in_tournament(players_list)
        new_round = modl.Rounds(players_in_round, time1)
        a_tournament.rounds.append(new_round)
        new_round.games = new_round.matchs_creation()
        new_round.in_game = True
        new_round.tournament_affiliation = a_tournament.identification
        round_saving(new_round, rounds_db)
        new_round.display()
        for player in players_list:
            print(player.in_game)
    else:
        print("Le round en cours n'est pas encore terminé",
              "il faut entrer tous les scores d'abord")
    the_page = 2
    return the_page


def matchs_informations(a_tournament):
    """ show actual matchs and say if they are done or not
        :return: the_page, type: int
    """
    if a_tournament.rounds == []:
        print("Le premier round n'a pas encore été crée")
    else:
        actual_round = a_tournament.rounds[-1]
        actual_round.display()
        if actual_round.in_game:
            print("Les matchs de ce round sont en cours, scores non enregistrés")
        else:
            print("Ce round est fini, les scores ont été enregistrés")
    the_page = 2
    return the_page


def round_saving(a_round, rounds_db):
    """ create a dictionay with round's attributes
    :return: the new round is add to the data file
    """
    games_for_db = []
    for game in a_round.games:
        player1 = game['opponents'][0]
        player2 = game['opponents'][1]
        score1 = game['score'][0]
        score2 = game['score'][1]
        games_for_db.append([player1.identification, player2.identification, score1, score2])
    serialized_round = {"starting time": a_round.starting_time,
                        "finishing time": a_round.finishing_time,
                        "in game": a_round.in_game,
                        "tournament's affiliation": a_round.tournament_affiliation,
                        "games in the round": games_for_db,
                        "identification": a_round.identification}
    return rounds_db.insert(serialized_round)


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
        cond3 = year < 1900
        if cond1 or cond2:
            date_test = False
        elif cond3:
            print("It seem to be very old, no ?")
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
        print("Ce n'est pas une année bixectile...")
    return verification


def time_check(a_string):
    """ check the time's format hh:mm
    :return: verification, a boolean
    """
    verification = False
    a_string = a_string.replace(":", "")
    if len(a_string) == 4 and a_string.isdigit():
        hours = int(a_string[0] + a_string[1])
        minutes = int(a_string[2] + a_string[3])
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
    return print("\n Le programme est désormais fermé. Bonne journée à vous.")


if __name__ == "__main__":
    main()
