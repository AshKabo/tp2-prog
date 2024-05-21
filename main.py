'''
Votre description du programme
@auteur(e)s     X.Ashtonn X.Kabore et Y.Loic Y.Arson
@matricules     e6250834 et e6242959
@date              18-05-2024
'''
import csv
import json
import math


class DonneesGeo:
    def __init__(self, ville, pays, latitude, longitude):
        self.ville = ville
        self.pays = pays
        self.latitude = float(latitude)
        self.longitude = float(longitude)
    @property
    def v(self):
        return self.ville
    @v.setter
    def v(self, x):
        if isinstance(x, str):
            self.ville = x

    @property
    def p(self):
        return self.pays
    @p.setter
    def p(self, x):
        if isinstance(x, str):
            self.pays = x

    @property
    def la(self):
        return self.latitude
    @la.setter
    def la(self, x):
        if isinstance(x, float):
            self.latitude = x

    @property
    def lo(self):
        return self.longitude
    @lo.setter
    def lo(self, x):
        if isinstance(x, float):
            self.longitude = x

    def __str__(self):
        return f"Ville: {self.ville} Pays: {self.pays} Latitude: {self.latitude} Longitude: {self.longitude}"

def lireDonneesCsv(fi_csv):
    donnees = []
    with open(fi_csv, newline="") as fichier_csv :
        lecteur_csv = csv.reader(fichier_csv)
        #affetctation de chaque elements de la ligne a son attribut dans la classe DonnesGeo
        for ligne in lecteur_csv :
            ville = ligne[0]
            pays = ligne[1]
            latitude = ligne[2]
            longitude = ligne[3]
            donnees.append(DonneesGeo(ville,pays,latitude,longitude)) #a partir de l'affectation, creer un object
                                                                    #DonneesGeo pour chaque ligne du fichier csv et
                                                                    #rajoute ces objet dans une liste pour le print
    return donnees


def ecrireDonneesJson(fi_json, liste_donnees):
    liste_dicts = []
    for donnees in liste_donnees:
        dico = {
            "ville": donnees[0],
            "pays": donnees[1],
            "latitude": donnees[2],
            "longitude": donnees[3]
        }
        liste_dicts.append(dico)

    # Écrire la liste de dictionnaires dans le fichier JSON avec indentation
    with open(fi_json, 'w', encoding='utf-8') as fichier_json:
        json.dump(liste_dicts, fichier_json)

def Distance(la1, lo1, la2, lo2):
    r = 6371 #rayon de la terre en KM
    #transformation en radians des valeurs et deltas necessaires a la formule
    rad_la1 = math.radians(la1)
    rad_la2 = math.radians(la2)
    delt_la = math.radians(la2 - la1)
    delt_lo = math.radians(lo2 - lo1)

    #La formule de Haversine
    dist = 2 * r * math.asin(math.sqrt((math.sin(delt_la / 2.0) ** 2 + math.cos(rad_la1) * math.cos(rad_la2) * math.sin(delt_lo / 2.0) ** 2)))
    return dist

def trouverDistance(fi_json):
    with open(fi_json, "r", encoding="utf-8") as h:
        donnees = json.load(h)
        objgeo = [DonneesGeo(**i) for i in donnees]

    dist_min= float("inf")
    ville1, ville2= None, None

    distance_calc = []

    for i in range(len(objgeo)):
        for L in range(i+1, len(objgeo)):
            dist= Distance(objgeo[1].latitude, objgeo[1].longitude, objgeo[L].latitude, objgeo[L].longitude)
            distance_calc.append(objgeo[i], objgeo[L], dist)
            if dist < dist_min:
                dist_min=dist
                ville1, ville2 = objgeo[i], objgeo[L]


            #affiche les villes et leur distance minimale
        if ville1 and ville2:
            print(f" la distance entre la ville numéro 1 {ville1.ville}et la ville numéro 2{ville2.ville} est de {dist_min}")

#sert à enregistrer les données obtenues dans un fichier csv
    with open("distance.csv", mode="w", encoding="utf-8") as fi_csv:
        L=csv.writer(fi_csv)
        L.writerow(["Ville #1","Pays #1", "Ville #2", "Pays #2", "Distance minimale entre ces deux villes"])
        for ville1, ville2, dist in distance_calc :
            L.writerow([ville1.ville, ville1.pays, ville1.longitude, ville1.latitude, ville2.ville, ville2.pays, ville2.longitude, ville2.latitude])
def menu_princ():
    print("\nMenu: ")
    print("1- Lire les données du fichier csv, créer les objets et afficher les données.")
    print("2- Sauvegarder les données dans un fichier .json.")
    print("3- Lire les données du fichier .json, déterminer et afficher les données associées à la distance minimale entre deux villes et sauvegarder les calculs dans distances.csv.")
    print("Entrez un numéro pour choisir une option ou appuyez sur 'q' pour quitter :")

def menu():
    donnees = []
    json = False #indique si le fichier .json a ete sauvegarde
    while True:
        menu_princ() #affiche le menu principal
        choix = input("Veuillez entrer votre choix: ").strip()
        if choix == '1':
            donnees = lireDonneesCsv('donnees_geo.csv')
            print("Voici les données lues du fichier CSV :")
            for donnee in donnees:
                print(donnee) #lecture et impression des donnes lu dans le fichier csv
                              #avec la fonction lireDonneesCsv
            input("Appuyez sur une touche pour continuer...")
        elif choix == '2':
            if not donnees: #assure que les donnees ont ete lues avant de pouvoir sauvegarder en .json
                print("Lisez les données du fichier .csv avant de les sauvegarder en .json")
            else:
                ecrireDonneesJson('donnees_geo.json', donnees)
                json = True
        elif choix == '3':
            if not json: #assure que les donnees ont ete sauvegardees en .json avant calcul
                print("Sauvegardez les données en .json avant de calculer les distances.")
            else:
                trouverDistance('donnees_geo.json')
                input("Appuyez sur une touche pour continuer...")
        elif choix == 'q':
            break
        else:
            print("Choix invalide. Veuillez selectionner une option valide.")

menu()