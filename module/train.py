from module.conteneur import Conteneur
import matplotlib.pyplot as plt
import random



class Train:
    def __init__(self):
        self.conteneurs : [Conteneur]= []
        


    def __str__(self):
        retour : str ="<====== Contenue du train ======>\n"
        i : int = 1
        for conteneur in self.conteneurs:
            retour += f"Le conteneur {i} contient :\n"
            retour += conteneur.__str__() + "\n"
            i+=1
        return retour

    def ajouter(self,conteneur: Conteneur):
        self.conteneurs.append(conteneur)

    def affichage_reduit(self):
        print("<===== Le train ( affichage reduit )======>")
        print(f"Le nombre de wagon est {len(self.conteneurs)}")
        volume : int = 0
        for i in range(len(self.conteneurs)):
            print(f"--- Wagon n° {i+1}")
            volume += self.conteneurs[i].getVolumeRestante()
            self.conteneurs[i].affichage()
        print(f"<===== il reste dans le train : {volume} m² de libre =====>")

    def afficher_graphique_3d(self):
        """
        Génère une fenêtre Matplotlib avec une représentation 3D de chaque conteneur.
        """
        nb_conteneurs = len(self.conteneurs)

        if nb_conteneurs == 0:
            print("Le train est vide, rien à afficher.")
            return

        # Création de la figure (plus il y a de conteneurs, plus la fenêtre est large)
        fig = plt.figure(figsize=(6 * nb_conteneurs, 6))

        for i, conteneur in enumerate(self.conteneurs):
            # Ajout d'un sous-graphique 3D pour ce conteneur
            ax = fig.add_subplot(1, nb_conteneurs, i + 1, projection='3d')
            ax.set_title(f"Conteneur {i + 1}", weight='bold')

            # Définir les limites du graphique basées sur la taille du conteneur
            ax.set_xlim([0, conteneur.longueur])
            ax.set_ylim([0, conteneur.largeur])
            ax.set_zlim([0, conteneur.hauteur])

            ax.set_xlabel('Longueur (X)')
            ax.set_ylabel('Largeur (Y)')
            ax.set_zlabel('Hauteur (Z)')

            # Ajuster les proportions de la boîte de rendu pour refléter la vraie forme du conteneur
            try:
                ax.set_box_aspect([conteneur.longueur, conteneur.largeur, conteneur.hauteur])
            except AttributeError:
                # set_box_aspect nécessite une version récente de Matplotlib, on ignore si ça plante
                pass

            # Dessiner chaque marchandise à l'intérieur
            for marchandise in conteneur.contenu:
                # Générer une couleur aléatoire claire pour bien différencier les boîtes
                couleur = "#" + ''.join([random.choice('456789ABCDEF') for _ in range(6)])

                # ax.bar3d(x, y, z, dx, dy, dz)
                ax.bar3d(
                    marchandise.x, marchandise.y, marchandise.z,
                    marchandise.longueur, marchandise.largeur, marchandise.hauteur,
                    color=couleur, alpha=0.8, edgecolor='black', linewidth=0.5
                )

        plt.tight_layout()
        plt.show()


