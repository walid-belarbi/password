import random
import json
import hashlib

def generate_random_password():
    
    uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
    digits = "0123456789"
    special_characters = "!@#$%^&*;"

    # Permet de génerer un mot de passe aléatoire
    password = (
        random.choice(uppercase_letters)+
        random.choice(lowercase_letters)+
        random.choice(digits)+
        random.choice(special_characters)+
        ''.join(random.choice(uppercase_letters + lowercase_letters + digits + special_characters) for _ in range(8))
        
    )
    # Permet de mélanger les caractères
    password_list= list(password)
    random.shuffle(password_list)
    shuffled_password = ''.join(password_list)
    return shuffled_password

def hash_password(password):
    # Utiliser l'algorithme SHA-256 pour le hachage
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password

def load_passwords(filename="hashed_passwords.json"):
    try:
        # Ouvre le fichier en MODE Lecture et vérifie si il n'y a pas d'erreur
        with open(filename, 'r') as file:
            hashed_passwords = json.load(file)
    except FileNotFoundError:
        hashed_passwords= []
    return hashed_passwords

# Ouvre le fichier en MODE Écriture
def save_passwords(hashed_passwords,filename="hashed_passords.json"):
    with open(filename, "w") as file :
        json.dump(hashed_passwords, file , indent=4)
        
        
def is_duplicate_password(password, hashed_passwords):
    # Vérifier si le mot de passe est déjà dans la liste
    return any (hash_password(password) == hashed_pass for hashed_pass in hashed_passwords)

def main():
    
    hashed_passwords = load_passwords()
    
    while True:
        password = input("Veuillez Entrez votre mot de passe (ou g pour généré un mot de pase aléatoire): ")
        if password.lower() == 'g':
            # Générer un mot de passe aléatoire
            password = generate_random_password()
            print("Mot de passe aléatoire généré :", password)

            # Hacher le mot de passe généré aléatoirement
            hashed_password = hash_password(password)
            print("Mot de passe généré aléatoirement et hashé :", hashed_password)

            # Enregistrement du mot de passe généré aléatoirement
            save_option = input("Voulez-vous enregistrer ce mot de passe dans le fichier JSON ? (oui/non) ").lower()
            if save_option == 'oui':
                hashed_passwords.append(hashed_password)
                save_passwords(hashed_passwords)
                print("Mot de passe enregistré dans le fichier 'hashed_passwords.json'.")

            # Affichage de la liste des mots de passe
            show_option = input("Voulez-vous afficher la liste des mots de passe hashés ? (oui/non) ").lower()
            if show_option == 'oui':
                print("Liste des mots de passe hashés :", hashed_passwords)

            print("Mot de passe généré aléatoirement et hashé Validé.")

            # Demander à l'utilisateur s'il veut entrer un autre mot de passe
            continue_option = input("Voulez-vous entrer un autre mot de passe ? (oui/non) ").lower()
            if continue_option != 'oui':
                break
            
        # Vérifie la longueur du mot de passe
        elif len(password) < 8:
            print("Le mot de passe doit contenir au moins 8 caractères.")
        # Vérifie si le mot de passe contient au moins 1 majuscule
        elif not any(c.isupper() for c in password):
            print("Le mot de passe doit contenir au moins 1 majuscule.")
        # Vérifie si le mot de passe contient au moins 1 minuscule
        elif not any (c.islower() for c in password):
            print("Le mot de passe doit contenir au moins 1 minusucle")
        # Vérifie si le mot de passe contient au moins 1 chiffre
        elif not any (c.isdigit() for c in password):
            print("Le mot de passe doit contenir au moins 1 chiffre")
        #Vérifie si le mot de passe contient au moins 1 caractère spécial
        elif not any (c in "!@#$%^&*;" for c in password):
            print("Le mot de passe doit contenur au moins 1 caractère spécial (!, @, #, $, %, ^, &, *, ;).")
        # Vérifie si le mot de passe existe déja    
        elif is_duplicate_password(password, hashed_passwords):
            print("Ce mot de passe existe déjà. Veuillez en choisir un autre.")
        else:
            # Hashe le mot de passe
            hashed_password = hash_password(password)
            print("Mot de passe hashé :", hashed_password)
            
            # Demande si vous voulez enrengistrer le mot de passe dans le fichier JSON
            save_option = input("Voulez-vous enregistrer ce mot de passe dans le fichier JSON ? (oui/non) ").lower()
            if save_option == 'oui':
                hashed_passwords.append(hashed_password)
                save_passwords(hashed_passwords)
                print("Mot de passe enregistré dans le fichier 'hashed_passwords.json'.")
                
            # Demande si vous voulez affichez la liste des mot de passe hashé    
            show_option = input("Voulez-vous afficher la liste des mots de passe hashés ? (oui/non) ").lower()
            if show_option == 'oui':
                print("Liste des mots de passe hashés :", hashed_passwords)
            
            print("Mot de passe Validé.")
            
            #Demande si vous voulez entrez un nouveau mot de passe 
            continue_option = input("Voulez-vous entrer un autre mot de passe ? (oui/non) ").lower()
            if continue_option != 'oui':
                break

if __name__ == "__main__":
    main()