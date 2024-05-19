'''
Votre description du programme
@auteur(e)s     X.Ashtonn X.Kabore et Y.Loic Y.Arson
@matricules     e6250834 et eYYYYYY
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

def ecrireDonneesJson(fi_json, donnees):
    dico={"ville": donnees[0], "pays": donnees[1], "latitude": donnees[2], "longitude": donnees[3]}

    with open(fi_json, "r+") as fichier_json :
        json.dump(dico, fichier_json)

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

def trouverDistanceMin(nomFichier):
    ##### continu math ici

def menu():
    print("\nMenu: ")
    print("1- Lire les données du fichier csv, créer les objets et afficher les données.")
    print("2- Sauvegarder les données dans un fichier .json.")
    print("3- Lire les données du fichier .json, déterminer et afficher les données associées à la distance minimale entre deux villes et sauvegarder les calculs dans distances.csv.")
    print("Entrez un numéro pour choisir une option ou appuyez sur 'q' pour quitter :")

def menu_princ():
    #### continu le menu ici




