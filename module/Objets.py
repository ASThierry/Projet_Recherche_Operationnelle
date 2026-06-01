import os
import pandas as pd
from module.Objet import Objet

class Objets:
    def __init__(self):
        self.all : [Objet] = []
        self.__lire_excel("data/velo.xlsx")

    def __lire_excel(self,chemin_fichier : str):
        """
        Lit un fichier Excel et retourne un DataFrame Pandas.
    x
        :param chemin_fichier: Chemin complet verxs le fichier Excel (.xlsx ou .xls)
        :return: DataFrame Pandas ou None si erreur
        """
        try:
            # Vérifier si le fichier existe
            if not os.path.isfile(chemin_fichier):
                print(f"Erreur : le fichier '{chemin_fichier}' est introuvable.")
                return None

            # Lecture du fichier Excel
            df = pd.read_excel(
                chemin_fichier,
                engine="openpyxl" if chemin_fichier.endswith(".xlsx") else None
            )
            print(f"Fichier '{chemin_fichier}' lu avec succès.")
            for i in range(len(df)):
                temp = Objet(df["Objet"][i], df["Masse"][i], df["Utilité"][i])
                self.all.append(temp)

        except ValueError as ve:
            print(f"Erreur de lecture : {ve}")
        except FileNotFoundError:
            print("Erreur : fichier introuvable.")
        except Exception as e:
            print(f"Erreur inattendue : {e}")

        return None

    def __str__(self):
        retour = ""
        for i in self.all:
            retour += i.__str__() + "\n"
        return retour
