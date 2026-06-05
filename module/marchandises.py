import os
import pandas as pd
from module.marchandise import Marchandise

# ==> Mathis
class Marchandises:
    def __init__(self):
        self.all : [Marchandise] = []
        self.__lire_excel("data/marchandises.xlsx")

    def __lire_excel(self, chemin_fichier: str):
        """
        Lit un fichier Excel et retourne un DataFrame Pandas.
        :param chemin_fichier: Chemin complet vers le fichier Excel (.xlsx ou .xls)
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
            df.columns = df.columns.str.strip()
            #print(f"Fichier \033[93m'{chemin_fichier}'\033[0m lu avec succès.")

            df.head()
            for i in range(len(df)):
                temp = Marchandise(df["Numero"][i], df["Designation"][i], df["Longueur"][i], df["Largeur"][i], df["Hauteur"][i],df["Retournable"][i])
                self.all.append(temp)

        except ValueError as ve:
            print(f"Erreur de lecture : {ve}")
        except FileNotFoundError:
            print("Erreur : fichier introuvable.")
        except Exception as e:
            print(f"Erreur inattendue : {e}")

        return None

    def __str__(self):
        retour :str = " toutes les marchandises :\n"
        for i in self.all:
            retour += i.__str__() + "\n"
        return retour
