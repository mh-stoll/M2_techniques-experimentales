# Etude de charges d'espace
Etude de la densité volumique de charge dans un solide par application d'un front d'onde thermique (MOT)

## Manip
Une masse métallique est maintenu dans une atmosphère à 60°C.
Elle est sortie pour être posée brusquement sur l'échantillon à l'aide d'une commande hydraulique.
Des électrodes de part et d'autre de l'échantillon mesurent alors le courant induit par le front d'onde.
Un ensemble conditionneur & CAN conduit le signal jusqu'à un PC,
une application labVIEW renvoit un fichier .txt contenant :
Temps(s),	Delta t (m),	Champ E (V/m),	Rho (C.m-3), Interpolation p.

## Objectif
Puisque la manip a été reproduite plusieurs fois par échantillon et avec trois échantillons,
on souhaite optimiser la visualisation et le traitement des données.

## Contenu
Input (exemples) : 
- essai2_4_PSP.txt (signal numérique, image du courant en fonction du temps, pour une intération)
- labview_results_2_0 (sortie labVIEW pour une intération)

graph_prod.py :
- produit et enregistre un graphe du signal numérique brut (pour une ou plusieurs itérations au choix)
    VOIR EXEMPLE essai2_4_PSP.txt.jpg
- produit et enregistre 4 graphes du signal traité avec labVIEW, montrant chaque variable en fonction du temps (pour une ou plusieurs itérations au choix)
- Produire une moyenne par échantillon des 4 graphes précédemment cités.
    VOIR EXEMPLE mean_mat_manip2.txt.jpg

Le production du dernier graphe avec le calcul de moyenne implique d'uniformiser les tailles de matrices d'essais de durées variables.

## Résultats
On considère la moyenne comme le résultat par échantillon, ce calcul est pertinent car il n'y a pas de flyer.
On notera une faible incertitude sur la distribution de la charge \rho,
plus forte sur la distribution du champ E, certainement liée à un degré d'interpolation trop élevé induisant des oscillations parasites.

## Auteur
Application réalisée par Marc-Henri Stoll
