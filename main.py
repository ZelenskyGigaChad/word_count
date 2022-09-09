#On crée notre fonction pour exécuter le programme de "comptage" de mots
def compteur_de_mots():
#On demande a l'utilisateur de crée une phrase
    count_word = input("Votre phrase : ")
#On affiche le nombre de mots
    print(len(count_word.split(" ")), "mots")

quitter = ""
#Tant que l'utilisateur ne quitte pas, on continue le code
while quitter != "oui" and quitter != "OUI":
    compteur_de_mots()
    quitter = input("Voulez-vous quitter? : ")