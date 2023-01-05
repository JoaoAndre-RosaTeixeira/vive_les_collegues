import csv
import datetime
from git import Repo

# import gitlab
# from gitlab.v4.objects import GroupMergeRequest

# Import de la classe Employe et Roles depuis le module entity
from entity.Employe import Employe
import inquirer
from entity.Roles import Roles


# Définition de la fonction automatise_reference_employes
def automatise_reference_employes():
    # Création d'une instance de la classe Employe
    new_employer = Employe()
    # Création d'une instance de la classe Roles
    roles = Roles()

    # Définition de la fonction add_name_class
    def add_name_class(str_class_name):
        # Initialisation de la variable class_name
        class_name = ""

        # Définition de la fonction input_name
        def input_name():
            # Demande de saisie de l'utilisateur
            return input(f"qu'elle est le {str_class_name} de l'employé a ajouter ? ")

        # Récupération de la saisie de l'utilisateur
        response = False
        while response == False:
            actual_input = input_name()

            # Vérifie que la saisie de l'utilisateur est une chaîne de caractères non vide et composee uniquement de lettres
            if len(actual_input) > 0 and actual_input.isalpha():
                # Met la saisie en minuscules et stocke la valeur dans class_name
                class_name = actual_input.lower()
                # Demande confirmation à l'utilisateur
                message = f"le {str_class_name} de l'employer est bien {class_name} ?"
                # Si la réponse est négative, relance la fonction
                if confirm_questions(message) == False:
                    add_name_class(str_class_name)
                else:
                    response = True
            # Si la saisie n'est pas valide, affiche un message d'erreur et relance la fonction
            else:
                print("error")

        # Renvoie la valeur de class_name
        return class_name

    # Définition de la fonction add_datetime_class_date
    def add_datetime_class_date():
        # Demande de saisie de l'utilisateur
        print(
            f"qu'elle est la date d'entrée dans l'entreprise de l'employé {new_employer.nom} {new_employer.prenom} ? ")

        # Liste des éléments à saisir (année, mois, jour)
        choose_D_M_Y = ["année", "month", "day"]

        # Définition de la fonction date_time_creator
        def date_time_creator():
            # Initialisation de la liste date_list

            date_list = []
            i_dmy = 0

            # Définition de la fonction input_date
            def input_date(message):
                # Demande de saisie de l'utilisateur
                return input(f"{message} : ")

            # Définition de la fonction D_M_Y_for
            def D_M_Y_for():
                # Récupération de l'élément courant de la liste choose_D_M_Y
                D_M_Y = choose_D_M_Y[i_dmy]
                # Récupération de la saisie de l'utilisateur
                res_input = input_date(D_M_Y)
                # Vérifie que la saisie de l'utilisateur est une chaîne de caractères non vide et composee uniquement de chiffres
                if res_input == "" or isinstance(int(res_input), int) == False:
                    # Si la saisie n'est pas valide, affiche un message d'erreur
                    print("erreur entrer seulement un nombre")
                    # Relance la fonction
                    D_M_Y_for()
                # Si l'élément courant est "année", vérifie que la saisie comporte bien 4 chiffres
                if D_M_Y == choose_D_M_Y[0]:
                    if len(res_input) != 4:
                        # Si la saisie n'est pas valide, affiche un message d'erreur
                        print("erreur l'année doit etre composer de 4 chiffres")
                        # Relance la fonction
                        D_M_Y_for()
                        return
                # Si l'élément courant est "mois", vérifie que la saisie est un nombre compris entre 1 et 12
                if D_M_Y == choose_D_M_Y[1]:
                    if int(res_input) > 12 or int(res_input) < 1:
                        # Si la saisie n'est pas valide, affiche un message d'erreur
                        print("erreur le mois doit etre compris entre 1 et 12")
                        # Relance la fonction
                        D_M_Y_for()
                        return
                # Si l'élément courant est "jour", vérifie que la saisie est un nombre compris entre 1 et 31
                if D_M_Y == choose_D_M_Y[2]:
                    if int(res_input) < 1 or int(res_input) > 31:
                        # Si la saisie n'est pas valide, affiche un message d'erreur
                        print("erreur le jour doit etre compris entre 1 et 31")
                        # Relance la fonction
                        D_M_Y_for()
                        return
                # Convertit la saisie en entier et stocke la valeur dans actual_input

                actual_input: int = int(res_input)
                # Demande confirmation à l'utilisateur
                year_question = f"le {D_M_Y} d'entrer est bien {actual_input} ?"
                # Si la réponse est négative, relance la fonction
                if confirm_questions(year_question) == False:
                    D_M_Y_for()
                    return
                # Ajoute la valeur de actual_input à la liste date_list
                date_list.append(actual_input)

            # Pour chaque élément de la liste choose_D_M_Y, appelle la fonction D_M_Y_for
            for D_M_Y in choose_D_M_Y:
                D_M_Y_for()
                # Incrémente la valeur de i_dmy
                i_dmy += 1
            # Renvoie la date créée à partir de la liste date_list
            return datetime.date(date_list[0], date_list[1], date_list[2])

        # Appelle la fonction date_time_creator et renvoie la valeur renvoyée
        return date_time_creator()

        # Définition de la fonction add_role
    def add_role():
        # Création d'un questionnaire avec la bibliothèque inquirer
        questions = [
            inquirer.List('position',
                          message="quel est sont poste ?",
                          choices=roles.roles,
                          ),
        ]
        # Récupération des réponses de l'utilisateur au questionnaire
        answers = inquirer.prompt(questions)
        # Demande confirmation à l'utilisateur
        role_question = f"Le poste actuel de {new_employer.nom} {new_employer.prenom} est bien {answers['position']} ?"
        # Si la réponse est négative, relance la fonction
        if confirm_questions(role_question) == False:
            add_role()
        # Renvoie la valeur de la réponse de l'utilisateur
        return answers['position']

        # Demande de saisie de l'utilisateur
        print("ajout d'un employé")
        # Appelle la fonction add_name_class et affecte la valeur renvoyée à la propriété nom de l'instance new_employer
        new_employer.nom = add_name_class("nom")
        # Appelle la fonction add_name_class et affecte la valeur renvoyée à la propriété prenom de l'instance new_employer
        new_employer.prenom = add_name_class("prenom")
        # Appelle la fonction add_datetime_class_date et affecte la valeur renvoyée à la propriété date_entre de l'instance new_employer
        new_employer.date_entre = add_datetime_class_date()

        # Appelle la fonction add_role et affecte la valeur renvoyée à la propriété role de l'instance new_employer
        new_employer.role = add_role()

        # Ouvre le fichier "employes.csv" en mode "a" (ajout de données à la fin du fichier)
        with open("employes.csv", "a") as csv_file:
            # Création d'un objet "writer" qui va écrire dans le fichier csv
            writer = csv.writer(csv_file, delimiter=',')
            # Ajoute les données de l'instance new_employer au fichier csv, sous forme de liste
            writer.writerow([new_employer.nom, new_employer.prenom, new_employer.date_entre, new_employer.role])

        # Récupère l'instance du dépôt git courant
        repo = Repo()
        # Vérifie que le dépôt n'est pas en "detached HEAD" state
        assert not repo.head.is_detached

        # Création d'un commit avec un message par défaut
        repo.index.commit("Ajout de l'employé {} {}".format(new_employer.nom, new_employer.prenom))
        # Pousse le commit sur le dépôt distant associé au dépôt local
        origin = repo.remote("origin")
        origin.push()

    # Cette fonction demande à l'utilisateur de confirmer quelque chose
    # et renvoie un booléen en fonction de sa réponse
    def confirm_questions(message):
        # Crée une liste de questions d'inquiry
        questions = [
            inquirer.Confirm("confirm", message=message,
                             default=True),
        ]
        # Demande à l'utilisateur de répondre aux questions
        answers = inquirer.prompt(questions)

        # Renvoie False si l'utilisateur n'a pas confirmé
        if answers["confirm"] != True:
            return False

    # Cette fonction est la fonction principale qui est appelée à la fin du script
    def start_programme():
        # Capture les informations de l'employé et les stock dans un objet de classe
        new_employer.nom = add_name_class("nom")
        new_employer.prenom = add_name_class("prénom")
        new_employer.date_entrer_entreprise = add_datetime_class_date()
        new_employer.role = add_role()

        # Affiche les informations de l'employé
        print(new_employer.__str__())

        # Définit les noms de champs pour le fichier CSV
        field_names = ['nom', 'prenom', 'date', 'poste']

        # Crée un dictionnaire des informations de l'employé à écrire dans le CSV
        to_csv_save = {
            "nom": new_employer.nom,
            "prenom": new_employer.prenom,
            "date": new_employer.get_date(),
            "poste": new_employer.role
        }

        # Ouvre le fichier CSV et écrit les informations de l'employé
        with open('ressource/employees.csv', 'a') as f_object:
            # Crée un objet DictWriter et écrit les informations de l'employé
            dictwriter_object = csv.DictWriter(f_object, fieldnames=field_names)
            dictwriter_object.writerow(to_csv_save)
            # Ferme l'objet de fichier
            f_object.close()

        # Demande à l'utilisateur s'il souhaite ajouter un autre employé
        if confirm_questions("ajouter un autre employé ?") != False:
            # S'il le souhaite, appelle à nouveau cette fonction
            return automatise_reference_employes()
        else:
            # Sinon, essaie de pousser les modifications vers un dépôt Git
            PATH_OF_GIT_REPO = r'.git'  # assurez-vous que le dossier .git est correctement configuré
            COMMIT_MESSAGE = 'commit from secretary'

        def git_push():
            try:
                # Initialise le dépôt et ajoute, valide et pousse les modifications
                repo = Repo(PATH_OF_GIT_REPO)
                repo.git.add(update=True)
                repo.index.commit(COMMIT_MESSAGE)
                repo.git.checkout("secretary")
                repo.git.push('origin')
                print('good push')
            except:
                # Affiche un message d'erreur s'il y a un problème
                print('Une erreur est survenue lors de la mise à jour du dépôt')

            git_push()


            # TOKEN = "glpat--xQxDwxfRXzXdCVRa6RS"
            # GITLAB_HOST = 'https://gitlab.com/simplonclermontia3/'  # or your instance
            # gl = gitlab.Gitlab(GITLAB_HOST, private_token=TOKEN)
            #
            #
            # GROUP_ID = 40034422
            #
            # def mr_meets_merge_criteria(mr: GroupMergeRequest) -> bool:
            #     """
            #     A function to check if it meets criteria to
            #     be merged automatically by this script
            #     """
            #     print(mr.project_id)
            #     print(mr.merge_status)  # e.g. 'can_be_merged'
            #     # check something
            #     ...
            #     return True | False
            #
            # group = gl.groups.get(GROUP_ID)
            #
            # # loop over all merge requests in the group
            # for mr in group.mergerequests.list(as_list=False):
            #     if mr_meets_merge_criteria(mr):
            #         project = gl.projects.get(mr.project_id, lazy=True)
            #         project_mr = project.mergerequests.get(mr.iid)
            #         project_mr.merge()

    start_programme()


automatise_reference_employes()
