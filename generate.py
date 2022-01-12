# permet de generé le fichier all.json contenant toutes les informations
# de tous les programmes disponibles

import json
import os

paths = [
    "linux",
    "macos",
    "windows"
]

current_path = os.path.dirname(os.path.realpath(__file__))

def generate_all_json():
    all_json = {}
    for path in paths:
        with open(path + "/all.json", "r") as f:
            all_json[path] = json.load(f)
            
    with open(current_path + "/all.json", "w") as f:
        json.dump(all_json, f, indent=4)

def create_new_script():
    systeme_exploitation = input("Quel système d'exploitation voulez-vous utiliser ? (linux, macos, windows) : ")
    if systeme_exploitation not in paths:
        print(f"Le système d'éxploitation {systeme_exploitation} n'est pas supporté")
        create_new_script()
    name = input("Nom du programme: ")
    description = input("Description: ")
    github_url = input("Github: ")
    version = input("Version du programme: ")
    install = input("Chemin du script d'installation: ")
    uninstall = input("Chemin du script de désinstallation: ")
    # copy script
    copy_file_from_path(install, systeme_exploitation + "/" + "install_" + name + ".sh")
    copy_file_from_path(uninstall, systeme_exploitation + "/" + "uninstall_" + name + ".sh")

    with open(systeme_exploitation + "/all.json", "r") as f:
        all_json = json.load(f)
        all_json[name].append({
            "enabled": True,
            "description": description,
            "github_url": github_url,
            "latest_version": version,
            "install": install,
            "uninstall": uninstall
        })
        # write to file
        with open(systeme_exploitation + "/all.json", "w") as f:
            json.dump(all_json, f, indent=4)
            print(f"Le programme {name} a été ajouté au système d'exploitation {systeme_exploitation}")

def enable_or_disable_script():
    systeme_exploitation = input("Quel système d'exploitation voulez-vous utiliser ? (linux, macos, windows) : ")
    if systeme_exploitation not in paths:
        print(f"Le système d'éxploitation {systeme_exploitation} n'est pas supporté")
        create_new_script()
    name = input("Nom du programme: ")
    action = input("Action (enable, disable): ")
    if action not in ["enable", "disable"]:
        print("Action non reconnue")
        enable_or_disable_script()
    with open(systeme_exploitation + "/all.json", "r") as f:
        all_json = json.load(f)
        if all_json[name]["enabled"] == True:
            all_json[name]["enabled"] = False
        if action == "enable":
            all_json[name]["enabled"] = True

        # write to file
        with open(systeme_exploitation + "/all.json", "w") as f:
            json.dump(all_json, f, indent=4)
            print(f"Le programme {name} a été {action}")

def update_script():
    systeme_exploitation = input("Quel système d'exploitation voulez-vous utiliser ? (linux, macos, windows) : ")
    if systeme_exploitation not in paths:
        print(f"Le système d'éxploitation {systeme_exploitation} n'est pas supporté")
        create_new_script()
    name = input("Nom du programme: ")
    with open(systeme_exploitation + "/all.json", "r") as f:
        all_json = json.load(f)
        for i in range(len(all_json[name])):
            if all_json[name][i]["enabled"] == True:
                all_json[name][i]["latest_version"] = input("Version du programme: ")
                all_json[name][i]["install"] = copy_file_from_path(input("Chemin du script d'installation: "), systeme_exploitation + "/" + "install_" + name + ".sh")
                all_json[name][i]["uninstall"] = copy_file_from_path(input("Chemin du script de désinstallation: "), systeme_exploitation + "/" + "uninstall_" + name + ".sh")
        # write to file
        with open(systeme_exploitation + "/all.json", "w") as f:
            json.dump(all_json, f, indent=4)
            print(f"Le programme {name} a été mis à jour")


def copy_file_from_path(source, destination):
    with open(source, "r") as f:
        with open(destination, "w") as f2:
            f2.write(f.read())

def delete_script():
    systeme_exploitation = input("Quel système d'exploitation voulez-vous utiliser ? (linux, macos, windows) : ")
    if systeme_exploitation not in paths:
        print(f"Le système d'éxploitation {systeme_exploitation} n'est pas supporté")
        create_new_script()
    name = input("Nom du programme: ")
    with open(systeme_exploitation + "/all.json", "r") as f:
        all_json = json.load(f)
        for i in range(len(all_json[name])):
            if all_json[name][i]["enabled"] == True:
                all_json[name][i]["enabled"] = False
        # write to file
        with open(systeme_exploitation + "/all.json", "w") as f:
            json.dump(all_json, f, indent=4)
            print(f"Le programme {name} a été supprimé")

def main():
    print("1. Créer un nouveau script")
    print("2. Activer/désactiver un script")
    print("3. Mettre à jour un script")
    print("4. Supprimer un script")
    print("5. Quitter")
    choice = input("Votre choix : ")
    if choice == "1":
        create_new_script()
    elif choice == "2":
        enable_or_disable_script()
    elif choice == "3":
        update_script()
    elif choice == "4":
        delete_script()
    elif choice == "5":
        exit()
    else:
        print("Choix non reconnu")
        main()

if __name__ == "__main__":
    generate_all_json()
    main()
    generate_all_json()