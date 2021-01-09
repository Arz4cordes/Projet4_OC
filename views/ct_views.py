""" the user can view tournament's ranking,
    matchs create (players's opponents),
    and statistiques """

def home_page():
    """ print home page"""
    print(" ")
    print("MENU PRINCIPAL")
    print("1. Créer un nouveau tournoi")
    print("2. Voir le tournoi en cours ou le dernier tournoi terminé")
    print("3. Ajouter un nouveau joueur")
    print("4. Mettre à jour le classement général des joueurs")
    print("5. Voir les statistiques générales")
    print("6. Quitter le programme")
    choice = input("? ")
    return choice

def stat_page():
    """ print the statistiques's menu """
    print(" ")
    print("STATISTIQUES")
    print("1. Liste des joueurs")
    print("2. Liste des tournois")
    print("3. Aller au tournoi en cours")
    print("4. Retour au menu principal")
    choice = input("? ")
    return choice

def players_menu():
    choice = "0"
    while choice.lower() != "a" and choice.lower() != "b":
        print("a. Voir les joueurs par ordre alphabétique")
        print("b. Voir le classement de tous les joueurs")
        choice = input ("? ")
    if choice.lower == "a":
        choice = 1
    elif choice.lower() == "b":
        choice = 2
    return choice

def players_view(a_choice,a_list):
    if a_choice == 1:
        a_list = players_alphabetical_order(a_list)
    elif a_choice ==2:
        a_list = players_by_ranking(a_list)
    return a_list

def players_alphabetical_order(a_list):
    #fonction tri rapide de la liste de joueurs
    print("Liste de tous les joueurs enregistrés, par ordre alphabétique:")
    #fonction de tri à écrire !
    return a_list

def players_by_ranking(a_list):
    #tri des joueurs en regardant leurs indices
    print("Liste de tous les joueurs enregistrés dans l'ordre de leur classement:")
    #fonction de tri à écrire !
    return a_list

def choose_tournament(a_list):
    i = 1
    for tournament in a_list:
        print(f"{i}. {tournament}")
        i += 1
    choice = 0
    while choice < 1 and choice > len(a_list):
        print ("Entrer le numéro du tournoi pour voir ",
            "le détail du tournoi ou 0 pour revenir au menu \"statistiques\".")
        choice = input("? ")
        if choice.isdigit():
            choice = int(choice)
        else:
            choice = 0
    choice = choice - 1
    return choice

def tournament_informations(a_tournament):
    print("Voici les informations pour ce tournoi:")


def matchs_list(a_list):
    i = 0
    for round in a_list:
        print("round {i}:")
        for game in a_list.games:
            print(game['opponents'], ":", game['score'])
    
def rounds_list(a_list):
    i = 1
    for round in a_list:
        print(f"{i}. {round}")
        i += 1
    print ("Entrer le numéro du tournoi pour voir",
            "le détail du tournoi ou 0 pour revenir au menu 'statistiques'.")
    choice = input(" ")
    return choice

def tournament_page():
    """ print the tournament's menu """
    print(" ")
    print("TOURNOI EN COURS")
    print("1. Lancer le round suivant en générant les matchs")
    print("2. Voir les matchs en cours")
    print("3. Entrer les résultats du round actuel")
    print("4. Voir le classement actuel du tournoi")
    print("5. Voir les statistiques générales")
    print("6. Retour au menu principal")
    choice = input ("? ")

def tournament_ranking():
    pass 
    # return print(tournament's ranking)

def oppositions():
    pass 
    # return print(matchs to play)

def players_stat():
    pass 
    # return print(statistiques)
