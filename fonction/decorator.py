import time
from functools import wraps


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
        print(f"L'exécution de '{fonction.__name__}' a pris {temps_ecoule:.8f} secondes.")

        #On retourne le résultat de la fonction
        return resultat

    return wrapper