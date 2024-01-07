import os
from os import listdir
from os.path import isfile, join

# Chemin du répertoire principal
chemin_parent = "Z:\!!! MEDIA !!!\FILMS"

# Création de la liste avec tous les fichiers du répertoire
liste_fichiers = [f for f in listdir(chemin_parent) if isfile(join(chemin_parent, f))]

# Boucle pour traiter chaque fichier
for fichier in liste_fichiers:
    # Extraire le nom du fichier sans l'extension
    nom_fichier, extension = os.path.splitext(fichier)

    # Créer le chemin complet du répertoire en utilisant le nom du fichier sans l'extension
    chemin_repertoire = os.path.join(chemin_parent, nom_fichier)

    # Vérifier si le répertoire n'existe pas déjà
    if not os.path.exists(chemin_repertoire):
        os.makedirs(chemin_repertoire)
        print(f"Répertoire créé : {chemin_repertoire}")

    # Déplacer le fichier dans le répertoire
    chemin_source_fichier = os.path.join(chemin_parent, fichier)
    chemin_destination_fichier = os.path.join(chemin_repertoire, fichier)

    # Vérifier si le fichier source existe avant de le déplacer
    if os.path.exists(chemin_source_fichier):
        os.rename(chemin_source_fichier, chemin_destination_fichier)
        print(f"Fichier {fichier} déplacé vers {chemin_repertoire}")
    else:
        print(f"Le fichier {fichier} n'existe pas dans le répertoire source.")

# Afficher un message une fois que tous les répertoires ont été créés et les fichiers déplacés
print("Tous les répertoires ont été créés et les fichiers ont été déplacés avec succès.")
