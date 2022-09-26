#On crée notre fonction pour exécuter le programme de "comptage" de mots.
def count_word(phrase):
#On affiche le nombre de mots
    return (len(phrase.split()), "mots")

quitter = ""
#Tant que l'utilisateur ne quitte pas, on continue le code
while quitter != "oui":
    print(count_word(input("Votre phrase : ")))

    quitter = input("Voulez-vous quitter? : ").lower()
