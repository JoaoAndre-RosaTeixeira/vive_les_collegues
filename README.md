doc disponible sur http://localhost:63342/vivelescollegues_joao-main/build/ 


before run this code pip install necessary is :
    pip install python-csv
    pip install GitPython
    pip install inquirer

next run the app in terminal with  : python main.py

now the app is running enter the informations of the new(s) salarie(s)

IMPORTANT !!! after all action please read the return of app to verify your information and validate with touch y or enter

enter nom

enter prénom

enter date to entrance in the company in order : Year -> Month -> Day

select the role he has in the company

now check the informations and validate

for the end choose to continue and repeat same things or stop the programme with button n and app push automatically the branch secretary on gitlab.

Please for the end use a merge request to claim to your superior confirm the new data and he merge it






guide utilisation : 

Se code est une fonction appelée automatise_reference_employes() qui permet de créer une référence d'un employé en demandant à l'utilisateur de saisir certaines informations telles que le nom, le prénom, la date d'entrée dans l'entreprise et le poste de l'employé.
La fonction utilise plusieurs sous-fonctions pour demander ces informations à l'utilisateur et vérifier que les entrées sont valides. La fonction add_name_class() demande et vérifie le nom ou le prénom de l'employé, tandis que la fonction add_datetime_class_date() demande et vérifie la date d'entrée de l'employé dans l'entreprise. La fonction add_role() utilise la bibliothèque inquirer pour afficher une liste de postes disponibles et demander à l'utilisateur de sélectionner un poste pour l'employé.
Enfin, la fonction confirm_questions() affiche une question à l'utilisateur et attend une réponse pour savoir si l'entrée de l'utilisateur est correcte ou non. Si l'entrée de l'utilisateur n'est pas correcte, les fonctions pertinentes sont appelées à nouveau jusqu'à ce qu'une entrée valide soit fournie.
Il y a également plusieurs lignes de commentaire qui ne sont pas utilisées dans le code actuellement exécuté. Ces lignes de commentaire semblent indiquer que le code pourrait être utilisé pour travailler avec l'API GitLab et les demandes de fusion de groupe.

