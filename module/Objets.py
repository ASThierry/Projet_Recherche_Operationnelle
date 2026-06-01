import os
import pandas as pd

class Objets():
    def __init__(self):
        self.all = []
        self.__lire_excel("../data/velo.xlsx")

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
            self.all = pd.read_excel(
                chemin_fichier,
                engine="openpyxl" if chemin_fichier.endswith(".xlsx") else None
            )

            print(f"Fichier '{chemin_fichier}' lu avec succès.")

        except ValueError as ve:
            print(f"Erreur de lecture : {ve}")
        except FileNotFoundError:
            print("Erreur : fichier introuvable.")
        except Exception as e:
            print(f"Erreur inattendue : {e}")
        return None