import time
from functools import wraps
import os


def chronometrer(fonction):
    """Décorateur qui mesure et affiche le temps d'exécution d'une fonction."""

    @wraps(fonction)
    def wrapper(*args, **kwargs):
        #On relève le temps avant l'exécution
        debut = time.perf_counter()

        # On exécute la fonction avec tous ses arguments
        resultat = fonction(*args, **kwargs)

        # On relève le temps après l'exécution
        fin = time.perf_counter()

        #On calcule et affiche la différence
        temps_ecoule = fin - debut
        #print(f"L'exécution de \033[92m'{fonction.__name__}'\033[0m a pris {temps_ecoule:.8f} secondes.")

        dossier_logs = "stats_temps"
        os.makedirs(dossier_logs, exist_ok=True)

        nom_fichier = os.path.join(dossier_logs, f"{fonction.__name__}.txt")

        with open(nom_fichier, "a", encoding="utf-8") as fichier:
            # On écrit uniquement la valeur brute suivie d'un retour à la ligne
            fichier.write(f"{temps_ecoule}\n")

        #On retourne le résultat de la fonction
        return resultat

    return wrapper