import sys
from angajati import Angajat
from departament import Departament


def vizualizare():
    """ Reprezinta submeniul de vizualizare, care contine urmatoarele optiuni:
    1. Vizualizare a tuturor angajatilor in functie de departament
    2. Vizualizarea angajatilor dintr-un departament
    3. Iesire la meniul principal
    """
    # Functii pt asta == DONE
    pass


def informatii_firma():
    """ Reprezinta submeniul de informatii despre firma, care contine urmatoarele optiuni:
    1. Afisare medie salariala.
    2. Afisare nr angajati/ departament
    3. Afisare nr de angajati cu vechime mai mare de x ani.
    4. iesire la meniul principal
    """
    pass


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
        print("Meniu".center(35))
        print(40 * "=")
        print("1. Vizualizare\n2. Informatii despre firma\n3. Adaugare angajati\n4. Iesire")
        print(40 * "=")

        # Apelarea optiunii corespunzatoare input-ului
        match input("Introduceti optiune: "):
            case "1":
                Departament("IT").find_all_in_dep()
                vizualizare()
            case "2":
                informatii_firma()
            case "3":
                adaugare_angajati()
            case "4":
                sys.exit()
            case _:
                print("Nu ati introdus o optiune valida")


if __name__ == "__main__":
    main()
