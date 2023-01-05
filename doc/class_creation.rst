Ici je presente comment j'ai creer les class lié a mon main
==============================================


La class employée
==============================================
.. code-block:: python


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

La class roles
==============================================
.. code-block:: python

    class Roles:
        roles = ["stagiaire", "Directeur général", "Digital Brand Manager", "Responsable communication", "Responsable marketing", "Directeur des opérations", "Directeur de site industriel", "Secrétaire général", "Directeur administratif et financier", "Chargé de communication", "directeur du système d’information"]