import time
from functools import wraps


def chronometrer(fonction):
    """Décorateur qui mesure et affiche le temps d'exécution d'une fonction."""

    @wraps(fonction)
    def wrapper(*args, **kwargs):
        # 1. On relève le temps avant l'exécution
        debut = time.perf_counter()

        # 2. On exécute la fonction avec tous ses arguments
        resultat = fonction(*args, **kwargs)

        # 3. On relève le temps après l'exécution
        fin = time.perf_counter()

        # 4. On calcule et affiche la différence
        temps_ecoule = fin - debut
        print(f"L'exécution de '{fonction.__name__}' a pris {temps_ecoule:.5f} secondes.")

        # 5. On retourne le résultat de la fonction
        return resultat

    return wrapper