import cryptography

def main():
    # Générez un dictionnaire de mots de passe aléatoires
    password_list = []
    for i in range(10000):
        password = cryptography.fernet.generate_password()
        password_list.append(password)

    # Essayez tous les mots de passe
    for password in password_list:
        try:
            # Essayez d'ouvrir le fichier avec le mot de passe
            word_file = open("/home/kali/Desktop/willow.docx", "rb", password=password.encode("utf-8"))
        except Exception as e:
            # Le mot de passe est incorrect
            pass
        else:
            # Le mot de passe est correct
            print("Le mot de passe est :", password)
            sys.exit()

if __name__ == "__main__":
    main()
