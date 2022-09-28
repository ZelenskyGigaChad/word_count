#On crée notre fonction pour exécuter le programme de "comptage" de mots.
def count_word(phrase):
#On retourne le nombre de mots
    return (len(phrase.split()), "mots")

quitter = ""
#Tant que l'utilisateur ne quitte pas, on continue le code
while quitter != "oui":
#On prend un input en str pour faire activer la fonction count_word, puis on l'affiche
    print(count_word(input("Votre phrase : ")))

    quitter = input("Voulez-vous quitter? : ").lower()
