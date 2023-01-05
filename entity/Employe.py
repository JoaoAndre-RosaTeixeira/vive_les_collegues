
from datetime import datetime

class Employe:
    prenom: str = ""
    nom: str = ""
    date_entrer_entreprise = datetime.now()
    role = ""
    choose_D_M_Y = ["année", "month", "day"]

    def __str__(self):
        print(self.prenom)
        print(self.nom)
        print(self.get_date())
        print(self.role)
        return ""

    def get_date(self):
        return self.date_entrer_entreprise
