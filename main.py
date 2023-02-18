import sys
from angajati import *

def vizualizare():
    # TODO vizualizare() -> Erin + Alexandra
    # TODO 1. Vizualizare a tuturor angajatilor in functie de departament -> Departament.find_all()
    # TODO 2. Vizualizarea angajatilor dintr-un departament -> Departament(Departament.alegere_dep()).find_all_in_dep()
    # TODO 3. Iesire la meniul principal
    pass


def informatii_firma():
    # TODO informatii_firma() -> Simona + Ana
    # TODO 1. Afisare medie salariala.
    # TODO 2. Afisare nr angajati/ departament
    # TODO 3. Afisare nr de angajati cu vechime mai mare de x ani.
    # TODO 4. iesire la meniul principal
    pass

def angajat_pe_departament(dep):

    nr_angajati = Date_Angajati.count_documents({"Departament":dep })
    print(f'S-au gasit {nr_angajati} in Departamentul {dep}')
    return nr_angajati
def total_angajati():
    Departament.creare_dict_dep()
    nr_total= 0
    for i in Departament.dict_optiuni.values():
        print(i)
        nr_total += angajat_pe_departament(i)
    print(f'Numarul total de angajati este: {nr_total}')


def adaugare_angajati():
    Angajat(
        Departament.alegere_dep(),
        input("Introduceti numele angajatului: "),
        input("Introduceti pozitia angajat: "),
        Departament.data_input(),
        Departament.float_input()
    ).add_angajat()


def main():
    """ Functia de main a proiectului. Reprezinta meniul principal"""

    while True:
        print(40 * "=")
        print("Meniu".center(40))
        print(40 * "=")
        print("1. Vizualizare\n2. Informatii despre firma\n3. Adaugare departament\n4. Adaugare angajati\n5. Iesire")
        print(40 * "=")

        # Apelarea optiunii corespunzatoare input-ului
        match input("Introduceti optiune: "):
            case "1":
                vizualizare()
                Departament.find_all()
                total_angajati()
            case "2":
                informatii_firma()
            case "3":
                Departament.add_departament()
            case "4":
                adaugare_angajati()
            case "5":
                sys.exit()
            case _:
                print("Nu ati introdus o optiune valida")




if __name__ == "__main__":
    main()
    # angajat_pe_departament()