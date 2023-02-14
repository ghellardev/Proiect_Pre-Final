from departament import *


class Angajat(Departament):
    # Variabila de clasa care va contine obiecte de tip Angajat

    def __init__(self, workdep, empname, job, hiredate, salary):
        """ Constructorul clasei Angajat. """
        super().__init__(workdep)
        self.empname = empname
        self.job = job
        self.hiredate = hiredate
        self.__salary = salary

