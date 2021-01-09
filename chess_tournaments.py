import controller.ct_controller as ctrl
import views.ct_views as view
import models.ct_models as modl

tournaments_list = []
players_list = []
tournament_done = False
matchs_done = True

def page_1():
    """ affiche le menu principal,
        demande à l'utilisateur de choisir une option,
        et exécute une instruction en fonction de l'option choisie"""
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
            tournament_players = ctrl.new_tournament()
            #portée de la variable ci-dessus ???
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
        info1, info2, info3, info4 = ctrl.player_creation() 
        player = modl.Players(info1,info2,info3,info4)
        players_list.append(player)
        the_page = 1
        return the_page,choice
    elif choice == 4:
        #fonction de modification de classement
        ctrl.ranking_update()
        the_page = 1
        return the_page,choice
    elif choice == 5:
        the_page = 3
        return the_page,choice
    elif choice == 6:
        the_page = 1
        return the_page,choice
           
def page_2():
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
            game = ctrl.match_results(game)
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

def main():
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



