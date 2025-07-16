#!/usr/bin/python
def generate_invitations(template, attendees):
   
    if type(template) is not str:
        print("Le template doit être une chaîne de caractères.")
        return
    if type(attendees) is not list or any(type(a) is not dict for a in attendees):
        print("La liste des invités doit être une liste de dictionnaires.")
        return

   
    if template.strip() == "":
        print("Template vide, aucun fichier généré.")
        return

    
    if len(attendees) == 0:
        print("Aucune donnée fournie, aucun fichier généré.")
        return

    champs = ['name', 'event_title', 'event_date', 'event_location']

    for i in range(len(attendees)):
        ligne = template
        for champ in champs:
            val = attendees[i].get(champ)
            if val is None or val == "":
                ligne = ligne.replace("{" + champ + "}", "N/A")
            else:
                ligne = ligne.replace("{" + champ + "}", str(val))
        try:
            with open("output_" + str(i+1) + ".txt", "w", encoding="utf-8") as f:
                f.write(ligne)
        except Exception as e:
            print("Erreur lors de l'écriture du fichier output_" + str(i+1) + ".txt :", e)
