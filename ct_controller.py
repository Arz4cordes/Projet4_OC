""" user's actions:
    create a new tournament
    give matchs's results
    and datas check (format) """
import views.ct_views as view
import models.ct_models as modl


import re

########## ICI LE PROG PRINCIPAL PRECEDENT ##########

def page_1():
    """ affiche le menu principal,
        demande à l'utilisateur de choisir une option,
        et exécute une instruction en fonction de l'option choisie
        :return: the_page et choice (types: int)"""
    choice = 0
    choice_list = [1, 2, 3, 4, 5, 6]
    while choice not in choice_list:
        choice = view.home_page()
        if choice.isdigit():
            choice = int(choice)
        else:
            choice = 0
    if choice == 1:
        #Créer un tournoi       
        if tournament_done == True:
            info1, info2, info3, info4, info5, info6, info7 = new_tournament()
            info8 = players_in_tournament(players_list)
            tournament = mdl.Tournaments(info1,info2,info3,info5,info6)
            tournament.total_of_rounds = info4
            tournaments.description = info7
            info8 = tournament.participants
            tournaments_list.append(tournament)
            tournament_done = False
            the_page = 2
            return the_page,choice
        else:
            print("Il faut clore le tournoi en cours",
                    " avant de lancer un nouveau tournoi !")
            the_page = 1
            return the_page,choice
    elif choice == 2:
        # aller au menu tournoi
        if len(tournaments_list) > 0:
            the_page = 2
            return the_page,choice
        else:
            print("Il n'y a aucun tournoi de crée",
                  " pour le moment...\n")
            the_page = 1
            return the_page,choice
    elif choice == 3:
        #fonction de creation d'un joueur,
        info1, info2, info3, info4 = player_creation() 
        player = modl.Players(info1,info2,info3,info4)
        players_list.append(player)
        the_page = 1
        return the_page,choice
    elif choice == 4:
        #fonction de modification de classement
        rating_update()
        the_page = 1
        return the_page,choice
    elif choice == 5:
        the_page = 3
        return the_page,choice
    elif choice == 6:
        the_page = 1
        return the_page,choice
           
def page_2():
    """ affiche le menu du tournoi,
        demande à l'utilisateur de choisir une option,
        et exécute une instruction en fonction de l'option choisie
        :return: the_page (type: int) """
    choice = 0
    choice_list = [1, 2, 3, 4, 5, 6]
    while choice not in choice_list:
        choice = view.tournament_page()
        if choice.isdigit():
            choice = int(choice)
        else:
            choice = 0
    if choice == 1:
        # Générer de nouveaux matchs        
        if matchs_done == True:
            l = len(rounds_list) + 1
            print("Entrer la date du nouveau round:")
            a = input ("? ")
            print("Entrer l'horaire de début du nouveau round")
            b = input("? ")
            time1 = {'date':a,'hour':b}
            new_round = modl.Rounds(tournament_players,l,time1)
            rounds_list.append(new_round)
            if len(rounds_list) > 1:
                new_round.round_type = False
            tournament_players = new_round.classify(tournament_players)
            round_games = new_round.game(tournament_players)
            print("Voici les matchs pour ce round:\n")
            for game in rounds_games:
                print(game)
            the_page = 2
            return the_page
        else:
            print("Il faut d'abord entrer les résultats",
                    " du round actuel avant de passer au round suivant...")
            the_page = 2
            return the_page
    elif choice == 2:
        # voir les matchs actuels
        if len(rounds_list) > 0:
            print("Voici les matchs pour ce round:\n")
            for game in round_games:
                print(game)
            the_page = 2
            return the_page
        else:
            print("Le premier round n'a pas encore été crée")
            the_page = 2
            return the_page
    elif choice == 3:
        #entrer les résultats du round
        for game in rounds_games:
            game = match_results(game)
        the_page = 2
        return the_page
    elif choice == 4:
        #voir le classement du tournoi
        the_page = 2
        return the_page,choice
    elif choice == 5:
        #aller aux stats
        the_page = 3
        return the_page
    elif choice == 6:
        #aller au menu principal
        the_page = 1
        return the_page

def page_3():
    """affiche le menu statistiques,
        demande à l'utilisateur de choisir une option,
        et exécute une instruction en fonction de l'option choisie
        :return: the_page (type: int)"""
    choice = 0
    choice_list = [1, 2, 3, 4]
    while choice not in choice_list:
        choice = view.stat_page()
        if choice.isdigit():
            choice = int(choice)
        else:
            choice = 0
    if choice == 1:        
        #voir liste des joueurs
        choice = view.players_menu()
        the_list = view.players_view(choice,players_list)
        for item in the_list:
            print(item.informations())
        the_page = 3
        return the_page
    elif choice == 2:
        #voir liste des tournois
        choice = view.choose_tournament(tournaments_list)
        if choice > 0:
            view.tournament_informations(tournaments_list[choice])
        else:
            print("Aucun tournoi n'a été crée pour le moment.")
        the_page = 3
        return the_page
    elif choice == 3:
        #aller au menu tournoi
        the_page = 2
        return the_page
    elif choice == 4:
        #aller au menu principal
        the_page = 1
        return the_page

def players_in_tournament(players_list):
    """ enter names and informations of players in the tournament,
        players_list is from the class Players
        :return: tournament_players, a list of players from the class Players"""
    tournament_players = []
    the_name = ""
    total_of_players = 1
    while answer.lower() != "fin":
        print("Entrez le nom de famille du joueur ",i)
        the_name = input()
        if players_list != None:
            i = 0
            indices_list = []
            for player in players_list:
                if player.first_name == the_name:
                    print(i,". ",player.informations())
                    indices_list.append(i)
                i += 1
            print("Si le joueur est dans la liste ci-dessus, ",
                  "entrez le numéro devant le joueur pour l'ajouter au tournoi,\n",
                  "et sinon appuyez sur Entrée")
            player_choosen = input()
            try:
                player_choosen = int(player_choosen)
                if player_choosen in indices_list:
                    tournament_players.append(players_list[player_choosen])
                else:
                    info1, info2, info3, info4 = player_creation() 
                    player = modl.Players(info1,info2,info3,info4)
                    players_list.append(player)
                    tournament_players.append(player)
            except ValueError:
                info1, info2, info3, info4 = player_creation() 
                player = modl.Players(info1,info2,info3,info4)
                players_list.append(player)
                tournament_players.append(player)
        else:
            info1, info2, info3, info4 = player_creation() 
            player = modl.Players(info1,info2,info3,info4)
            players_list.append(player)
            tournament_players.append(player)
    return tournament_players
            








########## ICI LE MODULE CONTROLLER PRECEDENT ##########
def tournament_name():
    """ input the name of a tournament,
       :return: the_name, type string with letters and some special characters"""
    verification = False
    while verification == False:
        the_name = input("Entrez le nom du tournoi:\n")
        result = re.match(r"^[\w\sçéèùê]+$",the_name)
        if (result) and (len(the_name) <= 100):
            verification = True
    return the_name

def tournament_place():
    """input the place of a tournament
       :return: the_place, type string with letters and some special characters"""
    verification = False
    while verification == False:
        the_place = input("Entrez le lieu du tournoi:\n")
        result = re.match(r"^[\w\sçéèùê]+$",the_place)
        if result and len(the_place) <= 100:
            verification = True
    return the_place

def tournament_date():
    """input the date for a tournament
       :return: the_date, a string in dd/mm/yyyy format"""
    verification = False
    while verification == False:
        print("Entrez la date de début du tournoi,",
              "au format jj/mm/aaaa, par exemple 03/10/2013 \n")
        the_date = input()
        verification = date_check(the_date)
    return the_date

def tournament_hour():
    """input hour and minutes for a tournament
       :return: the_hour, a string in hh:mm format"""
    verification = False
    while verification == False:
        print("Entrez l'horaire de début du tournoi,",
              "au format hh:mm ou hhmm, par exemple 09:35 pour 9 heures 35 minutes,",
              "ou 18:02 pour 6 heures 2 minutes l'après midi:")
        the_hour = input()
        verification = time_check(the_hour)
    return the_hour

def tournament_rounds_number():
    """ input the round's number for a tournament
       :return: total_of_rounds, type int"""
    verification = False
    while verification == False:
        print("Indiquez le nombre de rounds pour ce tournoi, ou tapez",
              " directement entrée pour laisser 4 par défaut:\n")
        total_of_rounds = input()
        if total_of_rounds.isdigit():
            verification = True
        elif total_of_rounds == "":
            verification = True
            total_of_rounds = 4
    total_of_rounds = int(total_of_rounds)
    return total_of_rounds

def tournament_time_type():
    """ input the time controller for a tournament
       :return: the string 'Blitz', 'Bullet' or 'Speed' """
    verification = False
    while verification == False:
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

def new_tournament():
    """ créé un nouveau tournoi, en demandant les différentes
        informations à l'utilisateur.
        :return: the_name, the_place, the_date,
                 total_of_rounds, time_controller, tournament_players,
                 description """
    print("Création d'un nouveau tournoi:")
    the_name = tournament_name()
    the_place = tournament_place()
    the_date = tournament_date()
    total_of_rounds = tournament_rounds_number()
    time_controller = tournament_time_type()
    beginning_hour = tournament_hour()
    #creer la description
    description = ""

    return the_name, the_place, the_date, total_of_rounds, beginning_hour, time_controller, description
     

def player_creation():
    """ create a new player, input differents informations about him
        :return: first_name,last_name,birth_date,gendar """
    print("Création d'un nouveau joueur:")
    first_name = "0"
    while not first_name.isalpha():
        first_name = input ("Entrez le prénom du joueur:\n")
    last_name = "0"
    while not last_name.isalpha():
        last_name = input ("Entrez le nom du joueur:\n")
    verification = False
    while verification == False:
        print("Entrez la date de naissance du joueur,",
            "au format jj/mm/aaaa, par exemple 03/10/1983 \n")
        birth_date = input()
        verification = date_check(birth_date)
    gendar = "0"
    while gendar.lower() not in ["f","h"]:
        gendar = input("Entrez H pour homme et F pour femme:\n")
    return first_name,last_name,birth_date,gendar

def rating_update():
    """ update a players's rating
        :return: """
    print("Tapez le nom d'un joueur ou bien tapez 0 pour voir la liste des joueurs")
    
def match_results(games_list):
    """ input matchs's results
        :param: games_list is a list of tuples
                with keys 'opponents' and 'score'
        :return: the games_list, update """
    print("Entrez les résultats pour chaque match,\n",
          "sous la forme 0 puis 1 ou 1 puis 0 en cas de vainqueur, \n",
          "ou bien 0.5 pour chaque joueur en cas de nul. \n",
          "Vous pouvez marquer 0 à chacun pour passer au match suivant,\n",
          "sans entrer de résultat.")
    for game in games_list:
        print(game['opponents'], ":")
        verification = False
        while verification == False:
            print("score pour ", game['opponents'][0],": \n")
            a = input ()
            print("score pour ", game['opponents'][1],": \n")
            b = input ()
            if a == "0" and b == "0":
                verification == True
            elif (a not in ["0","0.5","1"]) or (b not in ["0", "0.5", "1"]):
                print("Les scores entrés doivent être 0 ou 0.5 ou 1...")
            else:
                a = float(a)
                b = float(b)
                if a + b != 1:
                    print("Les résultats possibles sont 1 - 0, 0 - 1 ou 0.5 - 0.5...")
                else:
                    game['score'] = [a,b]
                    verification = True
    print("les scores ont bien été entrés\n")
    return games_list

def name_check():
    #check the name's format
    pass 

def date_check(a_date):
    """ check the format of a date
    :return: date_test, a boolean"""
    date_test = False
    result = re.match(r"^[0123]{1}\d{1}/[01]{1}\d{1}/\d{4}$",a_date)
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
       :return: verification, a boolean"""
    verification = False
    if (a_year % 400 == 0) or (a_year % 4 == 0 and a_year % 100 != 0):
        verification = True
    else:
        print("Ce n'est pas une année bixectile...")
    return verification 

def time_check(a_string):
    """ check the time's format hh:mm
        :return: verification, a boolean"""
    verification = False
    a_string = a_string.replace(":","")
    if len(a_string) == 4 and a_string.isdigit():
        hours = int(a_string[0] + a_string[1])
        minutes = int(a_string[2] + a_string[3])
        if 0 <= hours <= 24 and 0 <= minutes <= 60:
            verification = True
    return verification
        
def main():
    """ fonction principale: gère le passage d'une page à l'autre
        avec une boucle qui stop si the_page = 1 et choice = 6
        :return: message indiquant la fermeture du programme, le cas échéant"""
    tournaments_list = []
    players_list = []
    tournament_done = True
    matchs_done = True
    page = 1
    choice = 0
    stop = (page == 1) and (choice == 6)
    while not stop:
        if page == 1:
            page,choice = page_1()
        elif page == 2:
            page = page_2()
        elif page == 3:
            page = page_3()
        stop = page == 1 and choice == 6
    return print("\n Le programme est désormais fermé. Bonne journée à vous.")
    
if __name__ == "__main__":
    main()



