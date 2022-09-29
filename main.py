#Renaud Deschenes
#27 septembre 2022
#Compteur de mots Tp1
#On crée notre fonction pour exécuter le programme de "comptage" de mots.
def count_word(phrase):
#On retourne le nombre de mots
    return (len(phrase.split()))

quitter = ""
#Tant que l'utilisateur ne quitte pas, on continue le code
while quitter != "oui":
#On prend un input en str
    la_fameuse_phrase = input("Votre phrase : ")
#On appele la fonction count word avec l'input de la variable 'la fameuse phrase'
    execution = count_word(la_fameuse_phrase)
#On affiche le nombre de mots    
    print(execution, 'mots')

    quitter = input("Voulez-vous quitter? : ").lower()
