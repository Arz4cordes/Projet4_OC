# Programme de gestion des tournois d'échecs
#
# Pour utiliser le programme, créez d'abord un environnement virtuel en tapant:
python -m venv p4virtuel
# puis activez le en tapant:
p4virtuel/Scripts/activate
# (cette procédure est valable sous Windows, si vous utilisez un autre OS
# l'activation de l'environnement virtuel se fait avec des commandes différentes)
#
# Pour démarrer le programme, taper:
python ct_controller.py
# 
# Le programme sauvegarde les données après chaque action,
dans trois fichiers json:
chess_players
chess_rounds
chess_tournaments
# La mise à jour se fait à la fin de l'action:
par exemple si un tournoi est en cours de création
et qu'il y a 4 joueurs qui ont été crée
mais que tous les joueurs n'ont pas été inscrits quand on quitte le programme,
alors en relançant le programme les 4 joueurs auront été enregistrés
mais le tournoi n'aura pas été enregistré (création non terminée, à recommencer)
#
# Pour les statistiques, on peut voir:
les joueurs par ordre alphabétique
les joueurs en fonction de leur classement (nombre décroissant de rating)
les tournois, et lorsqu'un tournoi est choisi les participants au tournoi
ainsi que toutes les rondes avec les matchs s'affichent
#
# Le programme gère les tirages au sort des matchs selon le système suisse,
mais comme il y a plusieurs exceptions
alors le programme va éventuelement faire jouer
à nouveau deux joueurs qui se sont rencontrés ensemble
lorsqu'il y a un blocage
#
# Pour générer un nouveau rapport flake8, taper la commande suivante:
python -m flake8 --format=html --htmldir=flake8_rapport --max-lin-length=119 ct_controller.py views/ct_views.py models/ct_models.py




