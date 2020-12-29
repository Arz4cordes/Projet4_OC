""" the user can view tournament's ranking,
    matchs create (players's opponents),
    and statistiques """

def home_page():
    """ print home page"""
print(" ")
print("MENU PRINCIPAL")
print("1. Créer un nouveau tournoi")
print("2. Voir le tournoi en cours ou le dernier tournoi terminé")
print("Ajouter un nouveau joueur ou modifier le classement des joueurs")
print("4. Voir les statistiques générales")
choice = input("")
return choice

def stat_page():
    """ print the statistiques's menu """
    print("STATISTIQUES")
    print("1. Liste des joueurs")
    print("2. Liste des tournois")
    print("3. Retour au menu principal")
    print("4. Aller au tournoi en cours")
    choice = input("")
    return choice

def players_view(a_list):
    print("a. Voir les joueurs par ordre alphabétique")
    print("b. Voir le classement de tous les joueurs")
    choice = input ("")
    return choice 

def players_alphabetical_order(a_list):
    #fonction tri rapide de la liste de joueurs
    pass

def players_by_ranking(a_list):
    #tri des joueurs en regardant leurs indices
    pass

def tournaments_list(a_list):
    i = 1
    for tournament in a_list:
        print(f"{i}. {tournament}")
        i += 1
    print ("Entrer le numéro du tournoi pour voir ",
            "le détail du tournoi ou 0 pour revenir au menu 'statistiques'.")
    choice = input(" ")
    return choice

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

def tournament_ranking():
    pass 
    # return print(tournament's ranking)

def oppositions():
    pass 
    # return print(matchs to play)

def players_stat():
    pass 
    # return print(statistiques)
