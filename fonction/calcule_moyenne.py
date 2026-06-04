import os

# ==> Mathis et Gemini
def calculer_moyenne_temps(nom_de_la_fonction):
    """Lit le fichier de logs d'une fonction et calcule la moyenne de son temps d'exécution."""
    chemin_fichier = f"../stats_temps/{nom_de_la_fonction}.txt"

    if not os.path.exists(chemin_fichier):
        print(f"Aucune statistique trouvée pour la fonction '{nom_de_la_fonction}'.")
        return None

    with open(chemin_fichier, "r", encoding="utf-8") as fichier:
        # On lit chaque ligne, on enlève les espaces vides et on convertit en float
        temps_enregistres = [float(ligne.strip()) for ligne in fichier if ligne.strip()]

    if not temps_enregistres:
        print(f"Le fichier pour '{nom_de_la_fonction}' est vide.")
        return 0.0

    # Calcul mathématique simple
    moyenne = sum(temps_enregistres) / len(temps_enregistres)

    print(f"--- Statistiques pour '{nom_de_la_fonction}' ---")
    print(f"Nombre total d'exécutions : {len(temps_enregistres)}")
    print(f"Temps moyen d'exécution   : {moyenne:.8f} secondes.\n")

    return moyenne
def Calculer_moyenne_wagons():
    calculer_moyenne_temps("bestfit1doneline")
    calculer_moyenne_temps("bestfit1doffline")
    calculer_moyenne_temps("extremePoints3dOnline")
    calculer_moyenne_temps("extremePoints3dOffline")
    calculer_moyenne_temps("firstfit1doffline")
    calculer_moyenne_temps("firstfit1doneline")
    calculer_moyenne_temps("guillotine2dOnline")
    calculer_moyenne_temps("guillotine2dOffline")
    calculer_moyenne_temps("guillotine3dOffline")
    calculer_moyenne_temps("guillotine3dOnline")
    calculer_moyenne_temps("guillotine3dOffline_opti")
    calculer_moyenne_temps("guillotine3dOnline_opti")

def calculer_moyenne_sac():
    calculer_moyenne_temps("heuristique")
    calculer_moyenne_temps("Glouton_optimise")
    calculer_moyenne_temps("brute_force")

if __name__ == "__main__":
    calculer_moyenne_sac()