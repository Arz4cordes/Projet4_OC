""" user's actions:
    create a new tournament
    give matchs's results
    and datas check (format) """

import re


def new_tournament():
    #create a new tournament
    print("Création d'un nouveau tournoi:")
    #Nom
    verification = False
    while verification == False:
        the_name = input("Entrez le nom du tournoi:\n")
        result = re.match(r"^[\wçéèùê]+$",the_name)
        if (result) and (len(the_name) <= 100):
            verification = True
    #Place
    verification = False
    while verification == False:
        the_place = input("Entrez le lieu du tournoi:\n")
        result = re.match(r"^[\wçéèùê]+$",the_place)
        if result and len(the_place) <= 100:
            verification = True
    #Date
    verification = False
    while verification == False:
        print("Entrez la date de début du tournoi,",
            "au format jj/mm/aaaa, par exemple 03/10/2013 \n")
        the_date = input()
        verification = date_check(the_date)
    #Nombre de rounds
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
    #time controller
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
    #creer la liste de joueurs
    tournament_players = []
        #BOUCLE
        # demander un nom
        # proposer une liste de noms déjà enregistrés
            #si nouveau nom: fonction création de joueur
        #rajouter le nom à la liste
    
    #creer la description
    description = ""

    return the_name, the_place, the_date, total_of_rounds, time_controller, tournament_players, description
     

def player_creation():
    #creation d'un joueur
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

def ranking_update():
    #modifier le classement d'un ou plusieurs joueurs
    print("Tapez le nom d'un joueur ou bien tapez 0 pour voir la liste des joueurs")
    


def match_results(a_game_tuple):
    #enter match's result
    #return the tuple, with a list of two float
    #associate with the key score
    print("les scores ont bien été entrés")
    return a_game_tuple



def name_check():
    #check the name's format
    pass 

def date_check(a_date):
    date_test = False
    result = re.match(r"^[0123]{1}\d{1}/[01]{1}\d{1}/\d{4}$",a_date)
    if result:
        date_test = True
        decomposition = a_date.split("/")
        day = int(decomposition[0])
        month = int(decomposition[1])
        year = int(decomposition[2])
        cond1 = day < 1
        cond2 = day > 31
        cond3 = month < 1
        cond4 = month > 12
        cond5 = year < 1900
        cond6 = year % 4 == 0
        cond7 = year % 100 == 0
        cond8 = year % 400 == 0
        if cond1 or cond2 or cond3 or cond4:
            date_test = False
        elif cond5:
            print("It seem to be very old, no ?")
            date_test = False
        if day == 29 and month == 2:
            if cond6 == False:
                print("Ce n'est pas une année bixectile...")
                date_test = False
            elif (cond7 == True) and (cond8 == False):
                print("Ce n'est pas une année bixectile...")
                date_test = False
    return date_test 

def time_check():
    #check the time's format
    pass 



