'''
Votre description du programme
@auteur(e)s     X.Ashtonn X.Kabore et Y.Loic Y.Arson
@matricules     e6250834 et eYYYYYY
@date              18-05-2024
'''



class DonneesGeo:
    def __init__(self, ville, pays, latitude, longitude):
        self.ville = ville
        self.pays = pays
        self.latitude = latitude
        self.longitude = longitude
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
    