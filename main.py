import sys
from angajati import *
from os import system, name


def vizualizare():
    while True:
        clear()
        match input("1. Vizualizare a tuturor angajatilor in functie de departament\n"
                    "2. Vizualizarea angajatilor dintr-un departament\n"
                    "3. Iesire la meniul principal\n"):
            case "1":
                Departament.find_all()
                input("Apasati enter pentru a continua...")
            case "2":
                Departament(Departament.alegere_dep()).find_all_in_dep()
                input("Apasati enter pentru a continua...")
            case "3":
                break


def vizualizare_angajati():
    while True:
        clear()
        match input("1. Adaugare angajat\n"
                    "2. Stergere angajat\n"
                    "3. Actualizare nume angajat\n"
                    "4. Actualizare job angajat\n"
                    "5. Actualizare salariu angajat\n"
                    "6. Actualizare departament angajat\n"
                    "7. Iesire la meniul principal\n"):
            case "1":
                adaugare_angajati()
            case "2":
                Angajat.del_angajat(input("Nume angajat: "))
                input("Apasati enter pentru a continua...")
            case "3":
                Angajat.update_nume(input("Nume angajat: "))
                input("Apasati enter pentru a continua...")
            case "4":
                Angajat.update_job(input("Nume angajat: "))
                input("Apasati enter pentru a continua...")
            case "5":
                Angajat.update_salariu(input("Nume angajat: "))
                input("Apasati enter pentru a continua...")
            case "6":
                Angajat.update_dep(input("Nume angajat: "))
                input("Apasati enter pentru a continua...")
            case "7":
                break
            case _:
                print("Nu ati introdus o optiune valida")


def clear():
    # for mac and linux
    if name == 'posix':
        _ = system('clear')

    # for windows(here, os.name is 'nt')
    else:
        _ = system('cls')


def informatii_firma():
    while True:
        clear()
        match input("1. Afisare medie salariala.\n"
                    "2. Afisare nr angajati/ departament\n"
                    "3. Afisare nr angajati total\n"
                    "4. Afisare nr de angajati cu vechime mai mare de x ani\n"
                    "5. Iesire la meniul principal\n"):
            case "1":
                medie_salariala()
                input("Apasati enter pentru a continua...")
            case "2":
                angajat_pe_departament(Departament.alegere_dep())
                input("Apasati enter pentru a continua...")
            case "3":
                total_angajati()
                input("Apasati enter pentru a continua...")
            case "4":
                afisare_vechime(Departament.float_input("Introduceti nr ani: "))
                input("Apasati enter pentru a continua...")
            case "5":
                break


def medie_salariala():
    lista_suma = []
    for dep in Departament.dict_optiuni.values():
        cursor = list(Date_Angajati.find({"Departament": dep}, {"_id": 0, "Salariu": 1}))
        for i in cursor:
            lista_suma.append(i['Salariu'])
    print(f"Media salariala este: {round(sum(lista_suma) / len(lista_suma), 2)}")


def afisare_vechime(nr_ani: float):
    cursor = Date_Angajati.find({}, {"_id": 0, "Data": 1})
    counter = 0
    for i in cursor:
        if (datetime.now() - i["Data"]).days >= 365 * nr_ani:
            counter += 1
    print(f"Numarul de angajati cu vechime mai mare de {nr_ani} este: {counter}")


def angajat_pe_departament(dep):
    nr_angajati = Date_Angajati.count_documents({"Departament": dep})
    print(f'S-au gasit {nr_angajati} in Departamentul {dep}')
    return nr_angajati


def total_angajati():
    Departament.creare_dict_dep()
    nr_total = 0
    for i in Departament.dict_optiuni.values():
        nr_total += angajat_pe_departament(i)
    print(f'Numarul total de angajati este: {nr_total}')


def adaugare_angajati():
    Angajat(
        Departament.alegere_dep(),
        input("Introduceti numele angajatului: "),
        input("Introduceti pozitia angajat: "),
        Departament.data_input(),
        Departament.float_input("Introduceti salariul: ")
    ).add_angajat()


def main():
    while True:
        clear()
        print(40 * "=")
        print("Meniu".center(40))
        print(40 * "=")
        print("1. Vizualizare\n"
              "2. Informatii despre firma\n"
              "3. Adaugare departament\n"
              "4. Angajati\n"
              "5. Iesire")
        print(40 * "=")

        # Apelarea optiunii corespunzatoare input-ului
        match input("Introduceti optiune: "):
            case "1":
                vizualizare()
            case "2":
                informatii_firma()
            case "3":
                Departament.add_departament()
            case "4":
                vizualizare_angajati()
            case "5":
                sys.exit()
            case _:
                print("Nu ati introdus o optiune valida")


if __name__ == "__main__":
    main()
