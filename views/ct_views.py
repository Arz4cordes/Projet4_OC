""" the user can view tournament's ranking,
    matchs create (players's opponents),
    and statistiques """


def home_page():
    """ print home page, page number 1
    input a choice
    :return: choice (type: string)
    """
    print(" ")
    print("MENU PRINCIPAL".center(20))
    print("1. Créer un nouveau tournoi")
    print("2. Voir le tournoi en cours ou le dernier tournoi terminé")
    print("3. Ajouter un nouveau joueur")
    print("4. Mettre à jour le classement d'un joueur")
    print("5. Voir les statistiques générales")
    print("0. Quitter le programme")
    choice = input("? ")
    return choice


def tournament_page():
    """ print the tournament's menu, page number 2
    input a choice
    :return: choice (type: string)
    """
    print(" ")
    print("TOURNOI EN COURS".center(20))
    print("1. Lancer le round suivant en générant les matchs")
    print("2. Voir les matchs en cours")
    print("3. Entrer les résultats du round actuel")
    print("4. Voir le classement actuel du tournoi")
    print("5. Voir les statistiques générales")
    print("6. Retour au menu principal")
    print("0. Quitter le programme")
    choice = input("? ")
    return choice


def stat_page():
    """ print the statistiques's menu, page number 3
    input a choice
    :return: choice (type: string)
    """
    print(" ")
    print("STATISTIQUES".center(20))
    print("1. Liste des joueurs")
    print("2. Liste des tournois et des rondes")
    print("3. Aller au tournoi en cours")
    print("4. Retour au menu principal")
    print("0. Quitter le programme")
    choice = input("? ")
    return choice


def players_menu():
    """ input a choice about players's list,
    by ranking or in alphabetical order
    :return: choice (type: int)
    """
    choice = "0"
    while choice.lower() != "a" and choice.lower() != "b":
        print("a. Voir les joueurs par ordre alphabétique")
        print("b. Voir le classement de tous les joueurs")
        choice = input("? ")
    if choice.lower() == "a":
        choice = 1
    elif choice.lower() == "b":
        choice = 2
    return choice


def players_view(players_list, a_choice):
    """ display a players's list,
    choice 1 is in alphabetical order,
    choice 2 is by rating
    choice 3 is in order of appearance
    """
    if players_list == []:
        print("Il n'y a aucun joueur à afficher pour le moment.")
    else:
        if a_choice == 1:
            print("Liste de tous les joueurs enregistrés ",
                  "dans l'ordre alphabétique:")
            for player in players_list:
                print(player.display())
                print("")
        elif a_choice == 2:
            print("Liste de tous les joueurs enregistrés ",
                  "dans l'ordre de leur classement:")
            i = 1
            for player in players_list:
                print(str(i) + ")")
                print(player.display())
                i += 1
        elif a_choice == 3:
            i = 0
            for player in players_list:
                print("Numéro", i)
                print(player.display())
                i += 1


def choose_tournament(a_list):
    """ menu about tournaments's view
    :return: choice (type: int)
    """
    i = 1
    for tournament in a_list:
        print(f"{i}. {tournament}")
        i += 1
    choice = 0
    while choice < 1 and choice > len(a_list):
        print("Entrer le numéro du tournoi pour voir ",
              "le détail du tournoi ou 0 pour revenir au menu",
              " 'statistiques' .")
        choice = input("? ")
        if choice.isdigit():
            choice = int(choice)
        else:
            choice = 0
    choice = choice - 1
    return choice


def tournament_informations(a_tournament):
    """ print a tournament's informations """
    return print("Voici les informations pour ce tournoi:")


def matchs_list(a_list):
    """ print the list of matchs for a round """
    i = 0
    for round in a_list:
        print(f"round {i}:")
        i += 1
        for game in a_list.games:
            print(game['opponents'], ":", game['score'])
    return print("Voilà la liste des matchs")


def rounds_list(a_list):
    i = 1
    for round in a_list:
        print(f"{i}. {round}")
        i += 1
    print("Entrer le numéro du round pour voir",
          "le détail du tournoi ou 0 pour revenir au menu 'statistiques'.")
    choice = input(" ")
    return choice


def tournament_ranking():
    """ affiche le classement du tournoi"""
    return print("Voilà le classement actuel du tournoi")


def text_area_display(a_string):
    return print(a_string)


def information_message(a_string):
    return print(a_string)
