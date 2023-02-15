from datetime import datetime
from DataBase_Connection import *


class Departament:
    # Variabila de clasa care va contine denumirile departamentelor deja existente in sistem
    lista_departamente = []

    @classmethod
    def departamente(cls):
        cursor = Date_Angajati.find({}, {"_id": 0, "Departament": 1})
        [Departament.lista_departamente.append(i["Departament"]) for i in cursor if
         i["Departament"] not in Departament.lista_departamente]
        # for dep in Departament.lista_departamente:
        #     print(dep)

    @classmethod
    def alegere_dep(cls):
        dict_optiuni = {}
        counter = 0
        for i in Departament.lista_departamente:
            counter += 1
            dict_optiuni[str(counter)] = i
        for key, val in dict_optiuni.items():
            print(f"{key}. {val}")
        while True:
            optiune = input()
            if optiune in dict_optiuni:
                return dict_optiuni[optiune]
            else:
                print("Nu ati introdus o optiune valida.")

    def __init__(self, workdep):
        """ Constructorul clasei Departament. """
        self.workdep = workdep

    # Metoda folosita pentru a introduce o valoare float valida
    @classmethod
    def float_input(cls):
        try:
            return float(input())
        except ValueError:
            print("Introduceti un numar:")
            return Departament.float_input()

    # Metoda folosita pentru a valida data introdusa
    @classmethod
    def data_input(cls, data):
        try:
            return datetime.strptime(data, "%d-%m-%Y").date()
        except ValueError:
            print("Data nu este valida!")
            return None

    @classmethod
    def find_all(cls):
        print(35 * "=")
        for i in Date_Angajati.find({}, {"_id": 0}):
            for attr, value in i.items():
                print(f"{attr}: {value}")
            print(35 * "=")
        input("Press return to continue...")
