from datetime import datetime
from DataBase_Connection import *

class Departament:
    # Variabila de clasa care va contine obiecte de tip Departament
    lista_departamente = []

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
