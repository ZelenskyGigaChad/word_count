#On crée notre fonction pour exécuter le programme de "comptage" de mots.
def count_word(phrase):
#On retourne le nombre de mots
    return (len(phrase.split()))

quitter = ""
#Tant que l'utilisateur ne quitte pas, on continue le code
while quitter != "oui":
#On prend un input en str pour faire activer la fonction count_word, puis on l'affiche
    la_fameuse_phrase = input("Votre phrase : ")
    execution = count_word(la_fameuse_phrase)
    print(execution, 'mots')

    quitter = input("Voulez-vous quitter? : ").lower()
