#On crée notre fonction pour exécuter le programme de "comptage" de mots
def count_word(counter = str):
#On demande a l'utilisateur de crée une phrase
    counter = input("Votre phrase : ")
#On affiche le nombre de mots
    print(len(counter.split()), "mots")
    return counter

quitter = ""
#Tant que l'utilisateur ne quitte pas, on continue le code
while quitter != "oui":
    count_word()
    quitter = input("Voulez-vous quitter? : ").lower()
