from datetime import datetime
from DataBase_Connection import *


class Departament:
    # Variabila de clasa care va contine denumirile departamentelor deja existente in sistem
    lista_departamente = []

    # Variabila de clasa care va contine maparea intre "indexul unui departament si denumirea acestuia"
    dict_optiuni = {}

    def __init__(self, workdep: str):
        """ Constructorul clasei Departament. """
        self.workdep = workdep

    @classmethod
    def departamente(cls) -> None:
        cursor = Date_Angajati.find({}, {"_id": 0, "Departament": 1})
        [Departament.lista_departamente.append(i["Departament"]) for i in cursor if
         i["Departament"] not in Departament.lista_departamente]
        # for dep in Departament.lista_departamente:
        #     print(dep)

    @classmethod
    def creare_dict_dep(cls) -> None:
        Departament.departamente()
        counter = 0
        for i in Departament.lista_departamente:
            counter += 1
            Departament.dict_optiuni[str(counter)] = i

    @classmethod
    def alegere_dep(cls) -> str:
        Departament.creare_dict_dep()
        while True:
            for key, val in Departament.dict_optiuni.items():
                print(f"{key}. {val}")
            optiune = input("  Alegeti un dep: ")
            if optiune in Departament.dict_optiuni:
                return Departament.dict_optiuni[optiune]
            else:
                print("Nu ati introdus o optiune valida.")

    # Metoda folosita pentru a introduce o valoare float valida
    @classmethod
    def float_input(cls, mesaj_afisat) -> float:
        try:
            print(mesaj_afisat)
            return round(float(input()), 2)
        except ValueError:
            return Departament.float_input(mesaj_afisat)

    # Metoda folosita pentru a valida data introdusa
    @classmethod
    def data_input(cls) -> datetime:
        try:
            return datetime.strptime(input('Introduceti data de forma dd-mm-yyyy: '), "%d-%m-%Y")
        except ValueError:
            print("Data nu este valida!")
            return Departament.data_input()

    def find_all_in_dep(self) -> None:
        Departament.creare_dict_dep()
        print(40 * "=")
        print(self.workdep.center(40))
        print(40 * "=")
        for i in Date_Angajati.find({"Departament": self.workdep}, {"_id": 0}):
            for attr, value in i.items():
                if attr != "Data":
                    print(f"{attr}: {value}")
                else:
                    print(f"{attr}: {value.date()}")
            print(40 * "=")

    @classmethod
    def find_all(cls) -> None:
        Departament.creare_dict_dep()
        for dep in Departament.dict_optiuni.values():
            Departament(dep).find_all_in_dep()

    @classmethod
    def add_departament(cls) -> None:
        Departament.lista_departamente.append(input("Adaugati departament nou: "))
