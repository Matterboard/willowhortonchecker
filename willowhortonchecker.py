import sys

def main():
    # Ouvrez le fichier Word
    word_file = open("willow.docx", "rb")

    # Lisez la liste des mots de passe
    with open("mots_de_passe.txt", "r") as f:
        mots_de_passe = f.readlines()

    # Essayez tous les mots de passe
    for mot_de_passe in mots_de_passe:
        mot_de_passe = mot_de_passe.strip()
        try:
            # Essayez d'ouvrir le fichier avec le mot de passe
            word_file.open("rb", password=mot_de_passe.encode("utf-8"))
        except Exception as e:
            # Le mot de passe est incorrect
            pass
        else:
            # Le mot de passe est correct
            print("Le mot de passe est :", mot_de_passe)
            sys.exit()

if __name__ == "__main__":
    main()
