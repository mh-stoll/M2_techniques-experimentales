'''
Mode d'emploi : 
	1 - Placer les données de la clé USB dans le sous-répertoire "/export_ronan"
	2 - Créer un dossier "picture" dans le répertoire du présent fichier .py pour la sauvegarde des graphiques
	3 - Supprimer les dernières lignes des fichiers de valeurs et insérer un "#" au début de la première ligne pour avoir un nombre constant de valeurs par lignes
'''

### --------------------------------------------------------------------------------------
### Bibliothèques externes
### --------------------------------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt
import os
import time

### --------------------------------------------------------------------------------------
### Utilitaire
### --------------------------------------------------------------------------------------

'''
Doc funct : var_name(var)
	entrée :
		variable
	sortie :
		nom de la variable au lieu de son "contenu"
	status : OK
'''

def var_name(var):
    for name,value in globals().items() :
        if value is var :
            return(name)
    return('err_funct_var_name')

'''
Doc funct : path_dir(my_directory)
	entrée :
		(le nom d'un dossier dans le même répertoire que ce scipt) néant
	sortie :
		(les sous répertoires de ce dossier) sous répertoires du dossier export_ronan
	status : OK
'''

def path_dir():
	os.chdir("export_ronan") # déplacement dans le sous répertoire
	result = os.listdir() # extraction du conenu
	os.chdir("..") # retour au point initial
	return(result)

### --------------------------------------------------------------------------------------
### Chargement des exports LATIS-Pro et LabView
### --------------------------------------------------------------------------------------

"""
Doc funct : str_to_mat(essaiN_M_PSP)
	entrée :
		chaine de caractère d'un fichier d'export
	sortie :
		matrice de nombres associées au fichier d'export
	status : OK
"""

def str_to_mat(nom_fichier):
	return(np.genfromtxt("export_ronan/"+nom_fichier))
	

### --------------------------------------------------------------------------------------
### Calcul des moyennes
### --------------------------------------------------------------------------------------

'''
CODE FONCTIONNEL ASSOCIÉ À MEAN MAT
m, n, p = 3779, 5, 2
mean_mat = np.zeros((m, n, p))#, dtype=np.float16)

manip1 = ["labview_results_0", "labview_results_1", "labview_results_2"]
manip2 = ["labview_results_2_0", "labview_results_2_1", "labview_results_2_2", "labview_results_2_3_1", "labview_results_2_4_1"]
'''
m1, n1 = 4059, 5
mean_mat1 = np.zeros((m1, n1))#, dtype=np.float16)
m2, n2 = 3779, 5
mean_mat2 = np.zeros((m2, n2))#, dtype=np.float16)

manip1 = ["labview_results_0", "labview_results_1", "labview_results_2"]
manip2 = ["labview_results_2_0", "labview_results_2_1", "labview_results_2_2", "labview_results_2_3_1", "labview_results_2_4_1"]
#manip3 = ["labview_results_3_0", "labview_results_3_1_1"]

''' inutile ?
manip_files = []
manip_files.append(manip1)
manip_files.append(manip2)
#manip_files.append(manip3)
'''

''' optimisation abandonnée
m1, n1, p1 = max([max(np.shape(str_to_mat(manip1[0]))), max(np.shape(str_to_mat(manip1[1]))), max(np.shape(str_to_mat(manip1[2])))]), 4, 3
manip1_mat = np.zeros((m1, n1, p1), dtype=np.float16)

for i in range(m1):
	print("manip1_mat loading {}%".format(round((i/m1)*100)))
	for j in range(n1):
		for k in range(p1):
			if k == 0:
				manip1_mat[i,j,k] = str_to_mat(manip1[0])[i,j]
			if k == 1:
				manip1_mat[i,j,k] = str_to_mat(manip1[1])[i,j]
			if k == 2:
				manip1_mat[i,j,k] = str_to_mat(manip1[2])[i,j]
print(manip1_mat)
'''
'''
CODE FONCTIONNEL, AJUSTEMENT DE LA TAILLE DE CHAQUE MATRICE DE MANIP
choice_mean_mat = int(input("Produce and save mean_mat ? (1/0) (be carreful ~30' processing) : "))

if choice_mean_mat == 1:
	start_time = time.time()
	for i in range(m):
		if i%2 == 0:
			dot = " ."
		else:
			dot = ". "
		print("mean_mat loading {}% {}".format(round((i/m)*100), dot), end="\r")
		i += 1
		for j in range(n):
			for k in range(p):
				#print(i, j, k)
				if k == 0:
					mean_mat[i-1,j,k] = np.mean([str_to_mat(manip1[0])[i,j], str_to_mat(manip1[1])[i,j], str_to_mat(manip1[2])[i,j]])
				if k == 1:
					mean_mat[i-1,j,k] = np.mean([str_to_mat(manip2[0])[i,j], str_to_mat(manip2[1])[i,j], str_to_mat(manip2[2])[i,j], str_to_mat(manip2[3])[i,j], str_to_mat(manip2[4])[i,j]])
		#print(mean_mat[i-1,:,:])

	for num_manip in range(2):
		np.savetxt("export_ronan/mean_mat_manip{}.txt".format(num_manip + 1), mean_mat[:,:,num_manip])
	print("Durée d'execution : {} min".format(round((time.time() - start_time)/60)))
'''

choice_mean_mat = int(input("Produce and save mean_mat1 mean_mat2 ? (0/1/2) (be carreful ~15' processing) : "))

if choice_mean_mat == 1:
	start_time = time.time()
	for i in range(m1):
		if i%2 == 0:
			dot = " ."
		else:
			dot = ". "
		print("mean_mat loading {}% {}".format(round((i/m1)*100), dot), end="\r")
		i += 1
		for j in range(n1):
			mean_mat1[i-1,j] = np.mean([str_to_mat(manip1[0])[i,j], str_to_mat(manip1[1])[i,j], str_to_mat(manip1[2])[i,j]])
	np.savetxt("export_ronan/mean_mat_manip{}.txt".format(choice_mean_mat), mean_mat1)
	print("Durée d'execution : {} min".format(round((time.time() - start_time)/60)))

if choice_mean_mat == 2:
	start_time = time.time()
	for i in range(m2):
		if i%2 == 0:
			dot = " ."
		else:
			dot = ". "
		print("mean_mat loading {}% {}".format(round((i/m2)*100), dot), end="\r")
		i += 1
		for j in range(n2):
			mean_mat2[i-1,j] = np.mean([str_to_mat(manip2[0])[i,j], str_to_mat(manip2[1])[i,j], str_to_mat(manip2[2])[i,j], str_to_mat(manip2[3])[i,j], str_to_mat(manip2[4])[i,j]])
	np.savetxt("export_ronan/mean_mat_manip{}.txt".format(choice_mean_mat), mean_mat2)
	print("Durée d'execution : {} min".format(round((time.time() - start_time)/60)))

'''
for i in range(m):
	i += 1
	for j in range(n):
		j += 1
		for k in range(p):
			print(i, j, k)
			if k == 0:
				mean_mat[i-1,j-1,k] = np.mean([str_to_mat(manip1[0])[i,j], str_to_mat(manip1[1])[i,j], str_to_mat(manip1[2])[i,j]])
			if k == 1:
				mean_mat[i-1,j-1,k] = np.mean([str_to_mat(manip2[0])[i,j], str_to_mat(manip2[1])[i,j], str_to_mat(manip2[2])[i,j], str_to_mat(manip2[3])[i,j], str_to_mat(manip2[4])[i,j]])
'''

### --------------------------------------------------------------------------------------
### Fonctions graphiques
### --------------------------------------------------------------------------------------

'''
Doc funct : latis_graph(essaiN_M_PSP)
	entrée :
		export LATIS-Pro.txt (matrice) ; nom pour l'image enregistrée (str) ; 1 pour activation du mode plt.show()
	sortie :
		graphique évolution temporelle de la tension en sortie de CAN (image du courant)
	status : OK
'''

def latis_graph(essaiN_M_PSP, save_name, show):
	plt.figure(figsize=(9,6))
	plt.plot(essaiN_M_PSP[:,0], essaiN_M_PSP[:,1])
	plt.xlabel("Temps ($s$)")
	plt.ylabel("Tension voie EA0 ($V$)")
	plt.title("Tension en sortie de CAN image du courant\n", fontsize=16)
	plt.savefig("picture/{}.eps".format(save_name))
	if show == 1:
		plt.show()
	print("saving ...")
	plt.close()

'''
Doc funct : labview_full(labview_results_N-M-P)
	entrée :
		export Labview (matrice) ; nom pour l'image enregistrée (str) ; 1 pour activation du mode plt.show()
	sortie :
		graphique évolution temporelle de toutes les variables en tab(2*2)
	status : OK
'''

def labview_full(labview_results_N_M_P, save_name, show):
	fig, ax = plt.subplots(2, 2, figsize=(15,12))
	t = labview_results_N_M_P[:,0]
	fig.suptitle("Traitement issu de l'application Labview fournie", fontsize=20)
	ax[0, 0].plot(t, labview_results_N_M_P[:,1])
	ax[0, 0].set_xlabel("Temps ($s$)")
	ax[0, 0].set_ylabel("$\delta t$ ($m$)")
	ax[0, 0].set_title("Réponse du matériaux à l'échelon de température")
	ax[0, 1].plot(labview_results_N_M_P[:,1], labview_results_N_M_P[:,2])
	ax[0, 1].set_xlabel("Distance ($m$)")
	ax[0, 1].set_ylabel("Champ $E$ ($V/m$)")
	ax[0, 1].set_title("Distribution du champ")
	ax[1, 0].plot(labview_results_N_M_P[:,1], labview_results_N_M_P[:,3])
	ax[1, 0].set_xlabel("Distance ($m$)")
	ax[1, 0].set_ylabel("$\\rho$ ($C.m^{-3}$)")
	ax[1, 0].set_title("Distribution de la charge")
	ax[1, 1].plot(t, labview_results_N_M_P[:,4])
	ax[1, 1].set_xlabel("Temps ($s$)")
	ax[1, 1].set_ylabel("Interpolation P")
	ax[1, 1].set_title("Interpolation de la variation de tension en sortie de CAN")
	title = var_name(labview_results_N_M_P)
	plt.savefig("picture/{}.eps".format(save_name))
	print("saving ...")
	if show == 1:
		plt.show()
	plt.close()

'''
Doc funct : graph_manip(mean_mat_manipN, save_name, show)
	entrée :
		Table des moyennes (matrice) ; nom pour l'image enregistrée (str) ; 1 pour activation du mode plt.show()
	sortie :
		graphique évolution temporelle de toutes les variables en tab(2*2) et moyenne pour chaque instant/distance
	status : OK
'''

def graph_manip(mean_mat_manipN, save_name, show):
	fig, ax = plt.subplots(2, 2, figsize=(15,12))
	fig.suptitle("Traitement issu de l'application Labview fournie et moyenne des mesures", fontsize=20)
	def label_it(num):#label itération n for plot "--"
		return("Mesure {}".format(num))
	label_moy = "Moyenne" #label for plot"-"
	alpha_set, linewidth_set = 0.7, 0.8
	num = 1
	if save_name == "mean_mat_manip1.txt":
		manip = manip1
	if save_name == "mean_mat_manip2.txt":
		manip = manip2
	for i in manip:
		labview_results_N_M_P = str_to_mat(i)
		t = labview_results_N_M_P[:,0]
		ax[0, 0].plot(t, labview_results_N_M_P[:,1], linestyle="--", alpha=alpha_set, linewidth=linewidth_set, label=label_it(num))
		ax[0, 1].plot(labview_results_N_M_P[:,1], labview_results_N_M_P[:,2], linestyle="--", alpha=alpha_set, linewidth=linewidth_set, label=label_it(num))
		ax[1, 0].plot(labview_results_N_M_P[:,1], labview_results_N_M_P[:,3], linestyle="--", alpha=alpha_set, linewidth=linewidth_set, label=label_it(num))
		ax[1, 1].plot(t, labview_results_N_M_P[:,4], linestyle="--", alpha=alpha_set, linewidth=linewidth_set, label=label_it(num))
		num += 1
	t = mean_mat_manipN[:,0]
	ax[0, 0].plot(t, mean_mat_manipN[:,1], color="r", label=label_moy)
	ax[0, 1].plot(mean_mat_manipN[:,1], mean_mat_manipN[:,2], color="r", label=label_moy)
	ax[1, 0].plot(mean_mat_manipN[:,1], mean_mat_manipN[:,3], color="r", label=label_moy)
	ax[1, 1].plot(t, mean_mat_manipN[:,4], color="r", label=label_moy)
	ax[0, 0].set_xlabel("Temps ($s$)")
	ax[0, 0].set_ylabel("$\delta t$ ($m$)")
	ax[0, 0].set_title("Réponse du matériaux à l'échelon de température")
	ax[0, 0].legend()
	ax[0, 1].set_xlabel("Distance ($m$)")
	ax[0, 1].set_ylabel("Champ $E$ ($V/m$)")
	ax[0, 1].set_title("Distribution du champ")
	ax[0, 1].legend()
#	ax[0, 1].set_yscale('log')
	ax[1, 0].set_xlabel("Distance ($m$)")
	ax[1, 0].set_ylabel("$\\rho$ ($C.m^{-3}$)")
	ax[1, 0].set_title("Distribution de la charge")
	ax[1, 0].legend()
#	ax[1, 0].set_yscale('log')
	ax[1, 1].set_xlabel("Temps ($s$)")
	ax[1, 1].set_ylabel("Interpolation P")
	ax[1, 1].set_title("Interpolation de la variation de tension en sortie de CAN")
	ax[1, 1].legend()
	title = var_name(labview_results_N_M_P)
	plt.savefig("picture/{}.eps".format(save_name))
	print("saving ...")
	if show == 1:
		plt.show()
	plt.close()


### --------------------------------------------------------------------------------------
### Execution
### --------------------------------------------------------------------------------------

#latis_graph(essai_0_PSP)
#labview_full(labview_results_0)

indice = 1
print("Script de production graphique.\nChoisir un numéro de fichier parmi la liste suivante :\n\n0 : All without show plot\n")
for i in path_dir():
	print("{} : {}\n".format(indice, i))
	indice += 1

choice = int(input("Choix utilisateur (choisir \"0\" pour l'ensemble) : "))
choice -= 1

first_letter_latis_export = "e"
first_letter_labview_export = "l"
first_letter_mean_mat = "m"

nb_files_in_exportronan_repertory = len(path_dir())

show = 1 # mode plt.show() activé

if choice in range(nb_files_in_exportronan_repertory):
	#On prélève la première lettre de la chaine de caractère associé au fichier choisi
	if path_dir()[choice][0] == first_letter_latis_export:
		latis_graph(str_to_mat(path_dir()[choice]), path_dir()[choice], show)
	if path_dir()[choice][0] == first_letter_labview_export:
		labview_full(str_to_mat(path_dir()[choice]), path_dir()[choice],show)
	if path_dir()[choice][0] == first_letter_mean_mat:
		graph_manip(str_to_mat(path_dir()[choice]), path_dir()[choice],show)

show = 0 # mode plt.show() désactivé

if choice == -1:
	for file in path_dir():
		if file[0] == first_letter_latis_export:
			latis_graph(str_to_mat(file), file, show)
		if file[0] == first_letter_labview_export:
			labview_full(str_to_mat(file), file, show)

if choice != -1 or choice not in range(nb_files_in_exportronan_repertory):
	print("Entrée non recevable")
