import sys
import os
import win32com.client
import docx

def main():
    # Chemin du fichier Word protégé par un mot de passe
    fichier_word = "C:\\Users\\Utilisateur\\OneDrive\\Documents\\willow.docx"

    # Lisez la liste des mots de passe
    with open("C:\\Users\\Utilisateur\\OneDrive\\Documents\\mots_de_passe.txt", "r") as f:
        mots_de_passe = f.readlines()

    # Créez une instance de l'application Word
    word_app = win32com.client.Dispatch("Word.Application")

    # Essayez tous les mots de passe
    for mot_de_passe in mots_de_passe:
        mot_de_passe = mot_de_passe.strip()
        try:
            # Ouvrez le fichier Word avec le mot de passe
            doc = word_app.Documents.Open(fichier_word, PasswordDocument=mot_de_passe)
        except Exception as e:
            # Le mot de passe est incorrect
            pass
        else:
            # Le mot de passe est correct
            print("Le mot de passe est :", mot_de_passe)
            doc.Close()
            word_app.Quit()
            sys.exit()

if __name__ == "__main__":
    main()
